import requests
from json.decoder import JSONDecodeError

response = requests.get('https://playground.learnqa.ru/api/hello', params={"name": "User"})
parsed_response_text = response.json()
print(parsed_response_text["answer"])


# response = requests.get('https://playground.learnqa.ru/api/get_text')
# print(response.text)
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print('Не удалось распарсить JSON')

# response = requests.get('https://playground.learnqa.ru/api/check_type')
# print(response.text)

# headers = {"some_header": "123"}
# response = requests.get('https://playground.learnqa.ru/api/show_all_headers', headers=headers)
# print(response.headers)

# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
# cookie_value = response1.cookies.get('auth_cookie')
# cookies = {}
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
# response2 = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookies)
# print(response2.text)