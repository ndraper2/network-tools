import socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

client_socket.connect(('127.0.0.1', 50000))
