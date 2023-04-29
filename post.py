import requests

url = 'http://127.0.0.1:5000/gpt4free'
question = 'Me cite 3 frases de John Locke em português'
payload = {'question': question}
response = requests.post(url, json=payload)
if response.ok:
    answer = response.json()['answer']
    escaped = answer.encode('utf-8').decode('unicode-escape')
    print(escaped)
else:
    print(response.json()['error'])
