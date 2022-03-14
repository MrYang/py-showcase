import records

from loguru import logger

db = records.Database('mysql+pymysql://root:123456@localhost/ct')


def query():
    return db.query('select * from admin limit 10')


if __name__ == '__main__':
    rows = query()
    logger.info(rows)
