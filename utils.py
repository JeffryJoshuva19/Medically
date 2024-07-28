from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
import os


class BaseConfig(object):
    SECRET_KEY = '691a03c2f0a7a449a00a394ca9deca08a3c4602f0995d8376bc60884c184c991'
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 100
    REFRESH_TOKEN_EXPIRE_MINUTES = 50

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire })
    encoded_jwt = jwt.encode(to_encode, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGORITHM)
    return encoded_jwt