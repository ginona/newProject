export default function ({
  isHMR,
  app,
  store,
  route,
  params,
  error,
  redirect,
}) {
  const locale = store.state.users.locale
  if (store.state.users.user && store.state.users.locales.length) {
    const userLocale = store.state.users.locales.find(
      (x) => x.cod === store.state.users.user.country_id
    )
    if (userLocale) {
      app.i18n.locale = locale || userLocale.locale
    }
  } else {
    app.i18n.locale = store.state.users.locale
  }
}
