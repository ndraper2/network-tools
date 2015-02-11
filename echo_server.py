import socket


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
