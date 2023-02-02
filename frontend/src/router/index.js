import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import AmazonLoginView from '../views/login/AmazonLoginView.vue'
import AdminLoginView from '../views/login/AdminLoginView.vue'
import HelpView from '../views/HelpView.vue'
import AboutView from '../views/AboutView.vue'
import ProductsView from '../views/authenticated/ProductsView.vue'
import ProductDetailsView from '../views/authenticated/ProductDetailsView.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/amazon-login',
    name: 'AmazonLogin',
    component: AmazonLoginView
  },
  {
    path: '/admin-login',
    name: 'AdminLogin',
    component: AdminLoginView
  },
  {
    path: '/help',
    name: 'Help',
    component: HelpView
  },
  {
    path: '/about',
    name: 'About',
    component: AboutView
  },
  {
    path: '/products',
    name: 'Products',
    component: ProductsView
  },
  {
    path: '/products/:id',
    name: 'ProductDetails',
    component: ProductDetailsView,
    props: true
  },
  // redirect
  {
    path: '/all-products',
    redirect: '/products'
  },
  // 404 catchall
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router