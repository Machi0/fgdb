<template>
  <v-container px-12>
    <v-row v-if="loading === false" justify="center">
      <v-card
        v-for="(post, index) in posts"
        :key="index"
        outlined
        tile
        width="290"
        class="mx-4 mb-6"
      >
        <v-card-title class="my-n2">
          <v-img
            :src="require('@/assets/unib/' + post.character + '.png')"
            alt="Character Portrait"
            contain
            max-width="35"
          />
          <v-spacer />
          <v-icon v-if="'tw' in post" color="blue" size="30">mdi-twitter</v-icon>
          <v-icon v-else color="red darken-1" size="30">mdi-youtube</v-icon>
          <v-spacer />
          <v-icon size="30" color="grey darken-1">mdi-flag</v-icon>
        </v-card-title>
        <v-divider />
        <v-card-text>
          <v-row>
            <v-col>
              <div>Starter:</div>
              <div class="mt-1">Damage:</div>
              <div class="mt-1">Meter:</div>
              <div class="mt-1">Counter Hit:</div>
              <div class="mt-1">Vorpal:</div>
              <div class="mt-1" v-if="'bullets' in post">Bullets:</div>
              <div v-if="'enh' in post" class="mt-1">Enhanced:</div>
              <div v-if="'wSword' in post" class="mt-1">Sword Install:</div>
              <div v-if="'wShield' in post" class="mt-1">Shield Install:</div>
              <div v-if="'azhi' in post" class="mt-1">Azhi:</div>
            </v-col>
            <v-spacer class="ml-n12" />

            <v-col class="text-end">
              <div>{{ post.starter }}</div>
              <div class="mt-1">{{ post.damage }}</div>
              <div class="mt-1">{{ post.meter }}</div>
              <div>
                <v-icon v-if="post.ch" size="18" color="green" class="mt-1">mdi-check</v-icon>
                <v-icon v-else size="16" color="red darken-1" class="mt-1">mdi-close</v-icon>
              </div>
              <div>
                <v-icon v-if="post.cs" size="18" color="green" class="mt-1">mdi-check</v-icon>
                <v-icon v-else size="16" color="red darken-1" class="mt-1">mdi-close</v-icon>
              </div>
              <div v-if="'bullets' in post" class="mt-1">{{ post.bullets }}</div>
              <div v-if="'enh' in post" class="mt-1">{{ post.enh }}</div>
              <div v-if="'wSword' in post">
                <v-icon v-if="post.wSword" class="mt-1" size="18" color="green">mdi-check</v-icon>
                <v-icon v-else size="16" class="mt-1" color="red darken-1">mdi-close</v-icon>
              </div>
              <div v-if="'wShield' in post">
                <v-icon v-if="post.wShield" size="18" class="mt-1" color="green">mdi-check</v-icon>
                <v-icon v-else size="16" color="red darken-1" class="mt-1">mdi-close</v-icon>
              </div>
              <div v-if="'azhi' in post">
                <v-icon v-if="post.azhi" size="18" color="green" class="mt-1">mdi-check</v-icon>
                <v-icon v-else size="16" color="red darken-1" class="mt-1">mdi-close</v-icon>
              </div>
            </v-col>
          </v-row>

          <v-row v-if="'notation' in post" justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>Notation: {{ post.notation }}</div>
            </v-col>
          </v-row>
          <v-row v-if="'desc' in post" justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>Notes: {{ post.desc }}</div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-row>

    <v-row v-else justify="center" align="center">
      <v-progress-circular color="primary" indeterminate size="50" />
    </v-row>

    <v-row justify="center" class="mt-6">
      <v-pagination circle v-model="page" :total-visible="8" :length="totalPages" color="primary" />
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'getcombos',

  data() {
    return {
      page: 1,
      totalPages: 1,
      posts: [],
      path: 'unib/combos',
      loading: true,
    };
  },

  created() {
    this.getPosts();
  },

  methods: {
    getPosts() {
      this.loading = true;

      this.$http
        .get(this.path)
        .then(response => {
          console.log(response.data.items);
          this.totalPages = response.data._meta.total_pages;
          this.posts = response.data.items;
        })
        .catch(error => {
          console.error(error);
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>
