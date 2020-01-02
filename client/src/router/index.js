import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import UnibCombos from '../views/UnibCombos.vue';

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
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
