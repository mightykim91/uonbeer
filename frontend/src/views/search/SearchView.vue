<template>
  <div>
    <div class="search-header flex-center">
        <search-bar></search-bar>
      <div class="search-filter-box flex-center">
        필터 옵션 (개발 중)
      </div>
    </div>    
    <h2 v-if="isSearchResult">
      {{ keyword }} 검색결과: {{ searchResultArray.length }}건
    </h2>
    
    <beer-list></beer-list>
  </div>
</template>

<script>
// components
import SearchBar from '@/components/common/SearchBar'
import BeerList from '@/components/beer/BeerList'

export default {
  name: "SearchView",

  components: {
    'search-bar': SearchBar,
    'beer-list': BeerList,
  },

  computed: {
    keyword() {
      return this.$store.state.search.keyword
    },
    searchResultArray() {
      return this.$store.state.search.searchResultArray
    },
    isSearchResult() {
      return !!this.$route.params.keyword
    },
  },

  destroyed() {
    this.$store.commit('search/resetSearchState')
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.search-header {
  height: 200px;
  margin-top: 40px;
  // background-image: $gradient-main;
  flex-direction: column;
  border-bottom: 1px solid lightgrey;
}

.search-filter-box {
  // temp
  height: 50px;
  color: blue; 
}

@media screen and (max-width: 768px) {
  .search-header {
    height: auto;
  }

  .search-filter-box {
    display: none;
  }
}

</style>