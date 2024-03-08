import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/views/HomePage.vue'

const routes = [
  {
    path: '/AccountProfile',
    name: 'AccountProfile',
    component: () => import('../components/views/AccountProfile.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/DashboardPage',
    name: 'DashboardPage',
    component: () => import('../components/views/DashboardPage.vue')
  },
  {
    path: '/CarListing',
    name: 'CarListing',
    component: () => import('../components/CarListing.vue')
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router