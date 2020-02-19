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
        <v-slider
          v-model="meter"
          color="secondary"
          label="Meter"
          max="200"
          min="0"
          step="50"
          thumb-label
          @change="meterChange()"
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
          @blur="bltChange()"
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
          @blur="enhChange()"
        />
      </v-col>
      <v-col cols="2" />
    </v-row>

    <v-row v-if="character == 'Wagner'" justify="center" class="mt-n8">
      <v-col md="2" class="text-center mr-xl-n12">
        <v-row justify="center">
          <v-checkbox
            v-model="wagner.sw"
            label="Sword Install"
            color="secondary"
            flat
            @change="swChange()"
          />
        </v-row>
      </v-col>
      <v-col md="2" class="text-center ml-xl-n12">
        <v-row justify="center">
          <v-checkbox
            v-model="wagner.sh"
            label="Shield Install"
            color="secondary"
            flat
            @change="shChange()"
          />
        </v-row>
      </v-col>
    </v-row>

    <v-row v-if="character == 'Chaos'" justify="center" class="mt-n8">
      <v-col md="2" class="text-center">
        <v-row justify="center">
          <v-checkbox
            v-model="chaos.azhi"
            label="Azhi"
            color="secondary"
            flat
            @change="azhiChange()"
          />
        </v-row>
      </v-col>
    </v-row>

    <v-row v-if="character == 'Londrekia'" justify="center" class="mt-n8">
      <v-col md="2" class="text-center">
        <v-row justify="center">
          <v-checkbox
            v-model="londrekia.ice"
            label="Ice Install"
            color="secondary"
            flat
            @change="iceChange()"
          />
        </v-row>
      </v-col>
    </v-row>

    <v-row justify="center" class="text-center">
      <v-col cols="6" md="2" lg="2" xl="1" sm="3">
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
      <v-col cols="1" class="mx-xl-n12  mx-lg-n5 mx-9">
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
      version: this.$route.query.ver || 'CLR',
      pos: this.$route.query.pos || 'Midscreen',
      starter: this.$route.query.str || 'All',
      meter: 200,
      ch: JSON.parse(this.$route.query.ch || false),
      cs: JSON.parse(this.$route.query.cs || true),
      success: false,
      filter: this.$route.query.flt || 'Newest',
      eltnum: {
        bullets: 13,
        enh: 13,
      },
      wagner: {
        sw: JSON.parse(this.$route.query.sw || true),
        sh: JSON.parse(this.$route.query.sh || true),
      },
      chaos: {
        azhi: JSON.parse(this.$route.query.az || true),
      },
      londrekia: {
        ice: JSON.parse(this.$route.ice || true),
      },

      rules: {
        required: value => Number.isInteger(parseInt(value)) || 'Required',
        limit: value => (value >= 0 && value <= 13) || '0-13',
      },
    };
  },

  created() {
    this.setMeter();
    this.setBullets();
    this.setEnh();
  },

  watch: {
    $route(to, from) {
      this.character = this.$route.query.char || 'All';
      this.version = this.$route.query.ver || 'CLR';
      this.pos = this.$route.query.pos || 'Midscreen';
      this.starter = this.$route.query.str || 'All';
      this.filter = this.$route.query.flt || 'Newest';
      this.setMeter();
      this.ch = JSON.parse(this.$route.query.ch || false);
      this.cs = JSON.parse(this.$route.query.cs || false) || this.$route.query.cs == undefined;
      this.setBullets();
      this.setEnh();
      this.wagner.sw =
        JSON.parse(this.$route.query.sw || false) || this.$route.query.sw == undefined;
      this.wagner.sh =
        JSON.parse(this.$route.query.sh || false) || this.$route.query.sh == undefined;
      this.chaos.azhi =
        JSON.parse(this.$route.query.az || false) || this.$route.query.az == undefined;
      this.londrekia.ice =
        JSON.parse(this.$route.query.ice || false) || this.$route.query.ice == undefined;
    },
  },

  methods: {
    setMeter() {
      if (this.$route.query.mtr == 0) {
        this.meter = 0;
      } else if (this.$route.query.mtr) {
        this.meter = this.$route.query.mtr;
      } else {
        this.meter = 200;
      }
    },

    setBullets() {
      if (this.$route.query.blt == 0) {
        this.eltnum.bullets = 0;
      } else if (this.$route.query.blt) {
        this.eltnum.bullets = this.$route.query.blt;
      } else {
        this.eltnum.bullets = 13;
      }
    },

    setEnh() {
      if (this.$route.query.enh == 0) {
        this.eltnum.enh = 0;
      } else if (this.$route.query.enh) {
        this.eltnum.enh = this.$route.query.enh;
      } else {
        this.eltnum.enh = 13;
      }
    },

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
      this.$router.push({
        query: Object.assign({}, this.$route.query, { char: this.character }, { page: undefined }),
      });
      this.$emit('pageReset');
    },

    versionChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { ver: this.version }, { page: undefined }),
      });
    },

    posChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { pos: this.pos }, { page: undefined }),
      });
    },

    starterChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { str: this.starter }, { page: undefined }),
      });
    },

    filterChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { flt: this.filter }, { page: undefined }),
      });
    },

    meterChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { mtr: this.meter }, { page: undefined }),
      });
    },

    chChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { ch: this.ch }, { page: undefined }),
      });
    },

    csChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { cs: this.cs }, { page: undefined }),
      });
    },

    bltChange() {
      if (this.eltnum.bullets >= 0 && this.eltnum.bullets <= 13 && this.eltnum.bullets) {
        this.$router
          .push({
            query: Object.assign(
              {},
              this.$route.query,
              { blt: this.eltnum.bullets },
              { page: undefined }
            ),
          })
          .catch(err => {});
      }
    },

    enhChange() {
      if (this.eltnum.enh >= 0 && this.eltnum.enh <= 13 && this.eltnum.enh) {
        this.$router
          .push({
            query: Object.assign(
              {},
              this.$route.query,
              { enh: this.eltnum.enh },
              { page: undefined }
            ),
          })
          .catch(err => {});
      }
    },

    swChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { sw: this.wagner.sw }, { page: undefined }),
      });
    },

    shChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { sh: this.wagner.sh }, { page: undefined }),
      });
    },

    azhiChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { az: this.chaos.azhi }, { page: undefined }),
      });
    },

    iceChange() {
      this.$router.push({
        query: Object.assign(
          {},
          this.$route.query,
          { ice: this.londrekia.ice },
          { page: undefined }
        ),
      });
    },
  },
};
</script>
