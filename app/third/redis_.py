import redis
from loguru import logger


def get_redis():
    pool = redis.ConnectionPool(host='localhost', port=6379)
    return redis.StrictRedis(connection_pool=pool)


if __name__ == '__main__':
    r = get_redis()
    r.set('a', 1)
    logger.info(r.get('a'))
