import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
methods = ['GET', 'POST', 'PUT', 'DELETE']

response1 = requests.get(url)
print(f'HTTP-запрос без параметра method приводит к ошибке: {response1.text}')

response2 = requests.head(url)
print(f'HTTP-запрос не из списка прикодит к {response2.status_code} статус коду')

response3 = requests.post(url, params={"method": "POST"})
print(f'Запрос с правильным значением method приводит к {response3.text}')

print('Проверка GET')
for i in methods:
    if i == 'GET':
        response = requests.get(url, params={"method": i})
        print(response.text)
        continue
    response = requests.get(url, data = {"method": i})
    print(response.text)

print('Проверка POST')
for i in methods:
    if i == 'GET':
        response = requests.post(url, params={"method": i})
        print(response.text)
        continue
    response = requests.post(url, data = {"method": i})
    print(response.text)

print('Проверка PUT')
for i in methods:
    if i == 'GET':
        response = requests.put(url, params={"method": i})
        print(response.text)
        continue
    response = requests.put(url, data = {"method": i})
    print(response.text)

print('Проверка DELETE')
for i in methods:
    if i == 'GET':
        response = requests.delete(url, params={"method": i})
        print(response.text)
        continue
    response = requests.delete(url, data = {"method": i})
    print(response.text)