# 네이버 API를 이용한

# 영화 평점 및 이미지 검색



### 목표

네이버 오픈 API를 이용하여 PJT_01에서 구한 영화 목록을 바탕으로, 해당 영화들의  **평점**, **링크**, **영화코드**를 받아오고 **포스터**이미지의 url을 받아 images 폴더에 저장한다.



## 영화데이터를 csv파일로 만들기



### PJT_01 에서 영화목록 받아오기

```python
import csv

with open('../PJT_01/movie.csv' ~) as f:
    reader = csv.Dictreader(f)


```



PJT_01 폴더에 있는 영화목록 데이터를 가져온다.

가져온 영화데이터 중 필요한 영화제목, 영화코드를 movies 딕셔너리에 추가한다

```python
	movies = {}
    for row in reader:
        name = row['movieNm']
        movies[name] ={}
        movies[name]['movieNm'] = name
        movies[name]['movieCd'] = row['movieCd']
```

딕셔너리에 영화제목을 키값으로 하여 넣음으로써, 추후 영화제목의 중복이 생기면 덮어써짐으로써 같은 내용의 데이터가 없도록한다.

동명의 영화제목이 걱정될때는 movieCd, 즉 영화코드를 키값으로 저장하면 해결될 것이다.



### 가져온 데이터를 기반으로 네이버 API에서 평점, 포스터, 링크 가져오기

```python
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
```

한줄(한 영화에 대한 정보)에 적어넣을 정보를 딕셔너리 형태로 만들기위하여

읽어온 데이터의 키값을 검색어로 네이버 API에서 링크, 포스터, 평점을 가져와 딕셔너리에 넣는다.

```python
goal_keys = [ 'movieNm','movieCd', 'image', 'link', 'userRating']
with open('movie_naver.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames= goal_keys, extrasaction='ignore')
    writer.writerow(movie_infos)
```

한줄의 영화데이터를 movie_naver.csv 파일에 추가하여 적어넣고,

다음 영화데이터를 반복한다.



## 가져온 데이터를 기반으로 영화 포스터 저장하기

movie_image.py라는 이름으로 포스터를 저장할 파이썬 프로그램을 만든다.

```python
with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
```

위 구문을 사용하여 방금 작성한 영화 데이터를 불러온다.

```python
    for row in reader:
        time.sleep(0.1)
        image_url = row['image']
        movieCd = row['movieCd']
        with open(f'images/{movieCd}.jpg', 'wb') as f: #wb : write binary
            response = requests.get(image_url)
            f.write(response.content)
```

내부에서 for 구문을 사용하여 **모든 영화**데이터에 대하여 포스터 이미지의 url을 받아오고 이미지를 요청하여 jpg 형식 파일로 저장한다.



## 이슈

평범하게 코드를 작성하여 실행했을 경우 제한시간 초과 에러 이슈가 나타났다.

이는 네이버 API 에 너무 빠르게 정보를 요청해서 생기는 오류로 이는

```python
import time

#반복 요청 코드 내에서
time.sleep('시간'=0.1)
을 이용하여 딜레이 시켜줌으로 해결할 수 있었다.

```





