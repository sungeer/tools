"""Gevent 协程
将数据库操作放入单独的线程池中
"""
from gevent import monkey

monkey.patch_all(thread=False, subprocess=False)

import MySQLdb
from flask import Flask, jsonify
from pebble import ThreadPool
from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

request_pool = Pool(50)
thread_db_pool = ThreadPool(max_workers=50)


def query_from_db(sql):
    # 这里要用自己的连接池，不要用全局连接
    conn = MySQLdb.connect(host='localhost', user='root', passwd='xxx', db='test')
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


@app.route('/data')
def data():
    future = thread_db_pool.submit(query_from_db, "SELECT * FROM mytable")
    try:
        result = future.result(timeout=3)  # 阻塞等待结果，但只阻塞当前协程，不会卡住整个 gevent
        return jsonify(result)
    except TimeoutError:
        return jsonify({'error': 'DB timeout'}), 504


if __name__ == '__main__':
    # server = WSGIServer(('0.0.0.0', 8848), app, log=None, spawn=request_pool)
    server = WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()
