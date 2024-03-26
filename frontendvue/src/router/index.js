import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CarListing from '../views/CarListing.vue'
import AccountProfile from '../views/AccountProfile.vue'
// import SignUp from '../views/SignUp.vue'
import Reservations from '../views/Reservations.vue'
import ViewUsers from '../views/ViewUsers.vue'
import CreateCarForm from '../views/CreateCarForm.vue'
import LogIn from '../views/LogIn.vue'
import LogOut from '../views/LogOut.vue'
import ViewReservations from '../views/ViewReservations.vue'
import UserReport from '../views/UserReport.vue'
import CarPage from '../views/CarPage.vue'
import ReservationPage from '../views/ReservationPage.vue'
import paymentPage from '../views/paymentPage.vue'
import CSRViewReservations from '../views/CSRViewReservations.vue'
import CSRReport from '../views/CSRReport.vue'
import RegisterForm from '../components/RegisterForm.vue'
import LoginForm from '../components/LoginForm.vue'
import PickUp from '../views/PickUp.vue'


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
  // {
  //   path: '/signUp',
  //   name: 'signUp',
  //   component: SignUp
  // },
  {
    path: '/reservations',
    name: 'Reservations',
    component: Reservations
  },
  {
    path: '/viewUsers',
    name: 'ViewUsers',
    component: ViewUsers
  },	
  {
    path: '/createCar',
    name: 'createCar',
    component: CreateCarForm
  },
  {
    path: '/carPage/:id',
    name: 'carPage',
    component: CarPage
  },  
  
  {
    path: '/ReservationPage/:reservationId', 
    name: 'ReservationPage', 
    component: ReservationPage, 
    props: true 
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterForm
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/viewReservations',
    name: 'ViewReservations',
    component: ViewReservations
  },
  {
    path: '/userReport',
    name: 'UserReport',
    component: UserReport
  },
  {
    path: '/paymentPage',
    name: 'paymentPage',
    component: paymentPage
  }
  ,
  {
    path: '/CSRViewReservations',
    name: 'CSRViewReservations',
    component: CSRViewReservations
  },
  {
    path: '/CSRReport',
    name: 'CSRReport',
    component: CSRReport
  },
  {
    path: '/PickUp',
    name: 'PickUp',
    component: PickUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
