import os

from loguru import logger


def read(file):
    with open(file, mode='r') as f:
        return f.readlines()


if __name__ == '__main__':
    lines = read(os.path.abspath(__file__))
    logger.info([line.strip() for line in lines])
