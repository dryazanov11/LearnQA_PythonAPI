import time
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):
    def test_delete_base_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': 1234
        }
        #LOGIN
        response = MyRequests.post('/user/login', data=data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        #DELETE BASE USER
        response1 = MyRequests.delete('/user/2',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})

        assert response1.content.decode('UTF-8') == 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.', \
            f'Unexpected response content {response1.content}'

    def test_delete_new_user(self):
        #REGISTER AND LOGIN NEW USER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        #SUCCESS DELETING
        response3 = MyRequests.delete(f'/user/{user_id}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid})
        Assertions.assert_code_status(response3, 200)

        #CHECK USER
        response4 = MyRequests.get(f'/user/{user_id}',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})
        assert response4.content.decode('UTF-8') == 'User not found', f'Unexpected response content {response4.content}'

    def test_delete_from_another_user(self):
        # REGISTER AND LOGIN FIRST USER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, 'id')

        email = register_data['email']
        password = register_data['password']

        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # REGISTER SECOND USER
        time.sleep(1)
        register_data1 = self.prepare_registration_data()
        response_1 = MyRequests.post('/user/', data=register_data1)
        Assertions.assert_code_status(response_1, 200)
        Assertions.assert_json_has_key(response_1, 'id')

        user_id1 = self.get_json_value(response_1, 'id')

        response_final = MyRequests.delete(f'/user/{user_id1}',
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid})
        print(response_final.status_code)