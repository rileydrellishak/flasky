from flask import Blueprint, abort, make_response, request, Response
from app.models.cat import Cat
from ..db import db
from .route_utilities import validate_model

bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@bp.post('')
def create_cat():
    request_body = request.get_json()

    new_cat = Cat.from_dict(request_body)
    db.session.add(new_cat)
    db.session.commit()

    return new_cat.to_dict(), 201

@bp.get('')
def get_all_cats():
    query = db.select(Cat)

    name_param = request.args.get('name')
    if name_param:
        query = query.where(Cat.name == name_param)

    color_param = request.args.get('color')
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%"))
    
    personality_param = request.args.get('personality')
    if personality_param:
        query = query.where(Cat.personality.ilike(f"%{personality_param}%"))

    query = query.order_by(Cat.id)
    cats = db.session.scalars(query)
    cats_response = []
    for cat in cats:
        cats_response.append(cat.to_dict())
    return cats_response

@bp.get('/<id>')
def get_one_cat(id):
    cat = validate_model(Cat, id)

    return cat.to_dict()

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

@bp.delete('/<id>')
def delete_cat(id):
    cat = validate_model(Cat, id)
    db.session.delete(cat)
    db.session.commit()
    
    return Response(status=204, mimetype='applications/json')