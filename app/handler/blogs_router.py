from fastapi import APIRouter
from app.data.article_model import Article, User, UpdateArticle
from app.db.orm import RemoteArticle

article = APIRouter(tags=['Article system'])


@article.get('/blogs/remote_article/get_all_article/{username}') 
async def get_blogs_on_username_title(username:str):
    data = RemoteArticle.select_articles(username)
    if 'Article' in data or 'User' in data:
        return data
    
    return {username: data}


@article.post('/blogs/remote_article/create_article/{username}/{title}')
async def create_article(username:str,article:Article):
    create_articles = RemoteArticle.create_articles(username,article.title,article.description)
    return {'Article create': 'True', 'Article': create_articles}


@article.put('/blogs/remote_article/update_article/{username}/{title}')
async def update_article(username:str,title:str,update: UpdateArticle):
    updated_articles = RemoteArticle.update_article(username,title,update.description)
    return {'Article update': 'True', 'Updated article': updated_articles}


@article.delete('/blogs/remoter_article/delete_article/{username}/{title}')
async def delete_article(username:str,title:str):
    delete = RemoteArticle.delete_articles(username,title)
    return {'Article delete': 'True', 'Delete article': delete} 