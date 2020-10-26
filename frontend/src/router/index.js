import Vue from 'vue'
import VueRouter from 'vue-router'
import Register from '../components/Register.vue'
import Home from '../components/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        name:'home',
        component:Home
    },
    {
        path:'/register',
        name:'register',
        component:Register
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router