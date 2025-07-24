import sqlite3

from tools import settings

DB_FILE = settings.DB_DIR.joinpath('20250724.db')


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


if __name__ == '__main__':
    pass
