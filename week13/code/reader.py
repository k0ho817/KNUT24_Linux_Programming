import os

fifo = 'mypipe'

# Named pipe에서 데이터를 읽기
with open(fifo, 'r') as pipe:
    while True:
        message = pipe.readline()
        if message:
            print(f"Read : {message.strip()}")
        else:
            break