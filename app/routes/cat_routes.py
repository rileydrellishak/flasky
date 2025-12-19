from flask import Blueprint, abort, make_response, request, Response
from app.models.cat import Cat
from ..db import db
from .route_utilities import create_model, get_models_with_filters, update_model, validate_model

bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@bp.post('')
def create_cat():
    request_body = request.get_json()
    return create_model(Cat, request_body), 201

@bp.get('')
def get_all_cats():
    return get_models_with_filters(Cat, request.args), 200

@bp.get('/<id>')
def get_one_cat(id):
    cat = validate_model(Cat, id)
    return cat.to_dict(), 200

@bp.put('/<id>')
def replace_cat(id):
    cat = validate_model(Cat, id)
    request_body = request.get_json()

    cat.name = request_body['name']
    cat.color = request_body['color']
    cat.personality = request_body['personality']
    cat.caretaker_id = request_body['caretaker_id']
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@bp.patch('/id')
def update_cat(id):
    cat = validate_model(Cat, id)
    request_body = request.get_json()
    return update_model(cat, request_body), 200

@bp.delete('/<id>')
def delete_cat(id):
    cat = validate_model(Cat, id)
    db.session.delete(cat)
    db.session.commit()
    
    return Response(status=204, mimetype='applications/json')