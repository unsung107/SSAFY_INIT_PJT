import requests
import csv
import time
from pprint import pprint

with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        time.sleep(0.1)
        image_url = row['image']
        movieCd = row['movieCd']
        with open(f'images/{movieCd}.jpg', 'wb') as f: #wb : write binary
            response = requests.get(image_url) #파일을 응답받음 파일을 바이너리 타입으로 받을거
            f.write(response.content)