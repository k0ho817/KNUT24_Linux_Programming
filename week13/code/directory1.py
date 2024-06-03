import os

# 디렉토리 생성
dir_name = 'example_dir'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f'Directory "{dir_name}" created.')
else:
    print(f"Directory '{dir_name}' already exists.")

# 디렉토리 변경
os.chdir(dir_name)
print(f"Changed current directory to '{dir_name}'.")

# 파일 생성
fd = os.open('example1.txt', os.O_RDWR | os.O_CREAT, 0o666)
os.close(fd)

# 부모 디렉토리로 이동하여 디렉토리 내용 읽기
os.chdir('..')
# 디렉토리 열기 및 내용 읽기
with os.scandir(dir_name) as entries:
    print(f"Contents of directory '{dir_name}' : ")
    for entry in entries:
        print(entry.name)

# 디렉토리 제거
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")
else:
    print(f"Directory '{dir_name}' does not exitst")