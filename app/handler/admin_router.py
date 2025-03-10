from fastapi import APIRouter
from app.db.orm import RemoteUser,RemoteArticle, RemoteAdmin

admin = APIRouter(tags=['Admin system'])

@admin.delete('/blogs/remote_user/delete_user',tags=['Admin system'])
async def delete_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        delete = RemoteAdmin.delete_user(username)

        if not delete:
            return {'Delete': 'Not success'}

        return {'Delete': 'Success'}
    
    else:
        return {'Law': 'Not enough'}
    

@admin.put('/blogs/remote_user/ban')
async def ban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        ban = RemoteAdmin.ban_user(username)

        if not ban:
            return {'Ban': 'Success'}

        return {'Ban': 'NotSuccess'}
    
    else:
        return {'Law': 'Not enough'}

@admin.put('/blogs/remote_user/unban')
async def unban_user_in_system(username:str):
    law = RemoteUser.have_admin(username)
    if law:
        unban = RemoteAdmin.unban_user(username)

        if not unban:
            return {'Unban': 'Success'}

        return {'Unban': 'Not Success'}
    else:
        return {'Law': 'Not enough'}


@admin.put('/blogs/remote_user/make_admin/{username}')
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

@admin.post('/blogs/remote_user/make_admin_test/{username}')
async def make_admin_user_fake(username:str):
    admin = RemoteAdmin.make_admin(username)
    return {'Admin': 'Success'}

@admin.put('/blogs/remote_user/unmake_admin/{username}')
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


@admin.put('/blogs/remote_article/ban_article/{username}/{title}')
async def ban_article(username:str,title:str):
    ban = RemoteArticle.ban_article(username,title)
    if ban:
        return {'Ban': 'True'}
    
    return {'Ban': 'False','Article':'Not found'}


@admin.put('/blogs/remote_article/unban_article/{username}/{title}')
async def unban_article(username:str,title:str):
    ban = RemoteArticle.unban_article(username,title)
    if ban:
        return {'UnBan': 'True'}
    
    return {'UnBan': 'False','Article':'Not found'}