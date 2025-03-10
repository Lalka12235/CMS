from fastapi import APIRouter
from app.data.article_model import Article, User
from app.db.orm import RemoteUser,RemoteArticle, RemoteAdmin

router = APIRouter()


@router.post('/blogs/register/{username}',tags=['Register'])
async def register_user_in_system(username:str):
    register = RemoteUser.register_user(username)

    if not register:
        return {'Register': 'Not Success'}
    
    return {'Register': 'Success'}

@router.post('/blogs/remote_user/delete_user',tags=['Admin system'])
async def delete_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        delete = RemoteAdmin.delete_user(username)

        if not delete:
            return {'Delete': 'Not success'}

        return {'Delete': 'Success'}
    
    else:
        return {'Law': 'Not enough'}


@router.post('/blogs/remote_user/ban',tags=['Ban system'])
async def ban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        ban = RemoteAdmin.ban_user(username,'11.03.2024')

        if not ban:
            return {'Ban': 'Success'}

        return {'Ban': 'NotSuccess'}
    
    else:
        return {'Law': 'Not enough'}

@router.post('/blogs/remote_user/unban',tags=['Ban system'])
async def unban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        unban = RemoteAdmin.unban_user(username)

        if not unban:
            return {'Unban': 'Success'}

        return {'Unban': 'Not Success'}
    else:
        return {'Law': 'Not enough'}


#@router.post('/blogs/remote_user/{username}',tags=['Admin system'])
#async def make_admin_user(username:str):
#    law = RemoteUser.have_admin(username)
#
#    if law:
#        admin = RemoteUser.have_admin(username)
#        if not admin:
#            give_admin = RemoteAdmin.make_admin(username)
#            return {'Make admin': 'Success'}
#        else:
#            return {'Admin': 'User is Admin'}
#    else:
#        return {'Law': 'Not enough'}

@router.post('/blogs/remote_user/make_admin/{username}',tags=['Admin system'])
async def test_make_admin_user(username:str):
    admin = RemoteAdmin.make_admin(username)
    return {'Admin': 'Success'}

@router.post('/blogs/remote_user/unmake_admin/{username}',tags=['Admin system'])
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
    

@router.get('/blogs/{username}/{title}',tags=['Article system']) # Использовать модель user чтобы сделат вывод более корректный. Аннотация возвращаемоего типа - User 
async def get_blogs_on_username_title(username:str):
    data = RemoteArticle.select_articles(username)
    if not data:
        return {'Article': 'Not found'}
    
    return {username: data}

