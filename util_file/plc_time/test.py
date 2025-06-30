import sqlite3
import secrets

from util_file import settings

DATA_FILE = settings.DATA_DIR.joinpath('m10_20250628.log')


def read_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


def get_data():
    with open('error.log', 'w', encoding='utf-8') as out_file:
        for line in read_file(DATA_FILE):
            if '耗时' not in line:
                continue
            print(line)
            out_file.write(line + '\n')



if __name__ == '__main__':
    get_data()
