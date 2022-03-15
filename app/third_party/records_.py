import records

from loguru import logger

db = records.Database('mysql+pymysql://root:123456@localhost/docker')


def query():
    return db.query('select * from admin limit 10')


if __name__ == '__main__':
    rows = query()
    for row in rows:
        logger.info(row)
