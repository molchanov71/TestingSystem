import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_URL = 'sqlite:///backend/app/db/app.db?check_same_thread=False'

engine = sa.create_engine(SQLALCHEMY_URL, echo=False)
Base = declarative_base()
