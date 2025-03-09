from fastapi import FastAPI
from app.handler.blogs_router import router
from app.db.orm import create_table,register_user,create_articles,delete_articles,update_article,make_admin,deprivation_of_admin

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    create_table()
    register_user('Egor')