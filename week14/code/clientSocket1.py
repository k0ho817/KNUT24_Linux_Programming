import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    data = client_socket.recv(1024)
    print(f'Received from server: {data.decode()}')
    client_socket.sendall(b"Hello, Server !")
    client_socket.close()

if __name__ == "__main__":
    start_client()