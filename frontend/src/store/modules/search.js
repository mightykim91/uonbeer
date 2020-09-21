export default {
  namespaced: true,
  
  state: {
    keyword: null,
    searchResultArray: [],
  },

  getters: {
    getSearchResultCount(state) {
      return state.searchResultArray.length
    }
  },

  mutations: {
    setKeyword(state, keyword) {
      state.keyword = keyword
    },
    setSearchResultArray(state, resultArray) {
      state.searchResultArray = resultArray
    },
    resetSearchState(state) {
      state.keyword = null,
      state.searchResultArray = []
    },
  },

  actions: {
    fetchSearchResult({ commit }, keyword) {
      let dummyItem = {
        name: 'omg IPA',
        country: '대한민국',
        state: '서울',
        brewery: 'mighty beer',
        abv: '7.5%',
        reviewCount: 3,
        likeCount: 150,
      }
      let dummyArray = []
      ;(function test() {for (let i=0; i<10; i++) {dummyArray.push(dummyItem)}}())
      commit('setKeyword', keyword)
      commit('setSearchResultArray', dummyArray)
    }
  }
}