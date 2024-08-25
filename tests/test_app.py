import pytest
from app import app
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_receive_data_success(client):
    response = client.post('/data', json={
        'date': datetime.now().timestamp(),
        'dados': 100
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Dados recebidos, armazenados e processados com sucesso"}

def test_receive_data_invalid_format(client):
    response = client.post('/data', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Formato de dados inválido"}

def test_receive_data_invalid_data_type(client):
    response = client.post('/data', json={
        'date': 'invalid_date',
        'dados': 'invalid_data'
    })
    assert response.status_code == 400
    assert response.get_json() == {"error": "Tipo de dados inválido"}
