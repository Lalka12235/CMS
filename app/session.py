from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

Session = sessionmaker(engine)