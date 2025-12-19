from flask import Blueprint, abort, make_response, request, Response
from app.models.caretaker import Caretaker
from ..db import db
from .route_utilities import create_model, validate_model

bp = Blueprint('bp', __name__, url_prefix='/caretakers')

@bp.get('')
def get_all_caretakers():
    query = db.select(Caretaker).order_by(Caretaker.id)
    caretakers = db.session.scalars(query)

    return [caretaker.to_dict() for caretaker in caretakers], 200

@bp.get('/<caretaker_id>')
def get_caretaker_by_id(caretaker_id):
    caretaker = validate_model(caretaker_id)
    return caretaker.to_dict()

@bp.post('')
def create_caretaker():
    return create_model(Caretaker, request.get_json())