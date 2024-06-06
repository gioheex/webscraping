import requests

answer = requests.get('https://www.uniceub.br/')

print(answer.status_code)

# print(answer.text)
print('HEADER:',  answer.headers)
print(answer.content)