export const state = {
  version: 1,
  list: [],
}

export const getters = {
  list(state) {
    return state.list
  },
}

export const actions = {
  list({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios.get('https://jsonplaceholder.typicode.com/todos').then(
        (result) => {
          commit('setList', result.data)
          resolve(result.data)
        },
        (error) => {
          reject(error)
        }
      )
    })
  },
}

export const mutations = {
  setList(state, payload) {
    state.list = payload
  },
}
