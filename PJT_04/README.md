# HTML/CSS/BOOTSTRAP 를 이용한 반응형 웹만들기



## 1. 목표

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 웹 페이지 꾸미기
- Bootstrap을 활용한 HTML/CSS, JS 라이브러리 활용
- 영화 추천 사이트 반응형 레이아웃 구성



## 2. 요구사항

1. 영화 추천 사이트 메인페이지 기초 레이아웃 구성

![](images\전체 - xl.PNG)



sticky navigation bar 아 sticky footer bar header container 로 구성된 레이아웃을 작성한다.

2. 영화추천 사이트를 위한 영화 리스트 구성

![](images\전체 - lg.PNG)



![전체 - md](images\전체 - md.PNG)





![전체 - sm](images\전체 - sm.PNG)



![전체 - xl](images\전체 - xl.PNG)

위 그림과같이 디스플레이 크기에 따라 영화 목록의 가로줄의 개수가 달라지 도록 구성한다.

위를 위하여 Bootstrap의 grid 시스템을 사용하였는데 그 방식은 다음과 같다.

```html
<div class="row">
      <div class="b-blcok col-xl-3 col-lg-4 col-md-6 col-12">
```



3. 영화 상세 보기

   

![](images\모달.PNG)

영화 이미지를 클릭하면 modal이 나오도록 만든다.

```html
<img src="images/라이온킹.jpg" data-target="#lionking" data-toggle="modal" class="card-img-top" alt="라이온킹">
```

과 같이 작성한다.

영화 상세보기를 클릭하면 네이버 영화 페이지가 나오도록

```html
<a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=169637" target="_blank" class="btn btn-primary">영화정보 보러가기</a>
```

을 제작한다.