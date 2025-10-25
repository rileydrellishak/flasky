from flask import Blueprint, abort, make_response, request, Response
from app.models.cat import Cat
from ..db import db

cats_bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@cats_bp.post('')
def create_cat():
    request_body = request.get_json()

    name = request_body['name']
    color = request_body['color']
    personality = request_body['personality']

    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    response = {
        'id': new_cat.id,
        'name': new_cat.name,
        'color': new_cat.color,
        'personality': new_cat.personality
    }

    return response, 201

@cats_bp.get('')
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)
    cats_response = []
    for cat in cats:
        cats_response.append(dict(id=cat.id, name=cat.name, color=cat.color, personality=cat.personality))
    return cats_response

@cats_bp.get('/<cat_id>')
def get_one_cat(cat_id):
    cat = validate_cat(cat_id)

    return dict(id=cat.id, name=cat.name, color=cat.color, personality=cat.personality)

def validate_cat(id):
    '''
    Checks if a cat with a given id exists. If id is incorrect type, returns 400 bad request error. If id does not exist in cats (list), returns 404 not found. If cat id found, returns the instance of cat.
    '''
    try:
        cat_id = int(id)
    except:
        response = {'message': f'cat {id} invalid'}
        abort(make_response(response, 400))
    
    query = db.select(Cat).where(Cat.id == cat_id)
    cat = db.session.scalar(query)

    if not cat:
        response = {'message': f'cat {cat_id} does not exist'}
        abort(make_response(response, 404))
    
    return cat

@cats_bp.put('/<cat_id>')
def update_cat(cat_id):
    cat = validate_cat(cat_id)
    request_body = request.get_json()

    cat.name = request_body['name']
    cat.color = request_body['color']
    cat.personality = request_body['personality']
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@cats_bp.delete('/<cat_id>')
def delete_cat(cat_id):
    cat = validate_cat(cat_id)
    db.session.delete(cat)
    db.session.commit()
    
    return Response(status=204, mimetype='applications/json')