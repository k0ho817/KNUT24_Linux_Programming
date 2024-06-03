import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 9999))

    command = input("Enter command to execute : ")
    client_socket.sendall(command.encode())

    result = client_socket.recv(4096).decode()
    print(f'Command output : \n {result}')

    client_socket.close()

if __name__ == "__main__":
    start_client()