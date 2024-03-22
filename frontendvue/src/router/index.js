import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
import SignUp from '../views/SignUp.vue'
import Reservations from '../views/Reservations.vue'
import BlankPage from '../views/BlankPage.vue'
import ViewUsers from '../views/ViewUsers.vue'
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
  },
  {
    path: '/reservations',
    name: 'Reservations',
    component: Reservations
  },
  {
    path: '/blankPage',
    name: 'BlankPage',
    component: BlankPage
  },
  {
    path: '/viewUsers',
    name: 'ViewUsers',
    component: ViewUsers
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
