from flask import Blueprint, abort, make_response, request, Response
from app.models.dog import Dog
from ..db import db
from .route_utilities import create_model, validate_model

bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@bp.post('')
def create_dog():
    request_body = request.get_json()

    new_dog = Dog.from_dict(request_body)
    db.session.add(new_dog)
    db.session.commit()

    return new_dog.to_dict(), 201

@bp.get('')
def get_all_dogs():
    query = db.select(Dog).order_by(Dog.id)

    name_param = request.args.get('name')
    if name_param:
        query = query.where(Dog.name == name_param)

    breed_param = request.args.get('breed')
    if breed_param:
        query = query.where(Dog.breed.ilike(f"%{breed_param}%"))

    personality_param = request.args.get('personality')
    if personality_param:
        query = query.where(Dog.personality.ilike(f"%{personality_param}%"))

    dogs = db.session.scalars(query)
    dogs_response = []
    for dog in dogs:
        dogs_response.append(dog.to_dict())

    return dogs_response

@bp.get('/<dog_id>')
def get_one_dog_by_id(dog_id):
    dog = validate_model(Dog, dog_id)
    return dog.to_dict(), 200