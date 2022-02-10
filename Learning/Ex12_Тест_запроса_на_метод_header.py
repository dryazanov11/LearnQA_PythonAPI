import requests

def test_secret_header():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')
    secret_header = response.headers.get('x-secret-homework-header')
    assert secret_header == 'Some secret value', "Header 'x-secret-homework-header' is not equal to expected value"