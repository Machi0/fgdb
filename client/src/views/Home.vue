<template>
  <div>
    <gamelist />
  </div>
</template>

<script>
import gamelist from '@/components/HomeGames.vue';
export default {
  name: 'home',
  components: {
    gamelist,
  },

  created() {
    this.$vuetify.theme.themes.dark.primary = '#B71C1C';
  },
};
</script>
