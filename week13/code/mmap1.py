import mmap
import os

# 샘플 파일 생성
filename = 'sample.txt'
with open(filename, 'wb') as f:
    f.write(b'Hello, this is a sample text.')

# 파일을 메모리에 매핑하여 읽기 및 쓰기
with open(filename, 'r+b') as f:
    # 파일 크기 가져오기
    filesize = os.path.getsize(filename)

    # 파일을 메모리에 매핑
    with mmap.mmap(f.fileno(), length=filesize, access=mmap.ACCESS_WRITE) as m:
        # 매핑된 메모리에서 데이터 읽기
        original_content = m[:]
        print(f'Original content: {original_content.decode("utf-8")}')
        # 매핑된 메모리의 데이터 수정
        m[0:2] = b'Hi'
        m[2:] = b', this is the updated text.'

        # 수정된 내용 확인
        updated_content = m[:]
        print(f'Updated content : {updated_content.decode("utf-8")}')

# 수정된 파일 내용 확인
with open(filename, 'rb') as f:
    print(f'Final file content: {f.read().decode("utf-8")}')