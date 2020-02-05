<template>
  <div>
    <v-dialog v-model="active" max-width="300">
      <template v-slot:activator="{ on }">
        <v-icon v-on="on" size="30" color="grey darken-1">mdi-flag</v-icon>
      </template>
      <v-card>
        <v-card-title>
          Flag Post
          <v-spacer />
          <v-icon @click="active = !active" small color="error" :disabled="loading">
            mdi-close
          </v-icon>
        </v-card-title>

        <v-card-text>
          <v-container class="mt-n6">
            <v-row justify="start">
              <v-col>
                <v-radio-group v-model="reason" :mandatory="true" :disabled="loading">
                  <v-radio color="secondary" label="Irrelevant Content" value="Irrelevant" />
                  <v-radio
                    color="secondary"
                    label="Incorrect Information"
                    value="Incorrect"
                    class="mt-4"
                  />
                  <v-radio color="secondary" label="Broken Link" value="Broken" class="mt-4" />
                  <v-radio
                    color="secondary"
                    label="Duplicate Post"
                    value="Duplicate"
                    class="mt-4"
                  />
                </v-radio-group>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-btn
                color="primary"
                class="self-text-center"
                :depressed="true"
                tile
                @click="insertFlag()"
                :ripple="false"
                :loading="loading"
                :disabled="loading"
              >
                Submit
              </v-btn>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>

      <v-snackbar v-model="badtime" :timeout="5000" top>
        Error reporting flag
        <v-icon @click="badtime = false" color="error" small>
          mdi-close
        </v-icon>
      </v-snackbar>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'flagpost',

  props: {
    id: Number,
  },

  data() {
    return {
      active: false,
      reason: 'Irrelevant',
      loading: false,
      badtime: false,
      path: 'unib/combos/',
    };
  },

  methods: {
    insertFlag() {
      this.loading = true;

      this.$http
        .put(this.path, { id: this.id, flag: this.reason }, { timeout: 30000 })
        .then(response => {
          this.$emit('success');
          this.active = false;
        })
        .catch(error => {
          this.badtime = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>
