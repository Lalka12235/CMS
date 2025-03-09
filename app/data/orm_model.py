from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,DateTime,text
import datetime



class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    is_admin: Mapped[bool | None]

    articles: Mapped[list['Articles']] = relationship(back_populates='users')


class Articles(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    username: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    created_at: Mapped[DateTime]  = mapped_column(DateTime,server_default=text("TIMEZONE('utc',now())"),nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime,server_default=text("TIMEZONE('utc',now())"),onupdate=datetime.datetime.utcnow,nullable=False)
    
    
    users: Mapped[list['Users']] = relationship(back_populates='articles')