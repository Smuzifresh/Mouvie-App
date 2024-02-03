from flask_login import UserMixin
from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User( UserMixin,db.Model):
    from .liked_films import Liked_Films
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    avatar: Mapped[str] = mapped_column(String, unique=False, default="/static/media/default.png")
    liked_films = db.relationship('Liked_Films', backref='user', lazy = True)


    def __repr__(self):
       return self.firstname