import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import HomeView from '../views/HomeView.vue';
import AccountView from '../views/AccountView.vue';


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'login',
            component: LoginView
        },
        {
            path: '/home/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/:slug/:id/',
            name: 'employee',
            component: AccountView
          },
    ]
})

export default router
