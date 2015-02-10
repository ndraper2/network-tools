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
    i -= 1
server_socket.close()
