import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/views/HomePage.vue'

const routes = [
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
    path: '/AboutPage',
    name: 'AboutPage',
    component: () => import('../components/views/AboutPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router