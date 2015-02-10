import socket
import sys


msg = sys.argv[1]

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

client_socket.connect(('127.0.0.1', 50000))
client_socket.sendall(msg)
client_socket.shutdown(socket.SHUT_WR)
buffsize = 16
response = ""
done = False
while not done:
    part = client_socket.recv(buffsize)
    if len(part) < buffsize:
        done = True
    response = "{}{}".format(response, part)
client_socket.close()
print response
