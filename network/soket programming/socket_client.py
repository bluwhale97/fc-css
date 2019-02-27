import socket

host = "localhost"
port = 7979
bufsize = 2048

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter hostname[{host}]: ".format(host = host)) or host
    port = input("Enter port number[{port}]: ".format(port = port)) or port

    addr = (host, int(port))
    client_socket.connect(addr)

    # 명령 패킷을 payload라고 한다.
    payload = "GET TIME"

    try:
        while True:
            client_socket.send(payload.encode('utf-8'))
            data = client_socket.recv(bufsize)
            print(data.decode('utf-8'))
            
            more = input("Want more(y/n)?: ")
            if more.lower() == "y":
                payload = input("What do you want?") or payload
            else:
                break
    except:
        print("Something Wrong!")

    client_socket.close()