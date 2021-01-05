<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <div class="text-center">
        <vuetify-logo />
      </div>
      <v-card v-for="test in tests.slice(0, 5)" :key="test.id" class="custom">
        <v-card-title class="headline">
          {{ test.title }}
        </v-card-title>
        <v-card-text>
          <p>
            {{ test.completed ? 'Completado' : 'Pendiente' }}
          </p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {
    VuetifyLogo,
  },
  // middleware: ['auth'],
  data() {
    return {
      greeting: 'Hello World',
    }
  },
  computed: {
    ...mapGetters({
      tests: 'tests/list',
    }),
  },
  watch: {},
  mounted() {
    this.$store.dispatch('tests/list')
  },
  methods: {},
}
</script>
