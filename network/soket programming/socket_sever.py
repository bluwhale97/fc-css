import socket
from time import ctime


host = 'localhost' # 127.0.0.1
port = 7979
bufsiz = 1024 # byte
addr = (host, port)

if __name__ == '__main__':
    # TCP/IP SOCKET정의
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding => TCP/IP소켓에다가 주소를 바인딩
    server_socket.bind(addr)

    # 소켓을 listen상태로 열어놓는다. 대기 수는 1명이다.
    server_socket.listen(1)
    # 소켓 옵션 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 
    while True:
        print("Socket Server is Listening on {host}:{port}".format(host = host, port = port))
        client_socket, client_addr = server_socket.accept()
        print("Client connected from : {addr}".format(addr = client_addr))

        while True:
            data = client_socket.recv(bufsiz)

            if not data or data == "END":
                break
            # elif data == "GET TIME":
            print("received data: {data}".format(data = data.decode('utf-8')))
            to_send = ctime()
            print("sending sever time : {}".format(to_send))
            
            try:
                client_socket.send(to_send.encode('utf-8'))
            except:
                print("Failed")

        client_socket.close()
    server_socket.close()

