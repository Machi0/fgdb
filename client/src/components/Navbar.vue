<template>
  <v-toolbar app color="primary" max-height="45" flat>
    <v-toolbar-items>
      <v-hover v-slot:default="{ hover }">
        <router-link to="/">
          <v-img
            src="@/assets/53454.png"
            alt="FGDB Logo"
            contain
            width="43"
            :class="{ 'on-hover': hover }"
            class="ml-4"
          />
        </router-link>
      </v-hover>
    </v-toolbar-items>
    <div class="mx-4" />
    <v-toolbar-items class="mt-4">
      <v-hover v-slot:default="{ hover }">
        <router-link to="/unib/combos">
          <v-img
            src="@/assets/453345.png"
            alt="UNIB Logo"
            contain
            width="130"
            :class="{ 'on-hover': hover }"
            class="fade"
          />
        </router-link>
      </v-hover>
    </v-toolbar-items>
  </v-toolbar>
</template>

<style scoped>
.fade {
  transition: opacity 0.2s ease-in-out;
}

.fade:not(.on-hover) {
  opacity: 0.5;
}
</style>

<script>
export default {
  name: 'navbar',
};
</script>
