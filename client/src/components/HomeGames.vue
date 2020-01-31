<template>
  <v-container px-12>
    <v-row justify="center">
      <v-col>
        <div class="headline font-weight-bold">GAMES</div>
        <v-divider class="mb-3 mt-1 white" />
        <v-row>
          <v-spacer class="hidden-sm-and-up" />
          <v-col>
            <v-card width="210" href="/unib/combos" flat hover>
              <v-img src="@/assets/unibcover.png" contain width="210" />
            </v-card>
          </v-col>
          <v-spacer class="hidden-sm-and-up" />
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'gamelist',
};
</script>
