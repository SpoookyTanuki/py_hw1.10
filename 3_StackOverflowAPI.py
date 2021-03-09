import requests
from datetime import date, timedelta

today = date.today()
day_b4_yesterday = today - timedelta(days=2)

response = requests.get('https://api.stackexchange.com/2.2/questions',
                        params={'fromdate': day_b4_yesterday, 'todate': today,
                               'order': 'desc', 'sort': 'activity',
                               'tagged': 'python', 'site': 'stackoverflow'})

items = response.json()['items']

for question in items:
    print(question['title'], question['link'])