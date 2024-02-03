from datetime import datetime
from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Comment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='comment', lazy = True)
    message: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    film_id : Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    def __repr__(self) -> str:
       return f"Comment:{self.id}, user_id:{self.user_id}, message:{self.message}, date:{self.date}, film_id:{self.film_id}"