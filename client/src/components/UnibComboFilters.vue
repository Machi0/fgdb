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
          @change="starterChange()"
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
          @change="versionChange()"
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
          @end="meterChange()"
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
          @change="posChange()"
        />
      </v-col>
      <v-col cols="6" md="2" sm="4" xl="1" class="text-center mx-xl-6 mb-n6">
        <v-row justify="center">
          <v-checkbox v-model="cs" label="Vorpal" color="secondary" flat @change="csChange()" />
        </v-row>
      </v-col>
      <v-col md="2" xl="1" class="text-center">
        <v-row justify="center">
          <v-checkbox
            v-model="ch"
            label="Counter Hit"
            color="secondary"
            flat
            @change="chChange()"
          />
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
          @change="filterChange()"
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

      character: this.$route.query.char || 'All',
      version: this.$route.query.ver || 'ST',
      pos: this.$route.query.pos || 'Midscreen',
      starter: this.$route.query.str || 'All',
      meter: [0, 200],
      ch: JSON.parse(this.$route.query.ch || false),
      cs: JSON.parse(this.$route.query.cs || true),
      success: false,
      filter: this.$route.query.flt || 'Newest',
      eltnum: {
        bullets: parseInt(this.$route.query.blt) || 13,
        enh: parseInt(this.$route.query.enh) || 13,
      },
      wagner: {
        sw: JSON.parse(this.$route.query.sw || true),
        sh: JSON.parse(this.$route.query.sh || true),
      },
      chaos: {
        azhi: JSON.parse(this.$route.query.az || true),
      },

      rules: {
        required: value => !!value || 'Required',
        limit: value => (value >= 0 && value <= 13) || '0-13',
      },
    };
  },

  created() {
    this.meterInit();
  },

  watch: {
    $route(to, from) {
      this.character = this.$route.query.char || 'All';
      this.version = this.$route.query.ver || 'ST';
      this.pos = this.$route.query.pos || 'Midscreen';
      this.starter = this.$route.query.str || 'All';
      this.filter = this.$route.query.flt || 'Newest';
      this.meterInit();
      this.ch = JSON.parse(this.$route.query.ch || false);
      this.cs = JSON.parse(this.$route.query.cs || false) || this.$route.query.cs == undefined;
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
      this.$router.push({ query: Object.assign({}, this.$route.query, { char: this.character }) });
    },

    versionChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { ver: this.version }) });
    },

    posChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { pos: this.pos }) });
    },

    starterChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { str: this.starter }) });
    },

    filterChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { flt: this.filter }) });
    },

    meterChange() {
      var a = Object.assign({}, this.$route.query, { mtr1: this.meter[0] });
      a = Object.assign({}, a, { mtr2: this.meter[1] });
      this.$router.push({ query: a }).catch(err => {});
    },

    chChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { ch: this.ch }) });
    },

    csChange() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { cs: this.cs }) });
    },

    meterInit() {
      if (this.$route.query.mtr1 && this.$route.query.mtr2) {
        this.meter = [this.$route.query.mtr1, this.$route.query.mtr2];
      } else {
        this.meter = [0, 200];
      }
    },
  },
};
</script>
