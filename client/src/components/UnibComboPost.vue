<template>
    <v-container>
        <v-row justify="center">
            <v-dialog v-model="post" max-width="200">
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
                        <v-container>
                            <v-row class="text-center">
                                <v-col>
                                    <v-dialog v-model="tw" max-width="600"
                                    transition="fade-transition" persistent>
                                        <template v-slot:activator="{ on }">
                                            <v-icon color="blue"
                                            @click="tw=!tw, post=!post" size="45">
                                                mdi-twitter
                                            </v-icon>
                                        </template>
                                        <v-card>
                                            <v-card-title>
                                                Upload Twitter Post
                                                <v-spacer/>
                                                <v-icon @click="tw=!tw" small color="error">
                                                    mdi-close
                                                </v-icon>
                                            </v-card-title>
                                                <v-card-text>
                                                    <v-container>
                                                        <v-row class="text-center">
                                                            <v-col>
                                                                <v-text-field>
                                                                </v-text-field>
                                                            </v-col>
                                                        </v-row>
                                                    </v-container>
                                                </v-card-text>
                                        </v-card>
                                    </v-dialog>
                                </v-col>
                                <v-col>
                                    <v-icon color="red darken-1" size="45">
                                        mdi-youtube
                                    </v-icon>
                                </v-col>
                            </v-row>
                        </v-container>
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
      tw: false,
      yt: false,

      characters: unibfilters.data().characters,
    };
  },
};
</script>
