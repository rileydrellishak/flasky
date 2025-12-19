from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Dog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    breed: Mapped[str]
    personality: Mapped[str]
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey('caretaker.id'))
    caretaker: Mapped[Optional['Caretaker']] = relationship(back_populates='dogs')