import requests
import pytest
import allure

data = [
    'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
    'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
]

@allure.epic('Check user agent')
@allure.description('Check user agent in response with true data')
@pytest.mark.parametrize('user_agent', data)
def test_user_agent(user_agent):
    response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check', headers={"User-Agent": user_agent})
    a, b, c = response.json()['platform'], response.json()['browser'], response.json()['device']
    if user_agent == data[0]:
        assert a == 'Mobile' and b == 'No' and c == 'Android', 'Значения в первом User-Agent не верны'
    if user_agent == data[1]:
        assert a == 'Mobile' and b == 'Chrome' and c == 'iOS', 'Значения во втором User-Agent не верны'
    if user_agent == data[2]:
        assert a == 'Googlebot' and b == 'Unknown' and c == 'Unknown', 'Значения в третьем User-Agent не верны'
    if user_agent == data[3]:
        assert a == 'Web' and b == 'Chrome' and c == 'No', 'Значения в четвертом User-Agent не верны'
    if user_agent == data[4]:
        assert a == 'Mobile' and b == 'No' and c == 'iPhone', 'Значения в пятом User-Agent не верны'
