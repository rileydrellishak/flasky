from flask import Blueprint, abort, make_response, request, Response
from app.models.caretaker import Caretaker
from ..db import db

bp = Blueprint('bp', __name__, url_prefix='/caretakers')

@bp.get('')
def get_all_caretakers():
    query = db.select(Caretaker)

@bp.post('')
def create_caretaker():
    pass