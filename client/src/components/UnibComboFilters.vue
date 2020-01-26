<template>
  <v-container px-12>
    <v-row justify="center" class="mb-n4">
      <v-col cols="12" md="4" sm="4" xl="3" class="text-center mb-n6">
        <v-autocomplete
          v-model="character"
          @change="characterChange()"
          :items="getCharacters()"
          spellcheck="false"
          label="Character"
          item-color="secondary"
          color="secondary"
        />
      </v-col>
      <v-col md="3" xl="2" class="text-center">
        <v-autocomplete
          v-if="character != 'All'"
          v-model="starter"
          :items="getStarters()"
          spellcheck="false"
          label="Starter"
          item-color="secondary"
          color="secondary"
        />
        <v-select v-else disabled label="Starter" item-color="secondary" color="secondary" />
      </v-col>
      <v-col md="2" xl="1" class="text-center">
        <v-select
          v-model="version"
          :items="versions"
          label="Version"
          item-color="secondary"
          color="secondary"
        />
      </v-col>
    </v-row>

    <v-row justify="center" class="mb-n8">
      <v-col md="5" xl="4" align-self="end">
        <v-range-slider
          v-model="meter"
          color="secondary"
          label="Meter"
          max="200"
          step="25"
          thumb-label
        />
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="6" md="2" sm="4" xl="1" class="text-center mb-n6">
        <v-select
          v-model="pos"
          :items="screenpos"
          label="Position"
          item-color="secondary"
          color="secondary"
        />
      </v-col>
      <v-col cols="6" md="2" sm="4" xl="1" class="text-center mx-xl-6 mb-n6">
        <v-row justify="center">
          <v-checkbox v-model="cs" label="Vorpal" color="secondary" flat />
        </v-row>
      </v-col>
      <v-col md="2" xl="1" class="text-center">
        <v-row justify="center">
          <v-checkbox v-model="ch" label="Counter Hit" color="secondary" flat />
        </v-row>
      </v-col>
    </v-row>

    <v-row v-if="character == 'Eltnum'" justify="center">
      <v-col cols="2" />
      <v-col md="1">
        <v-text-field
          v-model="eltnum.bullets"
          color="secondary"
          label="Bullets"
          :rules="[rules.required, rules.limit]"
          maxlength="2"
          placeholder=" "
          dense
        />
      </v-col>
      <v-col md="1">
        <v-text-field
          v-model="eltnum.enh"
          color="secondary"
          label="Enhanced"
          :rules="[rules.required, rules.limit]"
          maxlength="2"
          placeholder=" "
          dense
        />
      </v-col>
      <v-col cols="2" />
    </v-row>

    {{ cs }}
    <v-row v-if="character == 'Wagner'" justify="center" class="mt-n6">
      <v-col md="2" class="text-center mr-xl-n12">
        <v-row justify="center">
          <v-checkbox v-model="wagner.sw" label="Sword Install" color="secondary" flat />
        </v-row>
      </v-col>
      <v-col md="2" class="text-center ml-xl-n12">
        <v-row justify="center">
          <v-checkbox v-model="wagner.sh" label="Shield Install" color="secondary" flat />
        </v-row>
      </v-col>
    </v-row>

    <v-row v-if="character == 'Chaos'" justify="center" class="mt-n6">
      <v-col md="2" class="text-center">
        <v-row justify="center">
          <v-checkbox v-model="chaos.azhi" label="Azhi" color="secondary" flat />
        </v-row>
      </v-col>
    </v-row>

    <v-row justify="center" class="text-center">
      <v-col cols="4" md="2" lg="2" xl="1" sm="3">
        <v-select
          dense
          v-model="filter"
          :items="filters"
          label="Filter By"
          item-color="secondary"
          color="secondary"
        />
      </v-col>
      <v-col cols="1">
        <unibcomboplatform v-on:success="(success = true), $emit('success')" />
      </v-col>
    </v-row>

    <v-snackbar v-model="success" :timeout="5000" top>
      Combo posted
      <v-icon @click="success = false" color="error" small>
        mdi-close
      </v-icon>
    </v-snackbar>
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
      versions: ['ST', 'CLR'],
      screenpos: ['Midscreen', 'Corner'],
      filters: ['Newest', 'Damage'],

      starters: unibstarters.data(),

      character: this.initVars('char'),
      version: this.initVars('ver'),
      pos: this.initVars('pos'),
      starter: this.initVars('str'),
      meter: this.initVars('mtr'),
      ch: this.initVars('ch'),
      cs: true,
      success: false,
      filter: this.initVars('flt'),
      eltnum: {
        bullets: this.initVars('blt'),
        enh: this.initVars('enh'),
      },
      wagner: {
        sw: this.initVars('sw'),
        sh: this.initVars('sh'),
      },
      chaos: {
        azhi: this.initVars('az'),
      },

      rules: {
        required: value => !!value || 'Required',
        limit: value => (value >= 0 && value <= 13) || '0-13',
      },
    };
  },

  created() {
    this.init();
  },

  watch: {
    character: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { char: this.character }) });
    },

    version: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { ver: this.version }) });
    },

    pos: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { pos: this.pos }) });
    },

    starter: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { str: this.starter }) });
    },

    meter: function() {
      setTimeout(() => {
        this.$router
          .push({ query: Object.assign({}, this.$route.query, { mtr1: this.meter[0] }) })
          .catch(err => {});
        this.$router
          .push({ query: Object.assign({}, this.$route.query, { mtr2: this.meter[1] }) })
          .catch(err => {});
      }, 700);
    },

    ch: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { ch: this.ch }) });
    },

    cs: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { cs: this.cs }) });
    },

    filter: function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { flt: this.filter }) });
    },

    'eltnum.bullets': function() {
      setTimeout(() => {
        if (this.eltnum.bullets >= 0 && this.eltnum.bullets <= 13 && this.eltnum.bullets) {
          this.$router
            .push({
              query: Object.assign({}, this.$route.query, { blt: this.eltnum.bullets }),
            })
            .catch(err => {});
        }
      }, 700);
    },

    'eltnum.enh': function() {
      setTimeout(() => {
        if (this.eltnum.enh >= 0 && this.eltnum.enh <= 13 && this.eltnum.enh) {
          this.$router
            .push({
              query: Object.assign({}, this.$route.query, { enh: this.eltnum.enh }),
            })
            .catch(err => {});
        }
      }, 700);
    },

    'wagner.sw': function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { sw: this.wagner.sw }) });
    },

    'wagner.sh': function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { sh: this.wagner.sh }) });
    },

    'chaos.azhi': function() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { az: this.chaos.azhi }) });
    },
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

    init() {
      if (this.$route.query.cs) {
        this.cs = this.$route.query.cs === 'true';
      } else {
        this.cs = true;
      }
    },

    initVars(init) {
      if (this.$route.query.char && init === 'char') {
        return this.$route.query.char;
      } else if (init === 'char') {
        return 'All';
      }
      if (this.$route.query.ver && init === 'ver') {
        return this.$route.query.ver;
      } else if (init === 'ver') {
        return 'ST';
      }
      if (this.$route.query.pos && init === 'pos') {
        return this.$route.query.pos;
      } else if (init === 'pos') {
        return 'Midscreen';
      }
      if (this.$route.query.str && init === 'str') {
        return this.$route.query.str;
      } else if (init === 'str') {
        return 'All';
      }
      if (this.$route.query.mtr1 && this.$route.query.mtr2 && init === 'mtr') {
        var meter = [];
        meter[0] = parseInt(this.$route.query.mtr1);
        meter[1] = parseInt(this.$route.query.mtr2);
        return meter;
      } else if (init === 'mtr') {
        return [0, 200];
      }
      if (this.$route.query.cs && init === 'cs') {
        return this.$route.query.cs === 'true';
      } else if (init === 'cs') {
        return true;
      }
      if (this.$route.query.ch && init === 'ch') {
        return this.$route.query.ch === 'true';
      } else if (init === 'ch') {
        return false;
      }
      if (this.$route.query.flt && init === 'flt') {
        return this.$route.query.flt;
      } else if (init === 'flt') {
        return 'Newest';
      }
      if (this.$route.query.blt && init === 'blt') {
        return parseInt(this.$route.query.blt);
      } else if (init === 'blt') {
        return 13;
      }
      if (this.$route.query.enh && init === 'enh') {
        return parseInt(this.$route.query.enh);
      } else if (init === 'enh') {
        return 13;
      }
      if (this.$route.query.sw && init === 'sw') {
        return this.$route.query.sw === 'true';
      } else if (init === 'sw') {
        return true;
      }
      if (this.$route.query.sh && init === 'sh') {
        return this.$route.query.sh === 'true';
      } else if (init === 'sh') {
        return true;
      }
      if (this.$route.query.az && init === 'az') {
        return this.$route.query.az === 'true';
      } else if (init === 'az') {
        return true;
      }
    },
  },
};
</script>
