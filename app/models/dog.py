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

    @classmethod
    def from_dict(cls, dog_data):
        new_dog = Dog(
            name=dog_data['name'],
            breed=dog_data['breed'],
            personality=dog_data['personality'],
            caretaker_id=dog_data.get('caretaker_id', None),
            caretaker=dog_data.get('caretaker', None)
            )
        
        return new_dog

    def to_dict(self):
        dog_dict = {}
        dog_dict['id'] = self.id
        dog_dict['name'] = self.name
        dog_dict['personality'] = self.personality
        dog_dict['breed'] = self.breed
        
        if self.caretaker_id is not None:
            dog_dict["caretaker_id"] = self.caretaker_id
            dog_dict["caretaker"] = self.caretaker.name if self.caretaker else None

        return dog_dict