PJT 09

## 1. 부모 컴포넌트에 자식 컴포넌트 넣기

- 각 부모 컴포넌트에 자식 컴포넌트를 넣고 필요한 자료들을 props를 통해 넣어준다.

`App.vue`

```js
const axios = require('axios');
import MovieList from './components/movies/MovieList.vue'

export default{
    components: {
        MovieList
      },
    mounted() {
        axios.get(movieListUrl)
        .then(response1 => {
          this.moviesData = response1.data
          console.log(response1)
        })
    }
}

```

`MovieList.vue`

```js
export default {
  props: {
    moviesData: {
      type: Object,
      required: true
    }
  }
}
```



## 2. MovieList.vue에서 모든 영화 자료를 v-for를 이용해 표현

`MovieList.vue`

```js
   <div class="row mt-5">
    <MovieListItem v-for="movie in moviesData" :movie="movie" :key="movie.id" />
   </div>
```

MovieListItem.vue

```html
<template>
  <div class="col-3 my-3">
    <!-- img 태그에 src와 alt값(영화제목)을 설정하시오 -->
    <img class="movie--poster my-3" :src="movie.poster_url">
    <!-- 영화 제목을 출력하시오. -->
    <h3>{{ movie.name }}</h3>
    
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 합니다. -->
    <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">영화 정보 상세보기</button>
    <!-- 1-3. 호출하시오.
      필요한 경우 props를 데이터를 보내줍니다.
      -->
    <MovieListItemModal :movie="movie" />
  </div>
</template>
```



## 3. MovieListItem 에서 modal을 불러올수 있도록 한다

- 그러기 위하여 MovieListItemModal 에서 modal에 id값을 준다

`MovieListItemModal`

```html
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">
    ...
</div>
```

- 그 후 MovieListItem 에서 각 모달을 불러올 수 있도록 한다

`MovieListItem `

```html
<button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">
```



## 4. 장르를 선택하여 선택적으로 보여주기!

- 장르선택을 위하여 MovieList 에 선택창을 만든다
- 이 때 showMode라는 것을 바꿔줄 수 있도록 v-model 항목을 넣는다.

`MovieList.vue`

```html
   <select class="form-control" v-model="showMode">
      <option v-for="genre in genresData" v-bind:key="genre.id">{{genre.name}}</option>
      <option key="ALL">전체</option>
    </select>
```

```js
  computed: {
    movieListbyShowMode: function() {
      if (this.showMode && this.showMode !== '전체'){
        return this.moviesData.filter(movie => {
          return this.genresData[movie.genre_id - 1].name === this.showMode
        })
      } else{
        return this.moviesData
      }
    }
```

를 통하여 선택한 항목만 보여주는 movieListbyShowMode 를 만든다

```html
<MovieListItem v-for="movie in movieListbyShowMode" :movie="movie" :key="movie.id" />
```

로 수정해준다.

![1](img\1.JPG)

![2](img\2.JPG)

![3](img\3.JPG)

![4](img\4.JPG)