import os
import sys

# 리디렉션할 파일 열기
filename = 'output.txt'
with open(filename, 'w') as f:
    # 현재 stdout의 파일 디스크립터 저장
    saved_stdout = os.dup(1)

    # stdout을 파일 디스크립터로 복제하여 리디렉션
    os.dup2(f.fileno(), 1)

    try:
        # 이제 stdout이 파일로 리디렉션됨
        print("This will be written to the file.")
    finally:
        # 원래 stdout으로 복구
        os.dup2(saved_stdout, 1)
        os.close(saved_stdout)

print("This will be printed on the console.")