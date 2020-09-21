import * as cookies from 'vue-cookies'

export default {
  namespaced: true,
  
  state: {
    cookie: cookies.get('auth') ? true : false, 
    showSidebar: false,
  },

  mutations: {
    toggleShowSidebar(state) {
      state.showSidebar = !state.showSidebar
    },
    toggleCookie(state) {
      state.cookie = !state.cookie
    }
  },

  actions: {
  }
}