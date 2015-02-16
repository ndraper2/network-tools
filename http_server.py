# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import email.utils
import mimetypes
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def http_server():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    server_socket.bind(('127.0.0.1', 50000))
    server_socket.listen(10)
    try:
        while True:
            conn, addr = server_socket.accept()
            buffsize = 16
            msg = ""
            done = False
            while not done:
                part = conn.recv(buffsize)
                if len(part) < buffsize:
                    done = True
                msg = b"{}{}".format(msg, part)
            out = parse_request(msg)
            conn.sendall(out)
            conn.close()
    except KeyboardInterrupt:
        server_socket.close()


def response_ok(uri):
    date = email.utils.formatdate(usegmt=True)
    code = "HTTP/1.1 200 OK"
    guess = mimetypes.guess_type(uri)[0]
    content_type = "Content-Type: {}; charset=UTF-8".format(guess)
    headers = "{}\r\n{}\r\n{}\r\n\r\n".format(code, date, content_type)
    response = "{}{}\r\n".format(headers, uri)
    return response


def response_error(err, msg):
    code = "HTTP/1.1 {} {}".format(err, msg)
    date = email.utils.formatdate(usegmt=True)
    content_type = "Content-Type: text/html; charset=UTF-8"
    response = "{}\r\n{}\r\n{}\r\n\r\n".format(code, date, content_type)
    return response


def parse_request(msg):
    if isinstance(msg, str):
        msg = msg.decode('utf-8')
    lines = msg.split('\r\n')
    firstline = lines[0]
    words = firstline.split(' ')
    if words[0] != "GET":
        response = response_error(405, 'Method not allowed\r\nAllow: GET')
    elif words[2] != "HTTP/1.1":
        response = response_error(505, "HTTP Version Not Supported")
    else:
        response = response_ok(words[1])
    return response.encode('utf-8')


def resolve_uri(uri):
    guess = mimetypes.guess_type(uri)[0]
    main, sub = guess.split('/')
    if main == 'text':
        f = open('.{}'.format(uri))
        txt = MIMEText(f.read(), _subtype=sub)
        f.close()
        return txt


if __name__ == '__main__':
    http_server()
