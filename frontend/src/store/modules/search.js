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
    fetchSearchResult({commit}, response) {
      commit('setKeyword', response.config.params.keyword)
      commit('setSearchResultArray', response.data)
    }
  }
}