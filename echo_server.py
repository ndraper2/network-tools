import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)
server_socket.bind(('127.0.0.1', 50000))
server_socket.listen(10)
i = 3  # the exact number of tests we have
while i > 0:
    conn, addr = server_socket.accept()
    msg = conn.recv(4096)
    out = "{}{}".format("I heard: ", msg)
    conn.sendall(out)
    conn.close()
    i -= 1
server_socket.close()
