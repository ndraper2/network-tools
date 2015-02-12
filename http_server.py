# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import email.utils


def echo_server():
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
                msg = "{}{}".format(msg, part)
            out = "{}{}".format("I heard: ", msg)
            conn.sendall(out)
            conn.close()
    except KeyboardInterrupt:
        server_socket.close()


if __name__ == '__main__':
    echo_server()


def response_ok():
    response = ""
    date = email.utils.formatdate(usegmt=True)
    code = "HTTP/1.1 200 OK"
    content_type = "Content-Type: text/html; charset=UTF-8"
    response = "{}\r\n{}\r\n{}\r\n\r\n".format(code, date, content_type)
    response = response.encode('utf-8')
    return response


def response_error(err, msg):
    if err == 405:
        response = ""
        code = "HTTP1.1"
    pass


def parse_request(msg):
    lines = msg.split('\r\n')
    firstline = lines[0]
    words = firstline.split(' ')
    if words[0] != "GET":
        response_error(405, 'Method not allowed')
    if words[2] != "HTTP/1.1":
        response_error(505, "This server only supports HTTP 1.1")
    return words
