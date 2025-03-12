from fastapi import APIRouter
from app.data.pydantic_model import RegisterUser
from app.db.orm import RemoteUser

user = APIRouter(tags=['Register'])

@user.post('/blogs/register')
async def register_user(user:RegisterUser):
    register = RemoteUser.register_user(user.username,user.password)
    if not register:
        return {'Register': 'Not Success'}
    return {'Register': 'Success'}
