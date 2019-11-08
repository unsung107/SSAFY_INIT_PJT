<template>
  <div id="app">
    <div class="container">
      <MovieList :moviesData="moviesData" :genresData="genresData" />
      <!-- 1-3. 호출하시오. 
        필요한 경우 props를 데이터를 보내줍니다.
      -->
    </div>
  </div>
</template>

<script>
const movieListUrl = 'https://gist.githubusercontent.com/edujason-hphk/f57d4cb915fcec433ece535b2f08a10f/raw/612fd3f00468722ead2cfe809f14e38230b47686/movie.json'
const genreListUrl = 'https://gist.githubusercontent.com/edujason-hphk/eea9c85a937cbf469b8f55fd7f8524df/raw/68bad38a2bc911d3a39bce26d6dd9b68a7efe849/genre.json'
const axios = require('axios');

import MovieList from './components/movies/MovieList.vue'
import { POINT_CONVERSION_COMPRESSED } from 'constants';
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,


export default {
  name: 'app',
  // 1-2. 아래에 등록 후
  components: {
    MovieList
  },
  data() {
    return {
      moviesData: {},
      genresData: {},
    }
  },
  mounted() {
    
    // 0. mounted 되었을 때, 
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오.
    axios.get(movieListUrl)
    .then(response1 => {
      this.moviesData = response1.data
      console.log(response1)
    })


    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
    axios.get(genreListUrl)
    .then(response2 => {
      this.genresData = response2.data
      // console.log(response2)
    })
  },
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
