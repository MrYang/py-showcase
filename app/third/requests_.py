import requests
from faker import Faker
from loguru import logger
from bs4 import BeautifulSoup


def parse_html():
    faker = Faker()
    headers = {'User-Agent': faker.chrome()}
    r = requests.get('https://www.zhihu.com/question/368001626/answer/1177831961', headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    for img in soup.select('.RichContent figure img'):
        src = img['src']
        if src.startswith('http'):
            logger.info(src)


if __name__ == '__main__':
    parse_html()
