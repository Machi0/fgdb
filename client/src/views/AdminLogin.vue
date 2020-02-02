<template>
  <div>
    <v-text-field v-model="username" :type="'password'"></v-text-field>
    <v-text-field v-model="password" :type="'password'"></v-text-field>
    <v-btn @click="validate()" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      path: '/matrix/',
    };
  },

  methods: {
    validate() {
      this.$http
        .post(this.path, { username: this.username, password: this.password }, { timeout: 30000 })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
