from sqlalchemy import create_engine,insert,delete,update,select
from sqlalchemy.orm import sessionmaker
from app.data.orm_model import Base, Users,Articles
from app.config import settings
from datetime import datetime
from app.utils.hash import make_hash_pass

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
    def register_user(username:str,password:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username)).scalars().first()
            hash_pass = make_hash_pass(password)

            if exist_user:
                return {'Create user': 'User already exists'}
            
            result = session.execute(insert(Users).values(username=username,password=hash_pass,is_admin=False,have_banned=False))
            session.commit()
            return result
        
    @staticmethod
    def login_user(username: str):
        with Session() as session:
            user = session.execute(select(Users).where(Users.username == username)).scalars().first()
            return user
        
    @staticmethod
    def have_admin(username:str):
        with Session() as session:
            admin = session.execute(select(Users).where(Users.username == username,Users.is_admin == True))

            if not admin:
                return False
            
            return True
        
    

class RemoteAdmin:

    @staticmethod
    def delete_user(username:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username,Users.is_admin == True)).scalars().first()

            if exist_user:
                stmt = session.execute(delete(Users).where(Users.username == username))
                session.commit()
                return stmt
            
            return {'User':'Not found'}
        
    @staticmethod
    def make_admin(username:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username)).scalars().first()
            law = session.execute(select(Users).where(Users.username == username,Users.is_admin == True)).scalars().first()

            if not exist_user:
                return {'User': 'Not found'}
            if law:
                return {'Admin':' User is admin'}

            stmt = update(Users).where(Users.username == username).values(is_admin=True)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def deprivation_of_admin(username:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username,Users.is_admin == True)).scalars().first()

            if not exist_user:
                return {'User': 'Not found'}

            stmt = update(Users).where(Users.username == username).values(is_admin=False)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def ban_user(username:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username,Users.is_admin == True)).scalars().first()

            if not exist_user:
                return {'User': 'Not found'}
            
            stmt = update(Users).where(Users.username == username).values(have_banned=True)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def unban_user(username:str):
        with Session() as session:
            exist_user = session.execute(select(Users).where(Users.username == username,Users.is_admin == True)).scalars().first()

            if not exist_user:
                return {'User': 'Not found'}
            
            stmt = update(Users).where(Users.username == username).values(have_banned=False)
            session.execute(stmt)
            session.commit()

class RemoteArticle:

    @staticmethod
    def select_articles(username:str):
        with Session() as session:
            user = session.execute(select(Users).where(Users.username == username)).scalars().first()

            if not user:
                return {'User': 'Not found'}
            
            stmt = select(Articles).where(Articles.username == username,Articles.have_banned == False)
            articles = session.execute(stmt).scalars().all()
            return articles

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
                have_banned=False,
                created_at=datetime.utcnow(),  # устанавливаем время создания
                updated_at=datetime.utcnow()   # устанавливаем время обновления
            )

        
            session.add(new_article)
            session.commit()
            return new_article

    @staticmethod
    def update_article(username:str,title:str,description:str):
        with Session() as session:
            exist_article = session.execute(select(Articles).where(Articles.username == username, Articles.title == title)).scalars().first()

            if exist_article.title != title:
                exist_article.title = title
            if description != exist_article.description:
                exist_article.description = description

            if not exist_article:
                return {'Error': 'Article not found'}

            exist_article.title = title
            exist_article.description = description
            exist_article.updated_at = datetime.utcnow()

            session.commit()

    @staticmethod
    def delete_articles(username:str,title:str):
        with Session() as session:
            result = session.execute(delete(Articles).where(Articles.username == username, Articles.title == title))
            
            if not result:
                return {'Article': 'Not found'}
            
            session.commit()
    
    @staticmethod
    def ban_article(username:str,title:str):
        with Session() as session:
            exist_article = session.execute(select(Articles).where(Articles.username == username,Articles.title == title).join(Users).where(Users.is_admin == True)).scalars().first()

            if not exist_article:
                return {'Article': 'Not found'}
            
            stmt = update(Articles).where(Articles.username == username,Articles.title == title).values(have_banned=True)
            result = session.execute(stmt)
            session.commit()
            return result

    @staticmethod
    def unban_article(username:str,title:str):
        with Session() as session:
            exist_article = session.execute(select(Articles).where(Articles.username == username,Articles.title == title).join(Users).where(Users.is_admin == True)).scalars().first()

            if not exist_article:
                return {'Article': 'Not found'}
            
            stmt = update(Articles).where(Articles.username == username,Articles.title == title).values(have_banned=False)
            result = session.execute(stmt)
            session.commit()
            return result