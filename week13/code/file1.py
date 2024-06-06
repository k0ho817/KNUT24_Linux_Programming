import os

# 파일열기
fd = os.open('example1.txt', os.O_RDWR | os.O_CREAT)

# 파일쓰기
os.write(fd, b'Hello, this is a test') # fd에 binary로 인코딩

# 파일 포인터를 처음으로 이동
os.lseek(fd, 0, os.SEEK_SET) # 0으로 이동

# 파일에서 읽기
data = os.read(fd, 100) # 100byte 읽어라
print(f'Read date : {data.decode()}') # binary 코드를 다시 디코딩

# 파일 포인터를 특정 위치로 이동
os.lseek(fd, 7, os.SEEK_SET) # 7로 이동

# 파일에서 읽기
data = os.read(fd, 100)
print(f'Read data from position 7 : {data.decode()}')

# 파일 닫기
os.close(fd)