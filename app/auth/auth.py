from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils.jwt_token import encode_jwt, decode_jwt, SECRET_KEY, ALGORITHM
from app.utils.hash import verify_pass
from app.db.orm import RemoteUser

auth = APIRouter(tags=['Auth'])

# URL для получения токена
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token, SECRET_KEY, ALGORITHM)
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token or expired")

def get_current_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token, SECRET_KEY, ALGORITHM)
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_is_admin = RemoteUser.have_admin(username)
        if not user_is_admin:
            raise HTTPException(status_code=403, detail="Insufficient privileges")
        
        return username
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token or expired")


@auth.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = RemoteUser.login_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_pass(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = encode_jwt({"sub": form_data.username}, SECRET_KEY, ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}