from fastapi import FastAPI
from app.handler.blogs_router import article
from app.handler.admin_router import admin
from app.handler.user_router import user
from app.db.orm import InitDB

app = FastAPI()

app.include_router(article)
app.include_router(admin)
app.include_router(user)



if __name__ == '__main__':
    InitDB.create_table()