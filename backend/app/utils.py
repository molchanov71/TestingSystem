import time
from typing import Dict
from decouple import config
import jwt
from passlib.hash import sha512_crypt
from .db.utils import create_session
from .models import *
from .schemas import UserLoginSchema

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def token_response(token: str):
    return {
        'access_token': token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'expires': time.time() + 600,
    }
    token = jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM,])
        if decoded_token['expires'] >= time.time():
            return decoded_token
        return None
    except BaseException as err:
        print(err)
        return {}


def check_user(data: UserLoginSchema):
    session = create_session()
    user = session.query(User).filter(User.username == data.username).one()
    if not sha512_crypt.verify(data.password, user.password_hash):
        return False
    return True
