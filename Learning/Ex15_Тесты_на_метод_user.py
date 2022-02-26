from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest
import allure

@allure.epic('Check create user method')
class TestMethodUser(BaseCase):
    params = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]
    @allure.description('Check email format')
    def test_create_user_without_dog(self):
        email = 'testexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'UTF-8') == 'Invalid email format', f'Unexpected response content {response.content}'

    @pytest.mark.parametrize('value', params)
    @allure.description('Check without any value')
    def test_create_user_without_any_value(self, value):
        email = 'emailjustfortest_ryaz@example.com'
        if value == 'password':
            response = MyRequests.post('/user/', data={
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
            })
        elif value == 'username':
            response = MyRequests.post('/user/', data={
            "password": 123,
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
            })
        elif value == 'firstName':
            response = MyRequests.post('/user/', data={
            "username": "learnqa",
            "password": 123,
            "lastName": "learnqa",
            "email": email
            })
        elif value == 'lastName':
            response = MyRequests.post('/user/', data={
            "username": "learnqa",
            "password": 123,
            "firstName": "learnqa",
            "email": email
            })
        elif value == 'email':
            response = MyRequests.post('/user/', data={
                "username": "learnqa",
                "password": 123,
                "firstName": "learnqa",
                "lastName": "learnqa"
            })

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
                'UTF-8') == f"The following required params are missed: {value}", \
                f'Unexpected response content {response.content}'

    @allure.description('Check short firstName')
    def test_short_firstname(self):
        email = 'emailjustfortest_ryaz@example.com'
        response = MyRequests.post('/user/', data={
            "password": 123,
            "username": "learnqa",
            "firstName": "l",
            "lastName": "learnqa",
            "email": email
        })
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
                     'UTF-8') == f"The value of 'firstName' field is too short", \
                     f'Unexpected response content {response.content}'

    @allure.description('Check long firstName')
    def test_long_firstname(self):
        email = 'emailjustfortest_ryaz@example.com'
        response = MyRequests.post('/user/', data={
            "password": 123,
            "username": "learnqa",
            "firstName": "lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",
            "lastName": "learnqa",
            "email": email
        })
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
                     'UTF-8') == f"The value of 'firstName' field is too long", \
                     f'Unexpected response content {response.content}'