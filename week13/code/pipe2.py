import os

def child_process(pipe_out):
    os.close(pipe_out[0]) # 읽기 끝 닫기
    os.write(pipe_out[1], b"Hello from child process!")
    os.close(pipe_out[1])

def parent_process(pipe_in):
    os.close(pipe_in[1]) # 쓰기 끝 닫기
    message = os.read(pipe_in[0], 1024)
    print(f"Parent process received : {message.decode()}")
    os.close(pipe_in[0])

def main():
    pipe_in, pipe_out = os.pipe() # 파이프 생성
    pid = os.fork() # 새로운 프로세스 생성

    if pid == 0:
        # 자식 프로세스
        child_process((pipe_in, pipe_out))
    else:
        # 부모 프로세스
        parent_process((pipe_in, pipe_out))

if __name__ == "__main__":
    main()