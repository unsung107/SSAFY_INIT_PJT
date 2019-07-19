import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

key = config('API_KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
movie_names = []
movie_infos = dict()
for weeks_ago in range(50,-1,-1):

    targetDt = datetime(2019, 7, 13) - timedelta(weeks = weeks_ago)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0'

    response = requests.get(api_url)
    data = response.json()['boxOfficeResult']['weeklyBoxOfficeList']

    for i in range(10):
        movie_infos[data[i]['movieNm']] = data[i]

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    goal_keys = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames= goal_keys, extrasaction='ignore')
    writer.writeheader()
    for movie in movie_infos:
        writer.writerow(movie_infos[movie])
    
