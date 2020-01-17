<template>
  <div>
    <v-card>
      <v-card-title v-if="tw">
        Upload Twitter Post
        <v-spacer />
        <v-icon @click="$emit('close', false), reset()" small color="error" :disabled="loading">
          mdi-close
        </v-icon>
      </v-card-title>

      <v-card-title v-if="yt">
        Upload Youtube Video
        <v-spacer />
        <v-icon @click="$emit('close', false), reset()" small color="error" :disabled="loading">
          mdi-close
        </v-icon>
      </v-card-title>

      <v-card-text>
        <v-container class="mt-n6">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row class="text-center" justify="center">
              <v-col v-if="tw === true">
                <v-text-field
                  v-model="twlink"
                  color="secondary"
                  maxlength="200"
                  label="URL"
                  :rules="[rules.required, rules.twcheck]"
                  spellcheck="false"
                  validate-on-blur
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>

              <v-col v-if="yt === true">
                <v-text-field
                  v-model="ytlink"
                  color="secondary"
                  maxlength="200"
                  label="URL"
                  :rules="[rules.required, rules.ytcheck]"
                  spellcheck="false"
                  validate-on-blur
                  hint="Please add timestamp if necessary"
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>
            </v-row>

            <v-row class="text-center" justify="center">
              <v-col cols="4">
                <v-select
                  v-model="version"
                  :items="versions"
                  label="Version"
                  item-color="secondary"
                  color="secondary"
                  :rules="[rules.required]"
                  :readonly="loading"
                />
              </v-col>
              <v-col>
                <v-autocomplete
                  v-model="character"
                  :items="characters[version].slice(1)"
                  @change="characterChange()"
                  :rules="[rules.required]"
                  label="Character"
                  item-color="secondary"
                  color="secondary"
                  spellcheck="false"
                  :readonly="loading"
                />
              </v-col>
            </v-row>

            <v-row class="text-center" justify="center">
              <v-col>
                <v-autocomplete
                  v-model="starter"
                  :items="getStarters()"
                  :rules="[rules.required]"
                  label="Starter"
                  item-color="secondary"
                  spellcheck="false"
                  color="secondary"
                  :readonly="loading"
                />
              </v-col>
              <v-col>
                <v-text-field
                  v-model="damage"
                  color="secondary"
                  label="Damage"
                  :rules="[rules.required]"
                  maxlength="6"
                  validate-on-blur
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>
            </v-row>

            <v-row class="text-center" justify="center">
              <v-col>
                <v-select
                  v-model="pos"
                  :items="screenpos"
                  label="Position"
                  item-color="secondary"
                  color="secondary"
                  :rules="[rules.required]"
                  :readonly="loading"
                />
              </v-col>
              <v-col>
                <v-text-field
                  v-model="meter"
                  color="secondary"
                  label="Meter"
                  :rules="[rules.required, rules.meter]"
                  maxlength="3"
                  validate-on-blur
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>
            </v-row>

            <v-row class="text-center mt-n6" justify="center">
              <v-col cols="6" md="4" sm="4" lg="4" xl="4">
                <v-row justify="center">
                  <v-checkbox
                    v-model="cs"
                    label="Vorpal"
                    color="secondary"
                    flat
                    :readonly="loading"
                  />
                </v-row>
              </v-col>
              <v-col cols="6" md="4" sm="4" lg="4" xl="4">
                <v-row justify="center">
                  <v-checkbox
                    v-model="ch"
                    label="Counter Hit"
                    color="secondary"
                    flat
                    :readonly="loading"
                  />
                </v-row>
              </v-col>
            </v-row>

            <v-row v-if="character == 'Eltnum'" justify="center" class="mt-n4">
              <v-col cols="2" />
              <v-col md="2">
                <v-text-field
                  v-model="eltnum.bullets"
                  color="secondary"
                  label="Bullets"
                  :rules="[rules.limit]"
                  maxlength="2"
                  dense
                  validate-on-blur
                  placeholder=" "
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>
              <v-col md="2">
                <v-text-field
                  v-model="eltnum.enh"
                  color="secondary"
                  label="Enhanced"
                  :rules="[rules.limit, rules.ratio]"
                  maxlength="2"
                  dense
                  validate-on-blur
                  placeholder=" "
                  :readonly="loading"
                  autocomplete="off"
                />
              </v-col>
              <v-col cols="2" />
            </v-row>

            <v-row v-if="character == 'Wagner'" justify="center" class="mt-n10">
              <v-col cols="6" md="4" sm="4" lg="4" xl="4" class="text-center">
                <v-row justify="center">
                  <v-checkbox
                    v-model="wagner.sw"
                    label="Sword Install"
                    color="secondary"
                    flat
                    :readonly="loading"
                  />
                </v-row>
              </v-col>
              <v-col cols="6" md="4" sm="4" lg="4" xl="4" class="text-center">
                <v-row justify="center">
                  <v-checkbox
                    v-model="wagner.sh"
                    label="Shield Install"
                    color="secondary"
                    flat
                    :readonly="loading"
                  />
                </v-row>
              </v-col>
            </v-row>

            <v-row v-if="character == 'Chaos'" justify="center" class="mt-n10">
              <v-col md="2" class="text-center">
                <v-row justify="center">
                  <v-checkbox
                    v-model="chaos.azhi"
                    label="Azhi"
                    color="secondary"
                    flat
                    :readonly="loading"
                  />
                </v-row>
              </v-col>
            </v-row>

            <v-row class="mt-n8">
              <v-col>
                <v-text-field
                  v-model="notation"
                  color="secondary"
                  maxlength="140"
                  label="Notation (Optional)"
                  spellcheck="false"
                  :readonly="loading"
                  autocomplete="off"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-text-field
                  v-model="desc"
                  color="secondary"
                  maxlength="140"
                  label="Additional Notes (Optional)"
                  spellcheck="false"
                  :readonly="loading"
                  autocomplete="off"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <v-row justify="center" class="mt-4">
              <v-btn
                color="primary"
                class="self-text-center"
                :depressed="true"
                tile
                :ripple="false"
                @click="validate"
                :loading="loading"
                :disabled="loading"
              >
                Submit
              </v-btn>
            </v-row>
            <v-snackbar v-model="badtime" :timeout="8000" top>
              Error: Combo could not be posted
              <v-icon @click="badtime = false" color="error" small>
                mdi-close
              </v-icon>
            </v-snackbar>
          </v-form>
        </v-container>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import unibfilters from '@/components/UnibComboFilters.vue';

