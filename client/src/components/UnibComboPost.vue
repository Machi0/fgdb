<template>
    <div>
        <v-card-text class="mt-n6">
            <v-container v-if="tw===true">
                <v-form>
                    <v-row class="text-center" justify="center">
                        <v-col>
                            <v-text-field v-model="twlink" color="secondary" maxlength="200"
                            label="URL" :rules="[rules.required, rules.twcheck]"/>
                            <v-text-field/>
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

      characters: unibfilters.data().characters,

      rules: {
        required: value => !!value || 'Required Field',
        twcheck: value => value.includes('twitter.com') || 'Invalid Twitter URL',
      },
    };
  },
};
</script>
