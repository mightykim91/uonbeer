import Vue from 'vue'
import VueRouter from 'vue-router'

// modules
import accountsRouter from './modules/accountsRouter'

// components
import Home from '@/views/Home'
import SearchView from '@/views/search/SearchView'
import UserPageView from '@/views/userpage/UserPageView'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search/',
    name: 'Search',
    component: SearchView,
    children: [
      {
        path: ':keyword',
        name: 'SearchResult',
        component: SearchView
      }
    ]
  },
  {
    path: '/user/:username',
    name: 'UserPage',
    component: UserPageView,
  },
  ...accountsRouter,
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
