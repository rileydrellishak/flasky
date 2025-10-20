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
    try:
        cat_id = int(id)
    except:
        return {'message': f'cat {id} invalid'}, 400
    for cat in cats:
        if cat.id == cat_id:
            return dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality
        )
    return {'message': f'cat {cat_id} does not exist'}, 404

def validate_cat_id(id):

