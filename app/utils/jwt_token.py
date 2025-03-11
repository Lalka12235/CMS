import jwt 
from fastapi import HTTPException
from datetime import datetime,timedelta

SECRET_KEY = '43afac454e89a5df811fbd8d7b688ff2dbc921be4f5de19cc5a50be538f1eb9c'
ALGORITHM= 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def encode_jwt(payload, secret_key, algorithm, expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES):
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload.update({"exp": expire})
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


def decode_jwt(token, secret_key, algorithm):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=[algorithm])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
