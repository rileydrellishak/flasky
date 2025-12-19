from flask import Blueprint, abort, make_response, request, Response
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from ..db import db
from .route_utilities import create_model, get_models_with_filters, update_model, validate_model

bp = Blueprint('bp', __name__, url_prefix='/caretakers')

@bp.get('')
def get_all_caretakers():
    return get_models_with_filters(Caretaker, request.args), 200

@bp.get('/<caretaker_id>')
def get_caretaker_by_id(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    return caretaker.to_dict(), 200

@bp.post('')
def create_caretaker():
    return create_model(Caretaker, request.get_json()), 201

@bp.delete('/<caretaker_id>')
def delete_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    db.session.delete(caretaker)
    db.session.commit()
    
    return Response(status=204, mimetype='applications/json')

@bp.post('/<caretaker_id>/cats')
def post_cat_id_to_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    caretaker.cats = []
    for id in request_body['cat_ids']:
        cat = validate_model(Cat, id)
        cat.caretaker_id = caretaker.id
    db.session.commit()
    response = {
        'id': caretaker_id,
        'cat_ids': [cat.id for cat in caretaker.cats]
    }
    return response, 200

@bp.get('/<caretaker_id>/cats')
def get_cats_for_specific_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    response = caretaker.to_dict()
    response['cats'] = [cat.to_dict() for cat in caretaker.cats]
    return response, 200

@bp.patch('/<caretaker_id>')
def update_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    return update_model(caretaker, request_body), 200