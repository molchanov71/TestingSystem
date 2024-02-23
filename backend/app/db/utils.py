from sqlalchemy import orm
from sqlalchemy.orm import Session
from . import engine

factory = orm.sessionmaker(bind=engine)


def create_session() -> Session:
    return factory()
