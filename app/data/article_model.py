from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    title: str
    author: str
    description: str
    data: datetime

class User(BaseModel):
    username:str
    blogs: Article