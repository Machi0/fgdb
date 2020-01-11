<template>
    <div>
        <v-card-text class="mt-n6">
            <v-container>
                <v-form>
                    <v-row class="text-center" justify="center">
                        <v-col v-if="tw===true">
                            <v-text-field v-model="twlink" color="secondary" maxlength="200"
                            label="URL" :rules="[rules.required, rules.twcheck]"/>
                        </v-col>
                    </v-row>

                    <v-row class="text-center" justify="center">
                        <v-col cols="3">
                            <v-select v-model="version" :items="versions"
                            label="Version" item-color="secondary" color="secondary"
                            :rules="[rules.required]"/>
                        </v-col>
                        <v-col>
                            <v-autocomplete v-model="character" @change="characterChange()"
                            :items="characters[version].slice(1)" :rules="[rules.required]"
                            label="Character" item-color="secondary" color="secondary"/>
                        </v-col>
                    </v-row>

                    <v-row class="text-center" justify="center">
                        <v-col>
                            <v-autocomplete v-model="starter"
                            :items="getStarters()" :rules="[rules.required]"
                            label="Starter" item-color="secondary" color="secondary"/>
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

      characters: unibfilters.data().characters,
      versions: unibfilters.data().versions,
      starters: unibfilters.data().starters,

      rules: {
        required: value => !!value || 'Required Field',
        twcheck: value => value.includes('twitter.com') || 'Invalid Twitter URL',
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
