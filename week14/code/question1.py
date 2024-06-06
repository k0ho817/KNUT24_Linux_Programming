'''
두개의 자식 프로세스를 생성하고 두 자식 프로세스가 파이프를 통해 메시지를 송수신하는 프로그램을 작성하라.
첫번째 생성된 자식 프로세스 는 "Hello"를 전송하고 두번째 생성된 자식 프로세스는 "Hello"를 수신하고 출력하도록 하라.
부모 프로세스는 두 자식 프로세스가 모두 종료될때 까지 대기했다가 자식 프로세스들이 종료되면 종료되었음을 출력하라.
'''

import os

def child_process1(pOut):
    os.close(pOut[0])
    os.write(pOut[1], b"Hello")
    os.close(pOut[1])
    os._exit(0)

def child_process2(pIn):
    os.close(pIn[1])
    message = os.read(pIn[0], 1024)
    print(message.decode())
    os.close(pIn[0])
    os._exit(0)

def main():
    pIn, pOut = os.pipe()
    # 첫 번째 자식 프로세스 생성
    pid1 = os.fork()
    if pid1 == 0:
        # 첫 번째 자식 프로세스
        child_process1((pIn, pOut))
    # 두 번째 자식 프로세스 생성
    pid2 = os.fork()
    if pid2 == 0:
        # 두 번째 자식 프로세스
        child_process2((pIn,pOut))

    # 부모 프로세스는 두 자식 프로세스의 종료를 차례로 기다림
    os.close(pIn)
    os.close(pOut)

    os.waitpid(pid1, 0)
    os.waitpid(pid2, 0)
    print("pipe 통신 끝")


if __name__ == "__main__":
    main()
