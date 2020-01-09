<template>
    <v-container>
        <v-row justify="center">
            <v-dialog v-model="post" persistent max-width="200">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" v-on="on">mdi-domain</v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        Website
                    </v-card-title>
                    <v-card-text>
                        <v-row>
                            <v-btn @click="post=!post"/>
                            {{ characters.ST }}
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
      characters: unibfilters.data().characters,
    };
  },
};
</script>
