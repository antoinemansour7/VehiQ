import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
import SignUp from '../views/SignUp.vue'
import Reservations from '../views/Reservations.vue'
import LogIn from '../views/LogIn.vue'
import LogOut from '../views/LogOut.vue'
import BlankPage from '../views/BlankPage.vue'

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
    path: '/logIn',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/logOut',
    name: 'LogOut',
    component: LogOut
  },
  {
    path: '/blankPage',
    name: 'BlankPage',
    component: BlankPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
