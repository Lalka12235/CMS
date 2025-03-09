from sqlalchemy import create_engine,insert,delete,update,select
from sqlalchemy.orm import sessionmaker
from app.data.orm_model import Base, Users,Articles
from app.config import settings
from datetime import datetime

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

Session = sessionmaker(engine)

class InitDB:

    @staticmethod
    def create_table():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        return {'Create db': 'True'}

class RemoteUser:

    @staticmethod
    def register_user(username):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username)).scalars().first()

            if exist_user:
                return {'Create user': 'User already exists'}
            
            result = session.execute(insert(Users).values(username=username,is_admin=False))
            session.commit()
            return result
    
    @staticmethod
    def delete_user(username):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username)).scalars().first()

            if exist_user:
                stmt = session.execute(delete(Users).where(Users.username == username))
                session.commit()
                return stmt
            
            return {'User':'Not found'}
        
    @staticmethod
    def make_admin(username):
        with Session() as session:
            stmt = update(Users).where(Users.username == username).values(is_admin=True)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def deprivation_of_admin(username):
        with Session() as session:
            stmt = update(Users).where(Users.username == username).values(is_admin=False)
            session.execute(stmt)
            session.commit()


class RemoteArticle:

    @staticmethod
    def create_articles(username:str,title:str,description:str):
        with Session() as session:
            user = session.execute(select(Users).where(Users.username == username)).scalars().first()

            if not user:
                return {'error': 'User not found'}
            
            new_article = Articles(
                title=title,
                description=description,
                username=username,
                user_id=user.id,  # связываем статью с пользователем
                created_at=datetime.utcnow(),  # устанавливаем время создания
                updated_at=datetime.utcnow()   # устанавливаем время обновления
            )

        
            session.add(new_article)
            session.commit()

    @staticmethod
    def update_article(username:str,title:str,description:str,):
        with Session() as session:
            exist_article = session.execute(select(Articles).where(Articles.username == username)).scalars().first()

            if not exist_article:
                return {'Error': 'Article not found'}

            exist_article.title = title
            exist_article.description = description
            exist_article.updated_at = datetime.utcnow()

            session.commit()

    @staticmethod
    def delete_articles(username,title):
        with Session() as session:
            result = session.execute(delete(Articles).where(Articles.username == username, Articles.title == title))
            session.commit()
            return result
    

