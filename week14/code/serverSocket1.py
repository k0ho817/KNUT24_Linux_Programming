import socket

def start_server():
    port = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f'Server is listening on port {port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected by {addr}')
        client_socket.sendall(b'Hello Client !')
        data = client_socket.recv(1024)
        print(f'Receied from client : {data.decode()}')
        client_socket.close()

if __name__ == '__main__':
    start_server()