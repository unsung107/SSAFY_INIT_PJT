import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

key = config('API_KEY')
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
movie_infos = {}
find_keys = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm']
goal_keys = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'director', 'actor', 'company']

with open('movie.csv', 'w', encoding='utf-8', newline='') as g:
    writer = csv.DictWriter(g, fieldnames= goal_keys, extrasaction='ignore')
    writer.writeheader()


with open('boxoffice.csv', 'r', encoding='utf-8', newline = '') as f:
    
    reader = csv.DictReader(f)

    for row in reader:

        movieCd = row['movieCd']
        api_url = f'{base_url}?key={key}&movieCd={movieCd}&weekGb=0'
        response = requests.get(api_url)
        data = response.json()['movieInfoResult']['movieInfo']
        for keys in find_keys:
            try: 
                if keys in data:
                    movie_infos[keys] = data[keys]
                elif keys in data['audits'][0]:
                    movie_infos[keys] = data['audits'][0][keys]
                elif keys in data['genres'][0]:
                    movie_infos[keys] = data['genres'][0][keys]
                elif keys in data['directors'][0]:
                    movie_infos['director'] = data['directors'][0]['peopleNm']
                else:
                    movie_infos[keys] = ' '
            except:
                a = 0

        try:
            movie_infos['actor'] = data['actors'][0]['peopleNm']
            movie_infos['company'] = data['companys'][0]['companyNm']
        except:
            a = 0

        with open('movie.csv', 'a', encoding='utf-8', newline='') as g:
            writer = csv.DictWriter(g, fieldnames= goal_keys, extrasaction='ignore')
            writer.writerow(movie_infos)