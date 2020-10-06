import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import cookies from 'vue-cookies'
import vmodal from 'vue-js-modal'
import VCalendar from 'v-calendar'
import infiniteScroll from 'vue-infinite-scroll'

require('@/assets/scss/main.scss')

Vue.use(cookies)
Vue.use(vmodal)

// v-calendar
Vue.use(VCalendar)
// infinite scroll
Vue.use(infiniteScroll)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
