from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic('Негативные тесты на PUT')
class TestEditNegative(BaseCase):
    @allure.description('Проверка логина без авторизации, с неподходящими авторизационными данными, неверным форматом почты и'
                       'с коротким именем')
    def test_edit_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1,'id')

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # LOGIN SECOND
        login_data_second = {
            'email': 'vinkotov@example.com',
            'password': 1234
        }
        response_second = MyRequests.post('/user/login', data=login_data_second)
        auth_sid_second = self.get_cookie(response_second, 'auth_sid')
        token_second = self.get_header(response_second, 'x-csrf-token')

        #EDIT WITHOUT AUTHORIZE
        new_name = 'New firstName'
        response3 = MyRequests.put(f'/user/{user_id}', data={'firstName': new_name})
        assert response3.content.decode('UTF-8') == 'Auth token not supplied', f'Unexpected response content {response3.content}'

        #EDIT WITH ANOTHER PARAMS
        response4 = MyRequests.put(f'/user/{user_id}',
                                 headers={'x-csrf-token': token_second},
                                 cookies={'auth_sid': auth_sid_second},
                                 data={'firstName': new_name}
                                 )
        Assertions.assert_code_status(response4, 400)

        #EDIT EMAIL WITHOUT DOG
        response5 = MyRequests.put(f'/user/{user_id}',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid},
                                 data={'email': 'new_emailexample.com'}
                                 )
        assert response5.content.decode('UTF-8') == 'Invalid email format', f'Unexpected response content {response5.content}'

        # EDIT WITH SHORT FIRSTNAME
        response6 = MyRequests.put(f'/user/{user_id}',
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid},
                                   data={'firstName': 'l'}
                                   )
        assert response6.content.decode(
            'UTF-8') == '{"error":"Too short value for field firstName"}', f'Unexpected response content {response6.content}'


