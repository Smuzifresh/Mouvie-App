from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Liked_Films (db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    film_id: Mapped[int] = mapped_column(Integer, nullable=False)
    title : Mapped[str] = mapped_column(String, unique=False, nullable=False)
    release_date :  Mapped[str] = mapped_column(String, unique=False, nullable=False)
    poster_path :  Mapped[str] = mapped_column(String, unique=False, nullable=False)
    vote_average : Mapped[str] = mapped_column(String, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))