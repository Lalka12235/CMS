from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    title: str
    username: str
    description: str
    have_banned: bool = False
    created_at: datetime = datetime.utcnow()
    updated_at: datetime | None = None

class UpdateArticle(BaseModel):
    description:str
    updated_at: datetime | None = None

class User(BaseModel):
    username: str
    have_banned:bool
    ban_expired: datetime
    blogs: list[Article] = []
    is_admin: bool = False

class ADmin(User):
    is_admin: bool = True
