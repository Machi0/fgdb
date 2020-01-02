import Vue from 'vue';
import Vuetify from 'vuetify';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

new Vue({
  router,
  Vuetify,
  render: h => h(App),
}).$mount('#app');
