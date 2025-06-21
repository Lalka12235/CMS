from fastapi import FastAPI
from app.handler.blogs_router import article
from app.handler.admin_router import admin
from app.handler.user_router import user
from app.auth.auth import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='CMS System',
    description='API for managing blog posts, users, and admin tasks'
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080/docs",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

app.include_router(article)
app.include_router(admin)
app.include_router(user)
app.include_router(auth)