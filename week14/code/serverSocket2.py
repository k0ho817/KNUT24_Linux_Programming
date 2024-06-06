import socket
import os

def handle_client(client_socket):
    try :
        command = client_socket.recv(1024).decode()
        if not command :
            return
        
        pid = os.fork()

        if pid == 0:
            os.dup2(client_socket.fileno(), 1)
            os.dup2(client_socket.fileno(), 2)
            os.execlp(command.split()[0], *command.split())
        else :
            os.waitpid(pid, 0)
    except Exception as e:
        client_socket.sendall(f'Error : {str(e)}'.encode())
    finally:
        client_socket.close()

def start_server():
    port = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f'Server is listening on port {port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected by {addr}')
        handle_client(client_socket)

if __name__ == '__main__':
    start_server()