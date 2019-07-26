import requests
import csv
import time
from pprint import pprint

BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
CLIENT_ID = '0qeJm2fQEbgDssgoCfJK'
CLIENT_SECRET = 'BAyRdED3tU'
HEADERS = {
    'X-Naver-Client-Id' : CLIENT_ID,
    'X-Naver-Client-Secret' : CLIENT_SECRET,
}

with open('../PJT_01/movie.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f) 
    movies = {}
    for row in reader:
        name = row['movieNm']
        movies[name] = {}
        movies[name]['movieCd'] = row['movieCd']
        movies[name]['movieNm'] = row['movieNm']


goal_keys = [ 'movieNm','movieCd', 'image', 'link', 'userRating']

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames= goal_keys, extrasaction='ignore')
    writer.writeheader()


for key in movies:
    time.sleep(0.1)
    query = key
    API_URL = f'{BASE_URL}?query={query}'
    response = requests.get(API_URL, headers=HEADERS).json() #헤더를 보내야한다.
    movie_infos = {
        'movieNm' : key,
        'movieCd' : movies[key]['movieCd'],
        }
   
    movie_infos['userRating'] = response['items'][0]['userRating']
    movie_infos['image'] = response['items'][0]['image']
    movie_infos['link'] = response['items'][0]['link']
    
    with open('movie_naver.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames= goal_keys, extrasaction='ignore')
        writer.writerow(movie_infos)
