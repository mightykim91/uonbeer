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
      let dummyArray = []
      ;(function() {for (let i=0; i<10; i++) {
        let dummyItem = {
          id: i,
          name: 'omg IPA' + i,
          country: '대한민국',
          state: '서울',
          brewery: 'mighty beer',
          abv: '7.5%',
          rate: 4.3,
          reviewCount: 3,
          likeCount: 150,
        }
        dummyArray.push(dummyItem)
      }}())
      commit('setKeyword', keyword)
      commit('setSearchResultArray', dummyArray)
    }

    // fetchSearchResult({commit}, response) {
    //   commit('setKeyword', response.config.params.keyword)
    //   commit('setSearchResultArray', response.data)
    // }
  }
}