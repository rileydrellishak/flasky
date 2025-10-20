from flask import Blueprint, abort, make_response
from app.models.cat import cats

cats_bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@cats_bp.get('')
def get_all_cats():
    result = []
    for cat in cats:
        result.append(dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality
        ))
    return result

@cats_bp.get('/<id>')
def get_cat_by_id(id):
    cat = validate_cat_id(id)
    return dict(
        id=cat.id,
        name=cat.name,
        color=cat.color,
        personality=cat.personality
    )

def validate_cat_id(id):
    '''
    Checks if a cat with a given id exists. If id is incorrect type, returns 400 bad request error. If id does not exist in cats (list), returns 404 not found. If cat id found, returns the instance of cat.
    '''
    try:
        cat_id = int(id)
    except:
        response = {'message': f'cat {id} invalid'}
        abort(make_response(response, 400))
    
    for cat in cats:
        if cat.id == cat_id:
            return cat

    response = {'message': f'cat {cat_id} does not exist'}
    abort(make_response(response, 404))