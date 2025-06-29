"""流式逐行读取
"""


def read_file_line_by_line(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')  # 用 yield 每次返回一行


def run():
    for line in read_file_line_by_line('huge.log'):
        if 'ERROR' in line:
            print(line)
