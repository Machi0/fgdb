<template>
  <v-container px-12>
    <v-row justify="center">
      <v-card outlined tile width="290" class="mx-4 mb-6">
        <v-card-title class="my-n2">
          <v-img src="@/assets/unib/Eltnum.png" alt="Eltnum" contain max-width="35" />
          <v-spacer />
          <v-icon color="blue" size="30">mdi-twitter</v-icon>
          <v-spacer />
          <v-icon size="30" color="grey darken-1">mdi-flag</v-icon>
        </v-card-title>
        <v-divider />
        <v-card-text>
          <v-row>
            <v-col>
              <div>Starter:</div>
              <div>Damage:</div>
              <div>Meter:</div>
              <div>Vorpal:</div>
              <div>Counter Hit:</div>
              <div>Bullets:</div>
              <div>Enhanced:</div>
            </v-col>
            <v-spacer />
            <v-col class="text-end">
              <div>236B</div>
              <div>1000</div>
              <div>200</div>
              <div>Vorpal</div>
              <div>CH</div>
              <div>32</div>
              <div>42</div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notation: fassssssssssssssf
              </div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notes: Doesn't work on Linne
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-card outlined tile width="290" class="mx-4 mb-6">
        <v-card-title class="my-n2">
          <v-img src="@/assets/unib/Eltnum.png" alt="Eltnum" contain max-width="35" />
          <v-spacer />
          <v-icon color="blue" size="30">mdi-twitter</v-icon>
          <v-spacer />
          <v-icon size="30" color="grey darken-1">mdi-flag</v-icon>
        </v-card-title>
        <v-divider />
        <v-card-text>
          <v-row>
            <v-col>
              <div>Starter:</div>
              <div>Damage:</div>
              <div>Meter:</div>
              <div>Vorpal:</div>
              <div>Counter Hit:</div>
              <div>Bullets:</div>
              <div>Enhanced:</div>
            </v-col>
            <v-spacer />
            <v-col class="text-end">
              <div>236B</div>
              <div>1000</div>
              <div>200</div>
              <div>Vorpal</div>
              <div>CH</div>
              <div>32</div>
              <div>42</div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notation: fassssssssssssssf
              </div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notes: Doesn't work on Linne
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-card outlined tile width="290" class="mx-4 mb-6">
        <v-card-title class="my-n2">
          <v-img src="@/assets/unib/Eltnum.png" alt="Eltnum" contain max-width="35" />
          <v-spacer />
          <v-icon color="blue" size="30">mdi-twitter</v-icon>
          <v-spacer />
          <v-icon size="30" color="grey darken-1">mdi-flag</v-icon>
        </v-card-title>
        <v-divider />
        <v-card-text>
          <v-row>
            <v-col>
              <div>Starter:</div>
              <div>Damage:</div>
              <div>Meter:</div>
              <div>Vorpal:</div>
              <div>Counter Hit:</div>
              <div>Bullets:</div>
              <div>Enhanced:</div>
            </v-col>
            <v-spacer />
            <v-col class="text-end">
              <div>236B</div>
              <div>1000</div>
              <div>200</div>
              <div>Vorpal</div>
              <div>CH</div>
              <div>32</div>
              <div>42</div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notation: fassssssssssssssf
              </div>
            </v-col>
          </v-row>
          <v-row justify="center" class="mt-n3">
            <v-col class="text-center caption">
              <div>
                Notes: Doesn't work on Linne
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-row>
    <v-row justify="center" class="mt-6">
      <v-pagination circle v-model="page" :total-visible="8" :length="100" color="primary" />
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'getcombos',

  data() {
    return {
      page: 1,
    };
  },
};
</script>
