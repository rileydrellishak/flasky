from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Caretaker(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    cats: Mapped[list['Cat']] = relationship("Cat", back_populates='caretaker')
    dogs: Mapped[list['Dog']] = relationship('Dog', back_populates='caretaker')