import os
import time

fifo = 'mypipe'

# Named pipe에 데이터를 쓰기
with open(fifo, 'w') as pipe:
    for i in range(5):
        message = f"message {i}"
        print(f"Writing : {message}")
        pipe.write(message + '\n')
        pipe.flush()
        time.sleep(1)