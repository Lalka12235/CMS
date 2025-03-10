from fastapi import APIRouter
from app.data.article_model import Article, User, UpdateArticle
from app.db.orm import RemoteUser

user = APIRouter(tags=['Register'])

@user.post('/blogs/register/{username}')
async def register_user(username:str):
    register = RemoteUser.register_user(username)

    if not register:
        return {'Register': 'Not Success'}
    
    return {'Register': 'Success'}