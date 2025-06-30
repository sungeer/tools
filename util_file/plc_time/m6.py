import sqlite3
import secrets

from util_file import settings

DB_FILE = settings.DB_DIR.joinpath('m6_0629.db')

DATA_FILE = settings.DATA_DIR.joinpath('m6_20250629.log')


def creat_dbs():
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS mix (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_datetime TEXT NOT NULL,
            operation TEXT NOT NULL,
            duration_ms REAL NOT NULL
        );
    '''

    create_indexes_sql = [
        'CREATE INDEX IF NOT EXISTS log_datetime ON mix(log_datetime);',
        'CREATE INDEX IF NOT EXISTS idx_duration_ms ON mix(duration_ms);',
        'CREATE INDEX IF NOT EXISTS idx_operation ON mix(operation);'
    ]

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute(create_table_sql)

        # 执行所有索引创建语句
        for sql in create_indexes_sql:
            cursor.execute(sql)

        conn.commit()
    finally:
        cursor.close()
        conn.close()


def read_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


def generate_random_id(byte_length: int = 16) -> str:
    return secrets.token_hex(byte_length)


def add_log_data(data_list):
    sql_str = '''
        INSERT INTO mix (
            log_datetime, operation, duration_ms
        ) VALUES (?, ?, ?)
    '''
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.executemany(sql_str, data_list)
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


def get_data():
    burn_list = []
    for line in read_file(DATA_FILE):
        if '耗时' not in line:
            continue

        log_list = line.split(' - ')
        log_datetime = log_list[0]
        body_str = log_list[2]

        body_list = body_str.split(' ')
        operation = body_list[0].replace(':', '').replace('=================', '')
        duration_ms = str(float(body_list[1]) * 1000)

        data = (log_datetime, operation, duration_ms)
        burn_list.append(data)
        print(data)
    add_log_data(burn_list)


if __name__ == '__main__':
    creat_dbs()
    get_data()
