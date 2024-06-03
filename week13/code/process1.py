import os

def child_process():
    print("Child process (PID : {})".format(os.getpid()))
    # 새로운 프로그램 실행
    os.execlp("ls", "ls", "-l")

def parent_process(child_pid):
    print("Parent process (PID : {})".format(os.getpid()))
    print("Waiting for child process (PID : {}) to finish...".format(child_pid))
    os.waitpid(child_pid, 0)
    print("Child process finished.")

def main():
    print("Main process (PID : {})".format(os.getpid()))
    pid = os.fork()

    if pid == 0:
        # 자식 프로세스
        child_process()
    else:
        # 부모 프로세스
        parent_process(pid)

if __name__ == "__main__":
    main()