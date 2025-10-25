from flask import Blueprint, abort, make_response, request, Response
from app.models.dog import Dog
from ..db import db

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.post('')
def create_dog():
    request_body = request.get_json()

    name = request_body['name']
    breed = request_body['breed']
    personality = request_body['personality']

    new_dog = Dog(name=name, breed=breed, personality=personality)
    db.session.add(new_dog)
    db.session.commit()

    response = {
        'id': new_dog.id,
        'name': new_dog.name,
        'breed': new_dog.breed,
        'personality': new_dog.personality
    }

    return response, 201

@dogs_bp.get('')
def get_all_dogs():
    query = db.select(Dog).order_by(Dog.id)
    dogs = db.session.scalars(query)
    dogs_response = []
    for dog in dogs:
        dogs_response.append(dict(id=dog.id, name=dog.name, breed=dog.breed, personality=dog.personality))

    return dogs_response