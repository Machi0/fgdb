<template>
  <div>
    <v-card-text class="mt-n6">
      <v-container>
        <v-form>
          <v-row class="text-center" justify="center">
            <v-col v-if="tw === true">
              <v-text-field
                v-model="twlink"
                color="secondary"
                maxlength="200"
                label="URL"
                :rules="[rules.required, rules.twcheck]"
                spellcheck="false"
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
              />
            </v-col>
          </v-row>

          <v-row class="text-center" justify="center">
            <v-col cols="3">
              <v-select
                v-model="version"
                :items="versions"
                label="Version"
                item-color="secondary"
                color="secondary"
                :rules="[rules.required]"
              />
            </v-col>
            <v-col>
              <v-autocomplete
                v-model="character"
                @change="characterChange()"
                :items="characters[version].slice(1)"
                :rules="[rules.required]"
                label="Character"
                item-color="secondary"
                color="secondary"
                spellcheck="false"
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
              />
            </v-col>
          </v-row>

          <v-row v-if="character == 'Eltnum'" justify="center" class="mb-n6">
            <v-col cols="2" />
            <v-col md="2">
              <v-text-field
                v-model="eltnum.bullets"
                color="secondary"
                label="Bullets"
                :rules="[rules.required, rules.limit]"
                maxlength="2"
                dense
              />
            </v-col>
            <v-col md="2">
              <v-text-field
                v-model="eltnum.enh"
                color="secondary"
                label="Enhanced"
                :rules="[rules.required, rules.limit]"
                maxlength="2"
                dense
              />
            </v-col>
            <v-col cols="2" />
          </v-row>

          <v-row v-if="character == 'Wagner'" justify="center" class="mb-n5">
            <v-col md="4" class="text-center">
              <v-row justify="center">
                <v-checkbox
                  v-model="wagner.sw"
                  label="Sword Install"
                  color="secondary"
                  ripple="false"
                  flat
                />
              </v-row>
            </v-col>
            <v-col md="4" class="text-center">
              <v-row justify="center">
                <v-checkbox
                  v-model="wagner.sh"
                  label="Shield Install"
                  color="secondary"
                  ripple="false"
                  flat
                />
              </v-row>
            </v-col>
          </v-row>

          <v-row v-if="character == 'Chaos'" justify="center" class="mb-n5">
            <v-col md="2" class="text-center">
              <v-row justify="center">
                <v-checkbox
                  v-model="chaos.azhi"
                  label="Azhi"
                  color="secondary"
                  ripple="false"
                  flat
                />
              </v-row>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field
                v-model="notation"
                color="secondary"
                maxlength="140"
                label="Notation (Optional)"
                spellcheck="false"
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
              >
              </v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </v-card-text>
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

      notation: '',
      desc: '',

      characters: unibfilters.data().characters,
      versions: unibfilters.data().versions,
      starters: unibfilters.data().starters,
      eltnum: unibfilters.data().eltnum,
      chaos: unibfilters.data().chaos,
      wagner: unibfilters.data().wagner,

      rules: {
        required: value => !!value || 'Required Field',
        limit: value => (value >= 0 && value <= 13) || '0-13',

        twcheck: value =>
          value.includes('twitter.com') || value.includes('http://t.co') || 'Invalid Twitter URL',
        ytcheck: value =>
          value.includes('youtube.com') ||
          value.includes('https://youtu.be') ||
          'Invalid Youtube Url',
      },
    };
  },

  methods: {
    getStarters() {
      if (typeof this.starters[this.version][this.character] === 'undefined') {
        return [];
      }

      return this.starters[this.version][this.character].slice(1);
    },
  },
};
</script>
