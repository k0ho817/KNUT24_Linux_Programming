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


import os
import socket

def handle_client_connection(client_socket):
    r, w = os.pipe()
    r2, w2 = os.pipe()
    
    pid1 = os.fork()

    if pid1 == 0:
        # 첫 번째 자식 프로세스
        os.close(r)
        os.close(r2)
        os.close(w2)
        
        os.dup2(w, 1)  # 표준 출력을 첫 번째 파이프의 쓰기 끝으로 리디렉션
        os.close(w)
        
        os.execlp('ls', 'ls')  # 'ls' 명령어 실행
        os._exit(0)

    pid2 = os.fork()

    if pid2 == 0:
        # 두 번째 자식 프로세스
        os.close(w)
        os.close(w2)
        
        os.dup2(r, 0)  # 첫 번째 파이프의 읽기 끝을 표준 입력으로 리디렉션
        os.close(r)
        
        os.dup2(w2, 1)  # 표준 출력을 두 번째 파이프의 쓰기 끝으로 리디렉션
        os.close(w2)
        
        os.execlp('wc', 'wc')  # 'wc' 명령어 실행
        os._exit(0)

    os.close(r)
    os.close(w)
    os.close(w2)
    
    output = os.read(r2, 1024)
    os.close(r2)
    
    client_socket.sendall(output)
    client_socket.close()
    
    os.waitpid(pid1, 0)
    os.waitpid(pid2, 0)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9999))
    server_socket.listen(10)
    print("Server listening on port 9999")
    
    for _ in range(10):
        pid = os.fork()
        if pid == 0:
            while True:
                client_sock, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")
                handle_client_connection(client_sock)

if __name__ == '__main__':
    start_server()

'''

import socket
import os

def handle_client(client_socket):
    try :
        command = client_socket.recv(4096).decode()
        cmd1, cmd2 = tuple(command.split("|"))

        pIn1, pOut1 = os.pipe()
        pIn2, pOut2 = os.pipe()

        # 첫 번째 자식 프로세스 생성
        pid1 = os.fork()
        if pid1 == 0:
            # 첫 번째 자식 프로세스
            os.close(pIn2)
            os.close(pOut2)
            os.close(pIn1)
            os.dup2(pOut1, 1)
            os.close(pOut1)
            os.execlp(cmd1, cmd1)

        
        # 두 번째 자식 프로세스 생성
        pid2 = os.fork()
        if pid2 == 0:
            # 두 번째 자식 프로세스
            os.close(pIn2)
            os.close(pOut1)
            os.dup2(pIn1, 0)
            os.close(pIn1)
            os.dup2(pOut2, 1)
            os.close(pOut2)
            os.execlp(cmd2, cmd2)

        else :
            os.waitpid(pid1, 0)
            os.waitpid(pid2, 0)

        os.close(pIn1)
        os.close(pOut1)
        os.close(pOut2)

        result = os.read(pIn2, 2048)
        os.close(pIn2)

        client_socket.sendall(result)

        os.waitpid(pid1, 0)
        os.waitpid(pid2, 0)
        os._exit(0)

    except Exception as e:
        client_socket.sendall(f'Error : {str(e)}'.encode())
    finally:
        client_socket.close()

def start_server():
    port = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(10)
    print(f'Server is listening on port {port}')

    for _ in range(10):
        pid = os.fork()
        if pid == 0:
            while True:
                client_socket, addr = server_socket.accept()
                print(f'Connected by {addr}')
                handle_client(client_socket)
        os.waitpid(pid, 0)

if __name__ == "__main__":
    start_server()
'''