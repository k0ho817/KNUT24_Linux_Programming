'''
클라이언트가 소켓을 통해서 서버에 ls|wc를 전송한다.
서버는 두개의 자식 프로세스를 생성하고 첫번쩨 생성된 자식 프로세스는
ls명령을 실행하고 이때 생성된 결과를 두번째 자식 프로세스로 파이프를 통해서 전송한다.
두번째 생성된 자식 프로세스는 wc명령을 실행하고 wc명령의 입력은 첫번째 자식 프로세스가
전송하는 ls명령의 실행결과를 파이프를 통해서 입력받아 실행되도록 한다.
실행 결과는 클라이언트에 보내서 결과를 보여준다.
단, 동시에 10개의 클라이언트가 서버로 명령을 보내야 한다.
서버는 멀티 프로세스 기능을 이용하여 동시에 10개의 명령을 처리해서 클라이언트에 전송해야 한다.

bash를 이용하여 &로 백그라운드 실행 반복
fork()를 10번 수행
'''

import socket
import os

def child_process(index, command):

    os.__exit(0)

def handle_client(client_socket):
    try :
        command = client_socket.recv(1024).decode().split('|')
        command1 = command[0]
        command2 = command[1]

        pipe_in, pipe_out = os.pipe()

        pid1 = os.fork()
        if pid1 == 0:
            child_process(1)
        pid2 = os.fork()

        if pid1 == 0:
            os.dup2(client_socket.fileno(), 1)
            os.dup2(client_socket.fileno(), 2)

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