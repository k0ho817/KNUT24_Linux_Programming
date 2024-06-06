import os
def child_process(pipe_out):
    os.close(pipe_out[0]) # 읽기 끝 닫기
    w = os.fdopen(pipe_out[1], 'w') # 쓰기 끝 파일 객체로 열기
    w.write("Hello from child process!")
    w.close()

def parent_process(pipe_in):
    os.close(pipe_in[1]) # 쓰기 끝 닫기
    r = os.fdopen(pipe_in[0]) # 읽기 끝 파일 객체로 열기
    message = r.read()
    print(f"Parent process received : {message}")
    r.close()

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