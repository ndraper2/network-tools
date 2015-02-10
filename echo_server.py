import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)
server_socket.bind(('127.0.0.1', 50000))
server_socket.listen(1)
conn, addr = server_socket.accept()
msg = conn.recv(4096)
out = "{}{}".format("I heard: ", msg)
conn.sendall(out)
conn.close()
server_socket.close()
