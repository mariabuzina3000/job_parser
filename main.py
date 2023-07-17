import requests


params = {
    'text': 'повар'
}

data = requests.get('https://api.hh.ru/vacancies', params=params).json()

print(data)