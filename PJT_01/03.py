import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

key = config('API_KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?'
movieperson_infos = {}
find_keys = []
goal_keys = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames']

with open('director.csv', 'w', encoding='utf-8', newline='') as g:
    writer = csv.DictWriter(g, fieldnames= goal_keys, extrasaction='ignore')
    writer.writeheader()

with open('movie.csv', 'r', encoding='utf-8', newline = '') as f:
    
    reader = csv.DictReader(f)

    for row in reader:

        director_name = row['director']
        movie_name = row['movieNm']
        api_url = f'{base_url}key={key}&&peopleNm={director_name}'
        response = requests.get(api_url)
        
        data = response.json()['peopleListResult']
        people_number = int(data['totCnt'])

        for count in range(len(data['peopleList'])):
            if movie_name in data['peopleList'][count]['filmoNames'] and data['peopleList'][count]['repRoleNm'] == '감독':
                with open('director.csv', 'a', encoding='utf-8', newline='') as g:
                    writer = csv.DictWriter(g, fieldnames= goal_keys, extrasaction='ignore')
                    writer.writerow(data['peopleList'][count])
                    break
