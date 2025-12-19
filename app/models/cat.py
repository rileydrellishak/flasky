from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey('caretaker.id'))
    caretaker: Mapped[Optional['Caretaker']] = relationship(back_populates='cats')

    @classmethod
    def from_dict(cls):
        pass