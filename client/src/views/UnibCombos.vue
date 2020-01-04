<template>
    <v-container mx-auto my-8>
        <v-row justify="center">
            <v-col md="2" sm="2" class="text-center">
              <v-select v-model="character" :items="characters"
               label="Character" item-color="secondary"/>
              <v-checkbox v-model="ch" label="Counter Hit" color="primary"
               flat/>
            </v-col>
            <v-col md="2" sm="2" class="text-center">
              <v-select v-model="version" :items="versions"
               label="Version" item-color="secondary"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

export default {
  data() {
    return {
      characters: [
        'Akatsuki',
        'Byakuya',
      ],
      versions: [
        'ST',
        'CLR',
      ],
      character: '',
      ch: false,
      version: '',
    };
  },
  created() {
    this.$vuetify.theme.themes.dark.primary = '#512DA8';
    this.$vuetify.theme.themes.dark.secondary = '#7E57C2';
  },
};
</script>
