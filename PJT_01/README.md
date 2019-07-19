오픈 API 이용 영화정보따오기**

## 목표

- 영화평점서비스(예- watcha)을 만들기 위한 데이터 수집 단계로, 영화 데이터베이스 구축을 위한 csv 파일을 만든다.

## 과정

1. 최근 50주간 데이터 중에 주간 박스오피스 TOP10데이터를 수집한다.
   - 주간(월~일)까지 기간의 데이터를 조회합니다.
   - 조회 기간은 총 50주이며, 기준일(마지막 일자)은 2019년 7월 13일입니다.

![](\pjt1\Q1answer2.png)

| 코드     | 내용     | 코드     | 내용     | 코드     |    내용    |
| -------- | -------- | -------- | -------- | -------- | :--------: |
| movie Cd | 영화코드 | movie Nm | 영화이름 | Audi Acc | 누적관계수 |



2. 위에서 수집한 영화 대표코드를 활용하여 상세 정보를 수집합니다.

   - 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 관람등급 , 개봉연도 , 상영시간 , 장르 , 감독명 을 포함한다.

   - 배우 정보, 배급사 정보 등을 추가적으로 수집한다.

     

     ![](C:\Users\student\Desktop\Q2answer.PNG)

     

     

     | 코드          | 내용     | 코드        | 내용     | 코드        | 내용     |
     | ------------- | -------- | ----------- | -------- | ----------- | -------- |
     | Movie Cd      | 영화코드 | Movie Nm    | 영화제목 | Movie Nm en | 영문제목 |
     | Movie Name Or | 원제목   | Watch Garde | 관람등급 | Open Dt     | 상영날짜 |
     | Show Tm       | 런닝타임 | Genre Nm    | 장르     | Director    | 감독     |
     | Actor         | 배우     | Company     | 배급사   |             |          |

     

3. 위에서 수집한 영화 감독정보를 활용하여 상세 정보를 수집합니다.

   - 영화인명 으로 조회한다.
   - 영화인 코드 , 영화인명 , 분야 , 필모리스트를 포함한다.

   ![](C:\Users\student\Desktop\Q3answer.PNG)

| 코드        | 내용     | 코드        | 내용       |
| ----------- | -------- | ----------- | ---------- |
| People Cd   | 영화코드 | People Nm   | 감독이름   |
| Rep Role Nm | 역할     | Filmo Names | 필모리스트 |



## 방법

1. API KEY를 환경변수로 지정하기 위하여

   ```python
   from decouple import config
   
   key = config('API_KEY')
   ```

   를 통하여 .env 파일에 key를 저장하고 불러온다.

   .gitignore에 .env를 작성하여 올라가지 않도록 한다.

2. Requests를 이용하여 요청하고 받아오기

```python
import requests
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
targetDt = datetime(2019, 7, 13) - timedelta(weeks = weeks_ago)
targetDt = targetDt.strftime('%Y%m%d')
api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0'
response = requests.get(api_url)
data = response.json()['boxOfficeResult']['weeklyBoxOfficeList']
```

3. Csv를 이용하여 csv파일 작성하기

```python
import csv
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    goal_keys = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames= goal_keys, extrasaction='ignore')
    writer.writeheader()
    for movie in movie_infos:
        writer.writerow(movie_infos[movie])
```

