<template>
    <v-container px-12 mt-2>

        <v-row justify="center" class="mb-n5">
            <v-col md="4" class="text-center">
              <v-select v-model="character" @change="characterChange()"
              :items="characters"
              label="Character" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col md="3" class="text-center">
              <v-autocomplete v-if="character != 'All'" v-model="starter"
              :items="getCombos()"
              label="Starter" item-color="secondary" color="secondary"/>
              <v-select v-else disabled
              label="Starter" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col md="2" class="text-center">
              <v-select v-model="version" :items="versions"
              label="Version" item-color="secondary" color="secondary"/>
            </v-col>
        </v-row>

        <v-row justify="center" class="mb-n7">
            <v-col md="2" class="text-center" align="top">
              <v-select v-model="pos" :items="screenpos"
              label="Position" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col md="4" align-self="end">
              <v-range-slider v-model="meter" color="secondary"
              label="Meter" max="200" step="25" thumb-label/>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-col md="2" class="text-center">
              <v-row justify="center">
                <v-checkbox v-model="ch" label="Counter Hit" color="secondary"
                ripple="false" flat/>
              </v-row>
            </v-col>
            <v-col md="2" class="text-center">
              <v-row justify="center">
                <v-checkbox v-model="cs" label="Vorpal" color="secondary"
                ripple="false" flat/>
              </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import unibstarters from '@/components/UnibStarters.vue';

export default {

  data() {
    return {
      characters: [
        'All',
        'Akatsuki',
        'Byakuya',
        'Carmine',
        'Chaos',
        'Eltnum',
        'Enkidu',
        'Gordeau',
        'Hilda',
        'Hyde',
        'Linne',
        'Merkava',
        'Mika',
        'Nanase',
        'Orie',
        'Phonon',
        'Seth',
        'Vatista',
        'Wagner',
        'Waldstein',
        'Yuzuriha',
      ],
      versions: [
        'ST',
        'CLR',
      ],
      screenpos: [
        'Midscreen',
        'Corner',
      ],

      starters: unibstarters.data(),

      character: 'All',
      version: 'ST',
      pos: 'Midscreen',
      starter: 'All',
      meter: [0, 200],
      ch: false,
      cs: false,
    };
  },

  methods: {
    getCombos() {
      return this.starters[this.version][this.character];
    },

    characterChange() {
      this.starter = 'All';
    },
  },

  created() {
    this.$vuetify.theme.themes.dark.primary = '#512DA8';
    this.$vuetify.theme.themes.dark.secondary = '#7E57C2';
  },
};
</script>
