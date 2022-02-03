import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And ' \
            'this is a second message","timestamp":"2021-06-04 16:41:01"}]} '
data = json.loads(json_text)
message = data['messages'][1]['message']
print(f'Текст второго сообщения: {message}')