<template>
    <v-container px-12>

        <v-row justify="center" class="mb-n4">
            <v-col cols="12" md="4" sm="4" xl="3" class="text-center mb-n6">
              <v-autocomplete v-model="character" @change="characterChange()"
              :items="getCharacters()" spellcheck="false"
              label="Character" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col md="3" xl="2" class="text-center">
              <v-autocomplete v-if="character != 'All'" v-model="starter"
              :items="getStarters()" spellcheck="false"
              label="Starter" item-color="secondary" color="secondary"/>
              <v-select v-else disabled
              label="Starter" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col md="2" xl="1" class="text-center">
              <v-select v-model="version" :items="versions"
              label="Version" item-color="secondary" color="secondary"/>
            </v-col>
        </v-row>

        <v-row justify="center" class="mb-n8">
            <v-col md="5" xl="4" align-self="end">
              <v-range-slider v-model="meter" color="secondary"
              label="Meter" max="200" step="25" thumb-label/>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-col cols="6" md="2" sm="4" xl="1" class="text-center mb-n7" align="top">
              <v-select v-model="pos" :items="screenpos"
              label="Position" item-color="secondary" color="secondary"/>
            </v-col>
            <v-col cols="6" md="2" sm="4" xl="1" class="text-center mb-n7 mx-xl-6">
              <v-row justify="center">
                <v-checkbox v-model="cs" label="Vorpal" color="secondary"
                ripple="false" flat/>
              </v-row>
            </v-col>
            <v-col md="2" xl="1" class="text-center mb-n8">
              <v-row justify="center">
                <v-checkbox v-model="ch" label="Counter Hit" color="secondary"
                ripple="false" flat/>
              </v-row>
            </v-col>
        </v-row>

        <v-row v-if="character=='Eltnum'" justify="center" class="mt-6">
            <v-col cols="2"/>
            <v-col md="1">
              <v-text-field v-model="eltnum.bullets" color="secondary"
              label="Bullets" :rules="[rules.required, rules.limit]"
              maxlength="2" dense/>
            </v-col>
            <v-col md="1">
              <v-text-field v-model="eltnum.enh" color="secondary"
              label="Enhanced" :rules="[rules.required, rules.limit]"
              maxlength="2" dense/>
            </v-col>
          <v-col cols="2"/>
        </v-row>

        <v-row v-if="character=='Wagner'" justify="center">
          <v-col md="2" class="text-center mr-xl-n12">
            <v-row justify="center">
              <v-checkbox v-model="wagner.sw" label="Sword Install" color="secondary"
              ripple="false" flat/>
            </v-row>
          </v-col>
          <v-col md="2" class="text-center ml-xl-n12">
            <v-row justify="center">
              <v-checkbox v-model="wagner.sh" label="Shield Install" color="secondary"
              ripple="false" flat/>
            </v-row>
          </v-col>
        </v-row>

        <v-row v-if="character=='Chaos'" justify="center">
          <v-col md="2" class="text-center">
            <v-row justify="center">
              <v-checkbox v-model="chaos.azhi" label="Azhi" color="secondary"
              ripple="false" flat/>
            </v-row>
          </v-col>
        </v-row>

        <unibcomboplatform/>
    </v-container>
</template>

<script>
import unibstarters from '@/components/UnibStarters.vue';
import unibcomboplatform from '@/components/UnibComboPlatform.vue';

export default {
  name: 'unibfilters',

  components: {
    unibcomboplatform,
  },

  data() {
    return {
      characters: {
        ST: [
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

        CLR: [
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
          'Londrekia',
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
      },
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

      eltnum: {
        bullets: 13,
        enh: 13,
      },

      wagner: {
        sw: true,
        sh: true,
      },

      chaos: {
        azhi: true,
      },

      rules: {
        required: value => !!value || 'Required',
        limit: value => (value >= 0 && value <= 13) || '0-13',
      },
    };
  },

  methods: {
    getStarters() {
      return this.starters[this.version][this.character];
    },

    getCharacters() {
      if (this.version === 'CLR') {
        return this.characters.CLR;
      }
      return this.characters.ST;
    },

    characterChange() {
      this.starter = 'All';
    },
  },
};
</script>
