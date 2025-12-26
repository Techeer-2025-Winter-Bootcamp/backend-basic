import logging
import os
from time import time, sleep

import MySQLdb


def mysql_is_ready():
    check_timeout = 120
    check_interval = 5
    start_time = time()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # 환경 변수에서 DB 설정 가져오기
    db_host = os.getenv('DB_HOST', 'mysqldb')
    db_user = os.getenv('DB_USER', 'sa')
    db_password = os.getenv('DB_PASSWORD', '1234')
    db_name = os.getenv('DB_NAME', 'mydatabase')

    while time() - start_time < check_timeout:
        try:
            conn = MySQLdb.connect(
                host=db_host,
                port=3306,
                user=db_user,
                passwd=db_password,
                db=db_name
            )
            conn.close()
            logger.info("MySQL Connected Successfully.")
            return True
        except Exception as e:
            logger.info(f"Waiting for MySQL... ({e})")
            sleep(check_interval)

    logger.error(f"Could not connect to {db_host}:3306 within {check_timeout} seconds.")
    return False


if __name__ == '__main__':
    mysql_is_ready()
