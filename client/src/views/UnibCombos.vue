<template>
    <v-container px-12>

        <v-row justify="center" class="mb-n6">
            <v-col md="4" class="text-center">
              <v-autocomplete v-model="character" @change="characterChange()"
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

        <v-row justify="center" class="mb-n6">
            <v-col md="2" class="text-center" align="top">
              <v-select v-model="workson" :items="setWorksOn()" multiple
              label="Works On" item-color="secondary" color="secondary">
                <template v-slot:prepend-item>
                  <v-list-item ripple @click="allCharsToggle()">
                    <v-list-item-action>
                      <v-icon :color="allChars() ? 'secondary' : ''">{{ checkIcon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title> All </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-divider/>
                </template>
              </v-select>
            </v-col>
            <v-col md="2" class="text-center" align="top">
              <v-select v-model="pos" :items="screenpos"
              label="Position" item-color="secondary" color="secondary"/>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-col md="5" align-self="end">
              <v-range-slider v-model="meter" color="secondary"
              label="Meter" max="200" step="25" thumb-label/>
            </v-col>
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
        {{ this.workson }}
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
      workson: [],
      pos: 'Midscreen',
      starter: 'All',
      meter: [0, 200],
      ch: false,
      cs: false,
    };
  },

  computed: {
    allCharsIcon() {
      return this.workson.length === this.characters.length - 1;
    },

    checkIcon() {
      if (this.allCharsIcon) return 'mdi-checkbox-marked';
      return 'mdi-checkbox-blank-outline';
    },
  },

  methods: {
    getCombos() {
      return this.starters[this.version][this.character];
    },

    characterChange() {
      this.starter = 'All';
    },

    setWorksOn() {
      return this.characters.slice(1);
    },

    allChars() {
      return this.workson.length === this.characters.length - 1;
    },

    allCharsToggle() {
      this.$nextTick(() => {
        if (this.allChars()) {
          this.workson = [];
        } else {
          this.workson = this.characters.slice(1);
        }
      });
    },
  },

  created() {
    this.$vuetify.theme.themes.dark.primary = '#5E35B1';
    this.$vuetify.theme.themes.dark.secondary = '#7E57C2';
  },
};
</script>
