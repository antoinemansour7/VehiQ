import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
import SignUp from '../views/SignUp.vue'
import Reservations from '../views/Reservations.vue'
<<<<<<< HEAD
<<<<<<< Updated upstream
import BlankPage from '../views/BlankPage.vue'
import ViewUsers from '../views/ViewUsers.vue'
=======
=======
import CreateCarForm from '../views/CreateCarForm.vue'
>>>>>>> ee0176d520bd9686f1ec9a99823133d2f0e716f0
import LogIn from '../views/LogIn.vue'
import LogOut from '../views/LogOut.vue'
import ViewReservations from '../views/ViewReservations.vue'

<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> ee0176d520bd9686f1ec9a99823133d2f0e716f0
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
<<<<<<< HEAD
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
=======
    path: '/createCar',
    name: 'createCar',
    component: CreateCarForm
  },
  {
>>>>>>> ee0176d520bd9686f1ec9a99823133d2f0e716f0
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
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> ee0176d520bd9686f1ec9a99823133d2f0e716f0
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
