import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import UnibCombos from '../views/UnibCombos.vue';
import AdminLogin from '../views/AdminLogin.vue';
import Admin from '../views/Admin.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/unib/combos',
    name: 'unib combos',
    component: UnibCombos,
  },
  {
    path: '/matrix/',
    name: 'login',
    component: AdminLogin,
  },
  {
    path: '/admin/',
    name: 'admin',
    component: Admin,
    beforeEnter(to, from, next) {
      console.log(from);
      if (from.name == 'login') {
        next();
      } else {
        next({
          name: 'home',
        });
      }
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
