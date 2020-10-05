<template>
  <div class="search-bar-wrap flex-center">
    <input
      @keyup.enter="onSubmit"
      v-model="keyword"
      class="search-input" type="text">
    <div
      @click="onSubmit"
      :class="[ keyword ? 'active-icon' : '', 'search-btn flex-center']">
        <i class="fas fa-search"></i>
    </div>
    <select v-model="style">
      <option>all</option>
      <option>Lager</option>
      <option>Ale</option>
      <option>etc</option>
    </select>
    <select v-model="country">
      <option>all</option>
      <option>KR</option>
      <option>etc</option>
    </select>
    <input type="number" v-model="abvmax">
    <input type="number" v-model="abvmin">
  </div>
</template>

<script>
import api from '@/api/api'

export default {
  name: 'searchBar',

  data() {
    return {
      keyword: null,
      style: 'all',
      country: 'all',
      abvmax: 100,
      abvmin: 0,
    }
  },

  methods: {
    onSubmit() {
      if (this.keyword) {
        api.search({ keyword: this.keyword, style: this.style, country: this.country, abvmax: this.abvmax, abvmin: this.abvmin
        }).then((res) => {
          console.log(res)
          if (res.status === 200) {
            this.$store.dispatch('search/fetchSearchResult', res)
          } else {
            alert("찾으시는 맥주가 없습니다 ㅠㅠ")
            this.$store.dispatch('search/fetchSearchResult', res)
          }
        }).catch(() => alert('error'))
        this.$router.push(`/search/${this.keyword}`).catch(() => {})
      } else {
        alert('검색어를 입력하세요!')
      }
    },
  },
  
  mounted() {
    let keywordSearched = this.$store.state.search.keyword
    let keyword = keywordSearched ? keywordSearched : null
    this.keyword = keyword
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.search-bar-wrap {
  border-radius: 25px;
  border: 1px solid lightgrey;
  background-color: white;
}

.search-input {
  width: 600px;
  height: 45px;
  margin-left: 30px;
  padding: 0;
  border: none;
  background-color: white;
  font-size: 20px;
  
  &:focus {
    outline: none;
  }
}

.search-btn {
  width: 75px;
  height: 50px;
  padding: 1px 2px;
  border-radius: 0 25px 25px 0;
  background-color: white;

  &:hover {
    @extend .active-icon;
    cursor: pointer;
    color: white;
  }
}

.active-icon {
  animation: active-icon;
  animation-duration: 250ms;
  animation-iteration-count: 2;
  color: $highlight-color;
  // background-color: $highlight-color;
  // border-color: $highlight-color;
}

@keyframes active-icon {
  to {font-size: 115%;}
}

@media screen and (max-width: 768px) {
  .search-bar-wrap {
    width: 100vw;
    border: none;
    border-radius: 0;
  }

  .search-input {
    height: 40px;
    flex-grow: 2;
    font-size: 18px;
    font-weight: bold;
  }

  .search-btn {
    height: 40px;
    width: 80px;
    border-radius: 0;
  }
}
</style>