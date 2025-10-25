from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Dog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    breed: Mapped[str]
    personality: Mapped[str]