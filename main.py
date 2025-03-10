from fastapi import FastAPI
from app.handler.blogs_router import router
from app.db.orm import InitDB

app = FastAPI()

app.include_router(router)



if __name__ == '__main__':
    InitDB.create_table()