from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    id: int
    title: str
    username: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

class User(BaseModel):
    username: str
    blogs: list[Article] = []
    is_admin: bool = False

class ADmin(User):
    is_admin: bool = True
