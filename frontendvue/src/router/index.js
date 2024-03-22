import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
import SignUp from '../views/SignUp.vue'
import Reservations from '../views/Reservations.vue'
<<<<<<< Updated upstream
import BlankPage from '../views/BlankPage.vue'
import ViewUsers from '../views/ViewUsers.vue'
=======
import LogIn from '../views/LogIn.vue'
import LogOut from '../views/LogOut.vue'
import ViewReservations from '../views/ViewReservations.vue'

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    path: '/blankPage',
    name: 'BlankPage',
    component: BlankPage
  },
  {
    path: '/viewUsers',
    name: 'ViewUsers',
    component: ViewUsers
=======
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
    path: '/viewReservations',
    name: 'ViewReservations',
    component: ViewReservations
>>>>>>> Stashed changes
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
