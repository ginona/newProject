import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

export default ({ app, store }) => {
  // Set i18n instance on app
  // This way we can use it in middleware and pages asyncData/fetch

  // Dinamic locale with store
  // let locale = store.state.users.locale

  // if (store.state.users.user && store.state.users.locales.length) {
  //   const userLocale = store.state.users.locales.find(
  //     (x) => x.cod === store.state.users.user.country_id
  //   )

  //   if (userLocale) {
  //     locale = locale || userLocale.locale
  //   }
  // }

  app.i18n = new VueI18n({
    locale: 'es',
    messages: {
      es: require('~/locales/es.json'),
    },
  })

  app.i18n.path = (link) => {
    if (app.i18n.locale === app.i18n.fallbackLocale) {
      return `/${link}`
    }

    return `/${app.i18n.locale}/${link}`
  }
}
