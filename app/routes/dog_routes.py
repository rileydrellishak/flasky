from flask import Blueprint, abort, make_response, request, Response
from app.models.dog import Dog
from ..db import db
from .route_utilities import create_model, get_models_with_filters, update_model, validate_model

bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@bp.post('')
def create_dog():
    request_body = request.get_json()
    return create_model(Dog, request_body)

@bp.get('')
def get_all_dogs():
    return get_models_with_filters(Dog, request.args), 200

@bp.get('/<dog_id>')
def get_one_dog_by_id(dog_id):
    dog = validate_model(Dog, dog_id)
    return dog.to_dict(), 200

@bp.delete('/<dog_id>')
def delete_dog(dog_id):
    dog = validate_model(Dog, dog_id)
    db.session.delete(dog)
    db.session.commit()
    
    return Response(status=204, mimetype='applications/json')

@bp.patch('/<dog_id>')
def update_dog(dog_id):
    dog = validate_model(Dog, dog_id)
    return update_model(dog, request.get_json())