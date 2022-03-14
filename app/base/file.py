import csv
import os

from loguru import logger


def read(file):
    with open(file, mode='r') as f:
        return f.readlines()


def csv_read(file):
    csv_reader = csv.reader(open(file, mode='r', encoding='utf-8'))
    for row in csv_reader:
        logger.info(row)


if __name__ == '__main__':
    lines = read(os.path.abspath(__file__))
    logger.info([line.strip() for line in lines])

    csv_read('../asset/read.csv')
