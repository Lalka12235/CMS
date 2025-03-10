from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    id: int
    title: str
    username: str
    description: str
    have_banned: bool
    created_at: datetime
    updated_at: datetime | None = None

class User(BaseModel):
    username: str
    have_banned:bool
    ban_expired: datetime
    blogs: list[Article] = []
    is_admin: bool = False

class ADmin(User):
    is_admin: bool = True
