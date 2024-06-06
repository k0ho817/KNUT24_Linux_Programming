import os
import time

def child_process():
    print("Child process (PID : {}) started.".format(os.getpid()))
    time.sleep(5) # 자식 프로세스가 5초 동안 실행됨
    print("Child process (PID : {}) finished.".format(os.getpid()))
    os._exit(0)

def parent_process(child_pid):
    print("Parent process (PID : {}) waiting for child process.".format(os.getpid()))
    # 자식 프로세스가 종료될 때까지 블록 ( 0 옵션 )
    pid, status = os.waitpid(child_pid, 0)
    print(f"Child process {pid} terminated with status {status}.")

def non_blocking_wait(child_pid):
    print("Non-blocking wait in parent process (PID : {}).".format(os.getpid()))
    # 자식 프로세스가 종료되지 않더라도 즉시 반환 (os.WNOHANG 옵션)
    pid, status = os.waitpid(child_pid, os.WNOHANG)
    if pid == 0:
        print("Child process has not terminated yet.")
    else:
        print(f"Child process {pid} terminated with status {status}")

def main():
    print("Main process (PID : {})".format(os.getpid()))
    pid = os.fork()

    if pid == 0:
        # 자식 프로세스
        child_process()
    else:
        # 부모 프로세스
        non_blocking_wait(pid) # 비블로킹 대기
        print("Parent can do something while wait for child")
        parent_process(pid) # 블로킹 대기

if __name__ == "__main__":
    main()