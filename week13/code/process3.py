import os
import time

def child_process(index):
    print("Child process {} (PID : {}) started.".format(index, os.getpid()))
    time.sleep(5 + index) # 자식 프로세스가 실행되는 시간 (5초 + index)
    print("Chhild process {} (PID : {}) finished.".format(index, os.getpid()))
    os._exit(0)

def parent_process(child_pid):
    print("Parent process (PID : {}) waiting for child process {}.".format(os.getpid(), child_pid))
    # 자식 프로세스가 종료될 때까지 블록 (0 옵션)
    pid, status = os.waitpid(child_pid, 0)
    print(f"Child process {pid} terminated with status {status}.")

def main():
    print("Main process (PID : {})".format(os.getpid()))
    # 첫 번째 자식 프로세스 생성
    pid1 = os.fork()
    if pid1 == 0:
        # 첫 번째 자식 프로세스
        child_process(1)
    # 두 번째 자식 프로세스 생성
    pid2 = os.fork()
    if pid2 == 0:
        # 두 번째 자식 프로세스
        child_process(2)
    
    # 부모 프로세스는 두 자식 프로세스의 종료를 차례로 기다림
    parent_process(pid1)
    parent_process(pid2)

if __name__ == "__main__":
    main()