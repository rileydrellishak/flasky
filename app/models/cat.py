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
    def from_dict(cls, cat_data):
        new_cat = Cat(
            name=cat_data['name'],
            color=cat_data['color'],
            personality=cat_data['personality'],
            caretaker_id=cat_data.get('caretaker_id', None),
            caretaker=cat_data.get('caretaker', None)
            )
        
        return new_cat

    def to_dict(self):
        cat_dict = {}
        cat_dict['id'] = self.id
        cat_dict['name'] = self.name
        cat_dict['personality'] = self.personality
        cat_dict['color'] = self.color
        
        if self.caretaker_id is not None:
            cat_dict["caretaker_id"] = self.caretaker_id
            cat_dict["caretaker"] = self.caretaker.name if self.caretaker else None

        return cat_dict