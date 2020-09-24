export default {
  namespaced: true,

  state: {
    beerItem: null,
    beerReviewArray: [],
  },

  mutations: {
    setBeerItem(state, item) {
      state.beerItem = item
    },
  },

  actions: {},

  
}