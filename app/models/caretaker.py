from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Caretaker(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    cats: Mapped[list['Cat']] = relationship("Cat", back_populates='caretaker')
    dogs: Mapped[list['Dog']] = relationship('Dog', back_populates='caretaker')

    @classmethod
    def from_dict(cls, caretaker_data):
        new_caretaker = Caretaker(
            name=caretaker_data['name'],
            cats=caretaker_data.get('cats', []),
            dogs=caretaker_data.get('dogs', [])
            )
        
        return new_caretaker

    def to_dict(self):
        caretaker_dict = {}
        caretaker_dict['id'] = self.id
        caretaker_dict['name'] = self.name
        
        if self.cats is not None:
            caretaker_dict["cats"] = [cat.to_dict() for cat in self.cats]
        
        if self.dogs is not None:
            caretaker_dict['dogs'] = [dog.to_dict() for dog in self.dogs]

        return caretaker_dict