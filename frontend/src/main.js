import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import cookies from 'vue-cookies'
import vmodal from 'vue-js-modal'
import VCalendar from 'v-calendar'

require('@/assets/scss/main.scss')

Vue.use(cookies)
Vue.use(vmodal)

// v-calendar
Vue.use(VCalendar)
//쿠키 만료 1일
Vue.$cookies.config("1d")

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
