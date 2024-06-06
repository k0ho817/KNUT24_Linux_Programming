'''
클라이언트가 소켓을 통해서 서버에 ls|ws를 전송한다.
서버는 두개의 자식 프로세스를 생성하고 첫번쩨 생성된 자식 프로세스는
ls명령을 실행하고 이때 생성된 결과를 두번째 자식 프로세스로 파이프를 통해서 전송한다.
두번째 생성된 자식 프로세스는 wc명령을 실행하고 wc명령의 입력은 첫번째 자식 프로세스가
전송하는 ls명령의 실행결과를 파이프를 통해서 입력받아 실행되도록 한다.
실행 결과는 클라이언트에 보내서 결과를 보여준다.
단, 동시에 10개의 클라이언트가 서버로 명령을 보내야 한다.
서버는 멀티 프로세스 기능을 이용하여 동시에 10개의 명령을 처리해서 클라이언트에 전송해야 한다.
'''

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    client_socket.sendall(b"ls|wc")

    res = client_socket.recv(1024)
    print("Response from server:")
    print(res.decode())
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

'''
import socket

def send_command():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    
    # 명령어 전송
    command = "ls | wc"
    client_socket.sendall(command.encode())
    
    response = client_socket.recv(4096)
    print("Response from server:")
    print(response.decode())
    
    client_socket.close()

if __name__ == '__main__':
    send_command()
    '''