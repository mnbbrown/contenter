from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from api.accounts.models import User
from api.accounts import exceptions
from datetime import timedelta, datetime
from api import config
from api.accounts import repository
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from starlette.status import HTTP_401_UNAUTHORIZED
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str):
    user = repository.get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_user(db: Session, email: str, password: str):
    hashed_password = get_password_hash(password)
    return repository.create_user(db, email, hashed_password)


def create_access_token(*, data: dict, expires_delta: timedelta = config.ACCESS_TOKEN_EXPIRES):
    to_encode = data.copy()
    to_encode.update({"type": "access", "exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, str(config.SECRET_KEY), algorithm=config.JWT_ALGORITHM)


def create_refresh_token(*, data: dict, expires_delta: timedelta = config.REFRESH_TOKEN_EXPIRES):
    to_encode = data.copy()
    to_encode.update({"type": "refresh", "exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, str(config.SECRET_KEY), algorithm=config.JWT_ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, str(config.SECRET_KEY), algorithms=[config.JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise exceptions.unauthorized
    user = get_user_by_id(db, user_id)
    if user is None:
        raise exceptions.unauthorized
    return user
