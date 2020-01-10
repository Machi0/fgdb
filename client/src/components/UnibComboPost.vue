<template>
    <v-container>
        <v-row justify="center">
            <v-dialog v-model="post" persistent max-width="200">
                <template v-slot:activator="{ on }">
                    <v-icon color="secondary" v-on="on">mdi-plus-box</v-icon>
                </template>
                <v-card>
                    <v-card-title>
                        Upload
                        <v-spacer/>
                        <v-icon @click="post=!post" small color="error">
                            mdi-close
                        </v-icon>
                    </v-card-title>
                    <v-card-text>
                        <v-row class="text-center">
                            <v-col>
                                <v-icon color="blue" size="45">
                                    mdi-twitter
                                </v-icon>
                            </v-col>
                            <v-col>
                                <v-icon color="red darken-1" size="45">
                                    mdi-youtube
                                </v-icon>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-dialog>
        </v-row>
    </v-container>
</template>

<script>
import unibfilters from '@/components/UnibComboFilters.vue';

export default {
  name: 'unibcombopost',

  data() {
    return {
      post: false,
      yt: false,
      tw: false,

      characters: unibfilters.data().characters,
    };
  },
};
</script>
