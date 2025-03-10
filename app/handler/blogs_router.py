from fastapi import APIRouter
from app.data.article_model import Article, User, UpdateArticle
from app.db.orm import RemoteUser,RemoteArticle, RemoteAdmin

router = APIRouter()


@router.post('/blogs/register/{username}',tags=['Register'])
async def register_user(username:str):
    register = RemoteUser.register_user(username)

    if not register:
        return {'Register': 'Not Success'}
    
    return {'Register': 'Success'}

@router.delete('/blogs/remote_user/delete_user',tags=['Admin system'])
async def delete_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        delete = RemoteAdmin.delete_user(username)

        if not delete:
            return {'Delete': 'Not success'}

        return {'Delete': 'Success'}
    
    else:
        return {'Law': 'Not enough'}


@router.put('/blogs/remote_user/ban',tags=['Ban system'])
async def ban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        ban = RemoteAdmin.ban_user(username)

        if not ban:
            return {'Ban': 'Success'}

        return {'Ban': 'NotSuccess'}
    
    else:
        return {'Law': 'Not enough'}

@router.put('/blogs/remote_user/unban',tags=['Ban system'])
async def unban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        unban = RemoteAdmin.unban_user(username)

        if not unban:
            return {'Unban': 'Success'}

        return {'Unban': 'Not Success'}
    else:
        return {'Law': 'Not enough'}


@router.put('/blogs/remote_user/make_admin/{username}',tags=['Admin system'])
async def make_admin_user(username:str):
    law = RemoteUser.have_admin(username)

    if law:
        admin = RemoteUser.have_admin(username)
        if not admin:
            give_admin = RemoteAdmin.make_admin(username)
            return {'Make admin': 'Success'}
        else:
            return {'Admin': 'User is Admin'}
    else:
        return {'Law': 'Not enough'}

@router.post('/blogs/remote_user/make_admin_test/{username}',tags=['Admin system'])
async def make_admin_user_fake(username:str):
    admin = RemoteAdmin.make_admin(username)
    return {'Admin': 'Success'}

@router.put('/blogs/remote_user/unmake_admin/{username}',tags=['Admin system'])
async def unmake_admin_user(username:str):
    law = RemoteUser.have_admin(username)

    if law:
        admin = RemoteUser.have_admin(username)
        if admin:
            take_admin = RemoteAdmin.deprivation_of_admin(username)
            return {'Unmake admin': 'Success'}
        else:
            return {'Admin': 'User is not Admin'}
    else:
        return {'Law': 'Not enough'}


@router.put('/blogs/remote_article/ban_article/{username}/{title}',tags=['Admin system'])
async def ban_article(username:str,title:str):
    ban = RemoteArticle.ban_article(username,title)
    if ban:
        return {'Ban': 'True'}
    
    return {'Ban': 'False','Article':'Not found'}


@router.put('/blogs/remote_article/unban_article/{username}/{title}',tags=['Admin system'])
async def unban_article(username:str,title:str):
    ban = RemoteArticle.unban_article(username,title)
    if ban:
        return {'UnBan': 'True'}
    
    return {'UnBan': 'False','Article':'Not found'}


@router.get('/blogs/remote_article/get_all_article/{username}',tags=['Article system']) # Использовать модель user чтобы сделат вывод более корректный. Аннотация возвращаемоего типа - User 
async def get_blogs_on_username_title(username:str):
    data = RemoteArticle.select_articles(username)
    if 'Article' in data or 'User' in data:  # Проверка на ошибку
        return data
    
    return {username: data}


@router.post('/blogs/remote_article/create_article/{username}/{title}',tags=['Article system'])
async def create_article(username:str,article:Article):
    create_articles = RemoteArticle.create_articles(username,article.title,article.description)
    return {'Article create': 'True', 'Article': create_articles}


@router.put('/blogs/remote_article/update_article/{username}/{title}',tags=['Article system'])
async def update_article(username:str,title:str,update: UpdateArticle):
    updated_articles = RemoteArticle.update_article(username,title,update.description)
    return {'Article update': 'True', 'Updated article': updated_articles}


@router.delete('/blogs/remoter_article/delete_article/{username}/{title}',tags=['Article system'])
async def delete_article(username:str,title:str):
    delete = RemoteArticle.delete_articles(username,title)
    return {'Article delete': 'True', 'Delete article': delete} 