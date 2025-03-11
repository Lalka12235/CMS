from fastapi import APIRouter, Depends, HTTPException
from app.db.orm import RemoteUser, RemoteAdmin
from app.auth.auth import get_current_admin

admin = APIRouter(tags=['Admin system'])

@admin.delete('/blogs/remote_user/delete_user',tags=['Admin system'])
async def delete_user_in_system(username: str, current_admin: str = Depends(get_current_admin)):
    if username != current_admin:
        raise HTTPException(status_code=403, detail="")

    delete = RemoteAdmin.delete_user(username)
    if delete:
        return {'Delete': 'Success'}
    return {'Delete': 'Not Success'}

@admin.put('/blogs/remote_user/ban',tags=['Admin system'])
async def ban_user_in_system(username: str, current_admin: str = Depends(get_current_admin)):
    if username != current_admin:
        raise HTTPException(status_code=403, detail="")

    ban = RemoteAdmin.ban_user(username)
    if ban:
        return {'Ban': 'Success'}
    return {'Ban': 'Not Success'}

@admin.put('/blogs/remote_user/unban',tags=['Admin system'])
async def unban_user_in_system(username: str, current_admin: str = Depends(get_current_admin)):
    if username != current_admin:
        raise HTTPException(status_code=403, detail="")

    unban = RemoteAdmin.unban_user(username)
    if unban:
        return {'Unban': 'Success'}
    return {'Unban': 'Not Success'}

@admin.put('/blogs/remote_user/make_admin/{username}',tags=['Admin system'])
async def make_admin_user(username: str, current_admin: str = Depends(get_current_admin)):
    if username != current_admin:
        raise HTTPException(status_code=403, detail="")

    admin_status = RemoteUser.have_admin(username)
    if admin_status:
        return {'Admin': 'User is already Admin'}
    result = RemoteAdmin.make_admin(username)
    return {'Make admin': 'Success' if result else 'Failure'}
