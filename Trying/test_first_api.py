import requests
import pytest

class TestFirstAPI:
    names =[
        ('Vitalii'),
        ('Arseniy'),
        ('')
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name': name}
        response = requests.get(url, params=data)
        assert response.status_code == 200, "Неверный код ответа"

        response_dict = response.json()
        assert "answer" in response_dict, "В ответе нет поля 'answer'"

        if name == '':
            expected_response_text = f'Hello, someone'
        else:
            expected_response_text = f'Hello, {name}'
        actual_response_text = response_dict['answer']
        assert expected_response_text == actual_response_text, 'Полученный ответ не корректен'