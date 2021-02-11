<template>
  <div>
    <v-row>
      <h3 class="my-10 ml-4 text-uppercase">History</h3>
    </v-row>
    <v-data-table :items-per-page="20" :headers="headers" :items="items">
      <template v-slot:item.actions="{ item }">
        <v-icon v-cloak @click="openDialog(item.path)">mdi-eye</v-icon>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog" persistent max-width="700" clas="border-alert">
      <v-card>
        <v-card-title class="justify-center text-center">
          <img src="~/assets/img/sauron-ico-red.png" width="50px" />
        </v-card-title>
        <v-card-text class="justify-center text-center">
          <img :src="src" />
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn color="red darken-1" text @click="dialog = false">
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
      src: '',
      headers: [
        { text: 'Camera Id', value: 'camera_id' },
        { text: 'Accuracy', value: 'accuracy' },
        { text: 'Date', value: 'date' },
        { text: 'Watch', value: 'actions' },
      ],
      items: [],
    }
  },
  mounted() {
    this.$axios
      .$get('/api/historial', {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then((result) => {
        this.items = result.data
      })
  },
  methods: {
    openDialog(path) {
      this.dialog = true
      this.src = 'http://localhost:5000/images/' + path
    },
  },
}
</script>
