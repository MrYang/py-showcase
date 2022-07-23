import requests
from bs4 import BeautifulSoup
from faker import Faker
from loguru import logger


def parse_html():
    faker = Faker()
    headers = {'User-Agent': faker.chrome()}
    r = requests.get('https://www.baidu.com', headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    for img in soup.select('#s_lg_img'):
        src = img['src']
        logger.info(src)


if __name__ == '__main__':
    parse_html()
