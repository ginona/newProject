export default function ({ store, redirect, $axios }) {
  // If the user is not authenticated
  if (!store.getters['users/isAuthenticated']) {
    return redirect('/login')
  } else {
    $axios.setToken(
      store.getters['users/token'],
      store.getters['users/token_type']
    )

    store.dispatch('roles/getRoles')
    store.dispatch('roles/getPermissions')

    store.dispatch('users/get').catch((error) => {
      if (error.response.status === 401) {
        store.dispatch('users/deleteTokenDevice')
        return redirect('/login')
      }
    })
  }
}
