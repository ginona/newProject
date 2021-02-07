<template>
  <div>
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
        { text: 'ID Cámara', value: 'camera_id' },
        { text: 'Precisión', value: 'accuracy' },
        { text: 'Fecha', value: 'date' },
        { text: 'Ver', value: 'actions' },
      ],
      items: [],
    }
  },
  mounted() {
    this.$axios
      .get('historial', {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then((result) => {
        // eslint-disable-next-line no-console
        console.log(result.data.data)

        this.items = result.data.data
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
