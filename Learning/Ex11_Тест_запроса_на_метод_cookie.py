import requests

def test_cookie():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
    cookie_in_answer = dict(response.cookies)
    assert cookie_in_answer == {'HomeWork': 'hw_value'}, 'Cookie is not equal to expected value'