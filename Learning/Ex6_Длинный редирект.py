import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')
history = response.history
final_url = response.url
print(f'Количество редиректов: {len(history)}, а итоговый URL: {final_url}')