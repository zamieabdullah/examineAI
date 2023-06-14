import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'home',
      component: Home
    }
  ]
})

export default router
