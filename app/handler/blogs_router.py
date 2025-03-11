from fastapi import APIRouter,Depends, HTTPException
from app.data.pydantic_model import Article, User, UpdateArticle
from app.db.orm import RemoteArticle
from app.auth.auth import get_current_user

article = APIRouter(tags=['Article system'])


@article.get('/blogs/remote_article/get_all_article/{username}')
async def get_blogs_on_username_title(username: str, current_user: str = Depends(get_current_user)):
    data = RemoteArticle.select_articles(username)
    if 'Article' in data or 'User' in data:
        return data
    return {username: data}



@article.post('/blogs/remote_article/create_article/{username}/{title}')
async def create_article(username:str,article:Article,current_user: str = Depends(get_current_user)):
    if username != current_user:
        raise HTTPException(status_code=403, detail="You can only delete your own articles")

    create_articles = RemoteArticle.create_articles(username,article.title,article.description)
    return {'Article create': 'True', 'Article': create_articles}


@article.put('/blogs/remote_article/update_article/{username}/{title}')
async def update_article(username:str,title:str,update: UpdateArticle,current_user: str = Depends(get_current_user)):
    if username != current_user:
        raise HTTPException(status_code=403, detail="You can only delete your own articles")

    updated_articles = RemoteArticle.update_article(username,title,update.description)
    return {'Article update': 'True', 'Updated article': updated_articles}


@article.delete('/blogs/remoter_article/delete_article/{username}/{title}')
async def delete_article(username:str,title:str,current_user: str = Depends(get_current_user)):
    if username != current_user:
        raise HTTPException(status_code=403, detail="You can only delete your own articles")

    delete = RemoteArticle.delete_articles(username,title)
    return {'Article delete': 'True', 'Delete article': delete} 