export default function ({ store, redirect }) {
  // If the user is authenticated
  if (store.getters['users/isAuthenticated']) {
    return redirect('/')
  }
}
