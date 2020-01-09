<template>
  <div>
    <unibfilters/>
  </div>
</template>

<script>
import unibfilters from '@/components/UnibComboFilters.vue';

export default {
  components: {
    unibfilters,
  },

  data() {
    return {
    };
  },

  created() {
    this.$vuetify.theme.themes.dark.primary = '#5E35B1';
    this.$vuetify.theme.themes.dark.secondary = '#7E57C2';
  },
};
</script>
