def test_get_all_cats_empty_table(client):
    response = client.get('/cats')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_cats_with_records(client, two_cats):
    response = client.get('/cats')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [dict(name='George', color='Gray', personality='Neutral', id=1), dict(name='Butters', color='White', personality='Playful', id=2)]

def test_get_one_cat_by_id_success(client, two_cats):
    response = client.get('/cats/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == dict(name='George', color='Gray', personality='Neutral', id=1)

def test_get_one_cat_by_id_404(client, two_cats):
    response = client.get('/cats/3')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': f'Cat 3 does not exist'}

def test_get_one_cat_by_id_400(client, two_cats):
    response = client.get('/cats/hi')
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {'message': f'Cat hi invalid'}

def test_create_one_cat_success(client):
    response = client.post('/cats', json={'name':'Butters', 'color':'White', 'personality':'Playful'})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {'name':'Butters', 'color':'White', 'personality':'Playful', 'id':1}

def test_create_one_cat_extra_keys(client):
    pass

def test_create_one_cat_missing_keys(client):
    pass