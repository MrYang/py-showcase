from loguru import logger
from sqlalchemy import Column, BigInteger, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    nickname = Column('nickname', String)


def get_session():
    engine = create_engine('mysql+pymysql://root:123456@localhost/docker', echo=True)
    session = sessionmaker(bind=engine)
    return session()


def query():
    return get_session().query(Admin).filter_by(id=1).first()


if __name__ == '__main__':
    admin = query()
    logger.info('admin id:{}, admin name:{}', admin.id, admin.name)
