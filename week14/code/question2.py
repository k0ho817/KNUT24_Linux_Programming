'''
두개의 자식 프로세스를 생성하고 두 자식 프로세스가 파이프를 통해
메시지를 송수신하는 프로그램을 작성하라.
첫번째 생성된 자식 프로세스는 ls명령을 실행하고 이때 생성된 결과를 두번째 자식 프로세스로 파이프를 통해서 전송한다.
두번째 생성된 자식 프로세스는 wc명령을 실행하고 wc명령의 입력은 첫번째 자식 프로세스가 전송하는 ls명령의 실행결과를 파이프를 통해서 입력받아 실행되도록 한다.
'''

import os

def child_process1(pOut):
    os.close(pOut[0])
    os.dup2(pOut[1], 1)
    os.close(pOut[1])
    os.execlp('ls', 'ls')
    os._exit(0)

def child_process2(pIn):
    os.close(pIn[1])
    os.dup2(pIn[0], 0)
    os.close(pIn[0])
    os.execlp('wc', 'wc')
    os._exit(0)

def main():
    pIn, pOut = os.pipe()
    # 첫 번째 자식 프로세스 생성
    pid1 = os.fork()
    print(pid1)
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
