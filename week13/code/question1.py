# 문제 1
# 두개의 자식 프로세스를 생성하고 두 자식 프로세스가 파이프를 통해 메시지를 송수신하는 프로그램을 작성하라.
# 첫번째 생성된 자식 프로세스는 "Hello"를 전송하고 두번째 생성된 자식 프로세스는 "Hello"를 수신하고 출력하도록 하라.
# 부모프로세스는 두 자식 프로세스가 모두 종료될때 까지 대기했다가 자식 프로세스들이 종료되면 종료되었음을 출력하라.

import os
def child_process1(pipe_out):
    os.close(pipe_out[0]) # 읽기 끝 닫기
    w = os.fdopen(pipe_out[1], 'w') # 쓰기 끝 파일 객체로 열기
    w.write("Hello")
    w.close()
    os._exit(0)

def child_process2(pipe_in):
    os.close(pipe_in[1]) # 쓰기 끝 닫기
    r = os.fdopen(pipe_in[0]) # 읽기 끝 파일 객체로 열기
    message = r.read()
    print(f"Parent process received : {message}")
    r.close()
    os._exit(0)

def parent_process(child_pid):
    print("Parent process (PID : {}) waiting for child process {}.".format(os.getpid(), child_pid))
    # 자식 프로세스가 종료될 때까지 블록 (0 옵션)
    pid, status = os.waitpid(child_pid, 0)
    print(f"Child process {pid} terminated with status {status}.")

def main():
    pipe_in, pipe_out = os.pipe() # 파이프 생성
    pid1 = os.fork() # 새로운 프로세스 생성
    if pid1 == 0:
        # 자식 프로세스
        child_process1((pipe_in, pipe_out))
    pid2 = os.fork()
    if pid2 == 0:
        child_process2((pipe_in, pipe_out))
    
    parent_process(pid1)
    parent_process(pid2)

if __name__ == "__main__":
    main()