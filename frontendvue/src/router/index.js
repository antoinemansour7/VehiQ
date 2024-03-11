import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
import SignUp from '../views/SignUp.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/carListing',
    name: 'carListing',
    component: CarListing
  },
  {
    path: '/profile',
    name: 'profile',
    component: AccountProfile
  },
  {
    path: '/signUp',
    name: 'signUp',
    component: SignUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
