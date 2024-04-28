import requests
token = '6526048505:AAEbiU1bGv63IDjLpSGfoKtGbHIXeyMVBbE'
main_url = f'https://api.telegram.org/bot{token}'
url = f'{main_url}/getUpdates'
result = requests.get(url)
print(result.json())

messages = result.json()['result']
for messages in messages:
    chat_id = messages['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Привет, дорогой пользователь'
    }
    result = requests.post(url,params=params)

