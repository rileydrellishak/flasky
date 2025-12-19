from flask import abort, make_response
from ..db import db

def validate_model(model, id):
    '''
    Checks if a cat with a given id exists. If id is incorrect type, returns 400 bad request error. If id does not exist in cats (list), returns 404 not found. If cat id found, returns the instance of cat.
    '''
    try:
        id = int(id)
    except:
        response = {'message': f'{model.__name__} {id} invalid'}
        abort(make_response(response, 400))
    
    query = db.select(model).where(model.id == id)
    result = db.session.scalar(query)

    if not result:
        response = {'message': f'{model.__name__} {id} does not exist'}
        abort(make_response(response, 404))
    
    return result