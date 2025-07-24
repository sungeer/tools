"""读取文件内容
"""
from tools import settings

DATA_FILE = settings.DATA_DIR.joinpath('stream.log')


# 流式逐行读取
def read_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')  # 用 yield 每次返回一行


# 写入文件
def write_file():
    with open('error.log', 'w', encoding='utf-8') as out_file:
        for line in read_file(DATA_FILE):
            if '耗时' not in line:
                continue
            print(line)
            out_file.write(line + '\n')
