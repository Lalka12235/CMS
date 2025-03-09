from fastapi import FastAPI
from app.handler.blogs_router import router
from app.db.orm import RemoteUser,RemoteArticle,InitDB

app = FastAPI()

app.include_router(router)



if __name__ == '__main__':
    InitDB.create_table()
    RemoteUser.register_user('Egor')
    RemoteArticle.create_articles('Egor',title='cms',description='Today i will make cms system')
    RemoteArticle.update_article('Egor',title='Update cms',description='I make update cms')