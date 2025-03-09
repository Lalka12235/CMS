from sqlalchemy import create_engine,insert,delete,update,select
from sqlalchemy.orm import sessionmaker
from app.data.orm_model import Base, Users,Articles
from app.data.article_model import Article,User
from app.config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

Session = sessionmaker(engine)


def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def register_user(username):
    with Session() as session:
        exist_user = session.execute(select(Users).where(Users.username == username)).scalars().first()

        if exist_user:
            return {'Create user': 'User already exists'}
        
        result = session.execute(insert(Users).values(username=username,is_admin=False))
        session.commit()
        return result
    
def create_articles(username,article: Article):
    with Session() as session:
        pass

def delete_articles(username):
    with Session() as session:
        result = session.execute(delete(Articles).where(Articles.username == username))
        session.commit()
        return result
    

def update_article(username):
    pass

def make_admin(username):
    with Session() as session:
        stmt = update(Users).where(Users.username == username).values(is_admin=True)
        session.execute(stmt)
        session.commit()


def deprivation_of_admin(username):
    with Session() as session:
        stmt = update(Users).where(Users.username == username).values(is_admin=False)
        session.execute(stmt)
        session.commit()