import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import AmazonLoginView from '../views/login/AmazonLoginView.vue'
import AdminLoginView from '../views/login/AdminLoginView.vue'
import HelpView from '../views/HelpView.vue'
import AboutView from '../views/AboutView.vue'
import ProfileView from '../views/authenticated/ProfileView.vue'
import ProductsView from '../views/authenticated/ProductsView.vue'
import ProductDetailsView from '../views/authenticated/ProductDetailsView.vue'
import GenerateBundleView from '../views/authenticated/GenerateBundleView.vue'
import ViewBundlesView from '../views/authenticated/ViewBundlesView.vue'
import ViewAnalyticsView from '../views/authenticated/ViewAnalyticsView.vue'
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
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/profile/products',
    name: 'Products',
    component: ProductsView
  },
  {
    path: '/profile/products/:id',
    name: 'ProductDetails',
    component: ProductDetailsView,
    props: true
  },
  {
    path: '/profile/generate-bundle',
    name: 'GenerateBundle',
    component: GenerateBundleView
  },
  {
    path: '/profile/view-bundles',
    name: 'ViewBundles',
    component: ViewBundlesView
  },
  {
    path: '/profile/view-analytics',
    name: 'ViewAnalytics',
    component: ViewAnalyticsView
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