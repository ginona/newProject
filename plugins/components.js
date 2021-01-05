import Vue from 'vue'

// import Example from 'example'

// First import component and then add to Vue
// Vue.component('example', Example)

// Set global variables, rules and functions
Vue.mixin({
  data() {
    return {
      rulesGlobal: {
        user: [
          (v) => !!v || this.$t('rules.type_user'),
          (v) => !!v || this.$t('rules.type_email'),
          (v) => /.+@.+\..+/.test(v) || this.$t('rules.valid_email'),
        ],
        password: [
          (v) => !!v || this.$t('rules.type_password'),
          (v) => v.length >= 5 || '5 ' + this.$t('rules.min_chars'),
        ],
        passwordConfirm: [
          (v) => !!v || this.$t('rules.type_password'),
          (v) =>
            v === this.form.password || this.$t('rules.password_not_match'),
        ],
        email: [
          (v) => !!v || this.$t('rules.type_email'),
          (v) => /.+@.+\..+/.test(v) || this.$t('rules.valid_email'),
        ],
      },
      // Vuetify datatable variables
      itemsPerPageOrderList: [3, 5],
      itemsPerPageSetter: [10, 25, 50, -1],
      itemsPerPageSetterDialogs: [5, 7],
    }
  },
  // General methods
  methods: {
    cleanObject(obj) {
      Object.keys(obj).forEach(
        (key) =>
          (obj[key] === null || obj[key] === undefined) && delete obj[key]
      )
    },
    getYears() {
      return [...Array(3).keys()].map((i) => i + 2019)
    },
    getDate(text) {
      if (text) {
        const [year, month, day] = text.substring(0, 10).split('-')
        return `${day}/${month}/${year}`
      }

      return null
    },
    getTime(time) {
      return time.substring(0, 5)
    },
    getDateTime(text) {
      if (text) {
        const data = text.split(' ')
        const [year, month, day] = data[0].split('-')
        return `${day}/${month}/${year} ${data[1]}`
      }

      return null
    },
    parseDate(date) {
      if (!date) return null

      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    getUrl(url) {
      return `${this.$axios.defaults.baseURL.substring(
        0,
        this.$axios.defaults.baseURL.length - 3
      )}${url}`
    },
    generateUrl(url) {
      if (url.includes('http:') || url.includes('https:')) return url

      return `https://${url}`
    },
    copyObject(obj) {
      return JSON.parse(JSON.stringify(obj))
    },
  },
})
