import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/empleados/nuevo',
    name: 'nuevo',
    component: () => import(/* webpackChunkName: "nuevo" */ '../views/NuevoEmpleadoView.vue')
  },
  {
    path: '/empleados/editar/:id',
    name: 'editar',
    component: () => import(/* webpackChunkName: "editar" */ '../views/EditarEmpleadoView.vue')
  },
  {
    path: '/empleados/eliminar/:id',
    name: 'eliminar',
    component: () => import(/* webpackChunkName: "eliminar" */ '../views/EliminarEmpleadoView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
