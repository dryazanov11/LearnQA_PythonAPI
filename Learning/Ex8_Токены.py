import requests
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
answer = response.json()
print('Получен токен и время ожидания')

key1 = 'token'
key2 = 'seconds'
key3 = 'result'
key4 = 'status'

response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params = {"token": answer[key1]})
res = response1.json()

if res[key4] == 'Job is NOT ready':
    print('Задача в процессе')
    time.sleep(answer[key2])

response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params = {"token": answer[key1]})
result = response2.json()
if key3 in result and result[key4] == 'Job is ready':
    print('Задача успешно отработала')
else:
    print('Задача не отработала')