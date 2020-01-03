<template>
    <v-container>
        <v-layout text-center>
            <v-flex>
                <v-btn @click="p=!p"></v-btn>
                <br/>
                <span>{{ p }}</span>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>

export default {
  data() {
    return {
      p: true,
    };
  },
  created() {
    this.$vue.navbar = '#311B92';
  },
};
</script>
