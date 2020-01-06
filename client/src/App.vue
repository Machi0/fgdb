<template>
  <v-app>
    <navbar/>

    <v-content>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import navbar from '@/components/Navbar.vue';

export default {
  components: {
    navbar,
  },
};
</script>
