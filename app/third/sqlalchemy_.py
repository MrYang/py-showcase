from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from loguru import logger

Base = declarative_base()


def get_session():
    engine = create_engine('mysql+pymysql://root:123456@localhost/ctcms', echo=True)
    session = sessionmaker(bind=engine)
    return session()


class Admin(Base):
    __tablename__ = 'ct_admin'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column('nichen', String)


if __name__ == '__main__':
    admin = get_session().query(Admin).filter_by(id=1).first()
    logger.info(admin.id, admin.name)
