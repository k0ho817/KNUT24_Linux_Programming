import os
# 파일 열기 또는 생성
file_path = 'example2.txt'
flags = os.O_RDWR | os.O_CREAT # 읽기/쓰기 모드 및 파일이 없으면 생성
mode = 0o666 # 파일권한 (rw-rw-rw-)

# 파일 디스크립터 생성
fd = os.open(file_path, flags, mode)

# 파일에 쓰기
os.write(fd, b'Hello, this is a test created using os.open().')

# 파일 포인터를 처음으로 이동
os.lseek(fd, 0, os.SEEK_SET)

# 파일에서 읽기
data = os.read(fd, 100)
print(f'Read data : {data.decode()}')

# 파일 닫기
os.close(fd)