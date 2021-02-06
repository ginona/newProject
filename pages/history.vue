<template>
  <v-data-table :items-per-page="20" :headers="headers" :items="items">
  </v-data-table>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        { text: 'ID Cámara', value: 'camera_id' },
        { text: 'Precisión', value: 'accuracy' },
        { text: 'Fecha', value: 'date' },
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
}
</script>
