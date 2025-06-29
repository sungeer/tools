import sqlite3
import secrets

from util_file import settings

DB_FILE = settings.DB_DIR.joinpath('mix.db')

DATA_FILE = settings.DATA_DIR.joinpath('huge.log')


def creat_dbs():
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS mix (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            random_id TEXT NOT NULL,
            log_date TEXT NOT NULL,
            hour TEXT NOT NULL,
            minute TEXT NOT NULL,
            second TEXT NOT NULL,
            millisecond TEXT NOT NULL,
            log_datetime TEXT NOT NULL,
            operation TEXT NOT NULL,
            duration_ms REAL NOT NULL
        );
    '''

    create_indexes_sql = [
        'CREATE INDEX IF NOT EXISTS idx_random_id ON mix(random_id);',
        'CREATE INDEX IF NOT EXISTS idx_log_date ON mix(log_date);',
        'CREATE INDEX IF NOT EXISTS idx_hour ON mix(hour);',
        'CREATE INDEX IF NOT EXISTS idx_minute ON mix(minute);',
        'CREATE INDEX IF NOT EXISTS idx_second ON mix(second);',
        'CREATE INDEX IF NOT EXISTS idx_millisecond ON mix(millisecond);',
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
            random_id, log_date, hour, minute, second, millisecond,
            log_datetime, operation, duration_ms
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
    random_id_up = ''
    random_id_burn = ''
    upload_list = []
    burn_list = []
    for line in read_file(DATA_FILE):
        if '耗时' not in line:
            continue

        log_list = line.split(' - ')
        log_datetime = log_list[0]
        body_str = log_list[2]

        if '上传耗时' in line:
            random_id_up = generate_random_id()
        if '获取芯片UID耗时' in line:
            random_id_burn = generate_random_id()

        body_list = body_str.split(' ')
        operation = body_list[0].replace(':', '')
        duration_ms = body_list[1]

        datetime_list = log_datetime.split(' ')
        log_date = datetime_list[0]

        time_list = datetime_list[1].split(':')
        hour = time_list[0]
        minute = time_list[1]

        second_list = time_list[2].split('.')
        second = second_list[0]
        millisecond = second_list[1]

        if operation in ['上传耗时', '上传结果写入耗时', '统计耗时']:
            data = (random_id_up, log_date, hour, minute, second, millisecond, log_datetime, operation, duration_ms)
            upload_list.append(data)
            print(data)
            continue
        data = (random_id_burn, log_date, hour, minute, second, millisecond, log_datetime, operation, duration_ms)
        burn_list.append(data)
        print(data)
    add_log_data(upload_list)
    add_log_data(burn_list)


if __name__ == '__main__':
    creat_dbs()
    get_data()
