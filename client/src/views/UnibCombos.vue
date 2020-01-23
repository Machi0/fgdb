<template>
  <div>
    <unibfilters />
    <getcombos ref="get" />
  </div>
</template>

<script>
import unibfilters from '@/components/UnibComboFilters.vue';
import getcombos from '@/components/UnibComboGet.vue';

export default {
  components: {
    unibfilters,
    getcombos,
  },

  data() {
    return {};
  },

  created() {
    this.$vuetify.theme.themes.dark.primary = '#5E35B1';
    this.$vuetify.theme.themes.dark.secondary = '#7E57C2';
  },

  watch: {
    $route(to, from) {
      this.$refs.get.path = this.$route.fullPath;
      this.$refs.get.getPosts();
    },
  },
};
</script>