export default {
  name: 'unibcombopost',

  props: {
    tw: Boolean,
    yt: Boolean,
  },

  data() {
    return {
      twlink: '',
      ytlink: '',

      character: '',
      version: 'ST',
      starter: '',
      meter: '',
      cs: false,
      ch: false,
      pos: '',
      damage: '',

      notation: '',
      desc: '',

      valid: false,
      loading: false,
      badtime: false,

      path: 'unib/combos',

      characters: unibfilters.data().characters,
      versions: unibfilters.data().versions,
      starters: unibfilters.data().starters,
      screenpos: unibfilters.data().screenpos,
      eltnum: unibfilters.data().eltnum,
      chaos: unibfilters.data().chaos,
      wagner: unibfilters.data().wagner,

      rules: {
        required: value => !!value || 'Required Field',
        limit: value => (value >= 0 && value <= 13) || '0-13',
        ratio: value => value <= this.eltnum.bullets || 'More enhanced than bullets',
        meter: value => (value >= 0 && value <= 200) || 'Must be 0-200',

        twcheck: value =>
          /twitter.com/.test(value) ||
          new RegExp('http://t.co/').test(value) ||
          'Invalid Twitter URL',
        ytcheck: value =>
          /youtube.com/.test(value) ||
          new RegExp('https://youtu.be').test(value) ||
          'Invalid Youtube URL',
      },
    };
  },

  created() {
    this.eltnum.enh = 0;
    this.eltnum.bullets = 0;
    this.wagner.sw = false;
    this.wagner.sh = false;
    this.chaos.azhi = false;
  },

  methods: {
    postCreate() {
      const payload = {
        character: this.character,
        ver: this.version,
        damage: this.damage,
        cs: this.cs,
        ch: this.ch,
        ms: this.pos,
        starter: this.starter,
        meter: this.meter,
        pos: this.pos,
      };

      if (this.yt) {
        payload.yt = this.ytlink;
      } else if (this.tw) {
        payload.tw = this.twlink;
      }

      if (this.character === 'Eltnum') {
        payload.bullets = this.eltnum.bullets;
        payload.enh = this.eltnum.enh;
      } else if (this.character === 'Wagner') {
        payload.wSword = this.wagner.sw;
        payload.wShield = this.wagner.sh;
      } else if (this.character === 'Chaos') {
        payload.azhi = this.chaos.azhi;
      }

      if (!!this.notation) {
        payload.notation = this.notation;
      }

      if (!!this.desc) {
        payload.desc = this.desc;
      }

      console.log(payload);

      return payload;
    },

    postCombo() {
      this.loading = true;

      this.$http
        .post(this.path, this.postCreate(), { timeout: 30000 })
        .then(response => {
          this.$emit('close', false);
          this.$emit('success');
          this.reset();
          console.log(response);
        })
        .catch(error => {
          this.badtime = true;
          console.log(error);
          console.log(error.response);
        })
        .finally(() => (this.loading = false));
    },

    getStarters() {
      if (typeof this.starters[this.version][this.character] === 'undefined') {
        return [];
      }

      return this.starters[this.version][this.character].slice(1);
    },

    characterChange() {
      this.starter = '';
    },

    validate: function() {
      if (this.$refs.form.validate()) {
        this.postCombo();
      }
    },

    reset: function() {
      this.$refs.form.reset();
      this.version = 'ST';
      this.cs = false;
      this.ch = false;
      this.sw = false;
      this.sh = false;
      this.azhi = false;
    },
  },
};
</script>
