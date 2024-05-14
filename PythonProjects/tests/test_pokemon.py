import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ddcd4ace199e70061ccf0ae7a7223754'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4078'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Тетя Зина'

@pytest.mark.parametrize('key, value', [('name','Тетя Зина'), ('trainer_id', TRAINER_ID), ('id','26229')])
def test_parametrize(key, value):
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response_parametrize.json()["data"][0][key] == value

# Статус 200 по тренеру
def test_status_code_tainers():
    response = requests.get(f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})       

# Cтрочка с именем твоего тренера
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Sergey'   


@pytest.mark.parametrize('key, value', [('trainer_name', 'Sergey') , ('level', '1'), ('city','Samara')])

def test_parametrize(key, value):
     response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
     assert response_parametrize.json()["data"][0][key] == value
