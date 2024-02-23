from fastapi import Body, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from passlib.hash import sha512_crypt
from . import server
from .auth_bearer import JWTBearer
from .db.utils import create_session
from .models import *
from .schemas import *
from .utils import check_user, sign_jwt


@server.get('/')
def index():
    return JSONResponse({'success': 'OK'})


@server.get('/check')
def check():
    session = create_session()
    data = session.query(User).filter(User.id == 0).all()
    return JSONResponse(data)


@server.post('/register')
async def register(data: UserRegisterSchema):
    session = create_session()
    if data.password != data.password_again:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Пароли не совпадают')
    password_hash = sha512_crypt.hash(data.password)
    user = User(
        username=data.username,
        password_hash=password_hash
    )
    session.add(user)
    session.commit()
    return sign_jwt(data.username)


@server.post('/login')
async def login(user: UserLoginSchema=Body()):
    if check_user(user):
        return sign_jwt(user.username)
    return JSONResponse({'error': 'Неправильный логин или пароль!'}, status_code=status.HTTP_401_UNAUTHORIZED)


@server.get('/test', dependencies=[Depends(JWTBearer())])
async def test():
    return JSONResponse({'message': 'ok'})
