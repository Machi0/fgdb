<template>
  <v-app>
    <navbar />

    <v-content>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>

    <v-footer>
      <v-spacer />
      <div class="overline font-weight-bold primary--text">
        Contact:
        <a href="mailto:setzerfgdb@gmail.com" style="text-decoration: none">setzerfgdb@gmail.com</a>
      </div>
      <v-spacer />
    </v-footer>
  </v-app>
</template>

<script>
import navbar from '@/components/Navbar.vue';

export default {
  components: {
    navbar,
  },

  created() {
    document.title = 'GRD BREAK';
  },
};
</script>
