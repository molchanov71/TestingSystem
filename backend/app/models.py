__all__ = [
    'User',
]

import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from .db import Base


class User(Base, SerializerMixin):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)
