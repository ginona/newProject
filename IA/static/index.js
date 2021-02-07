const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        loading: false,
        selection: 1,  
    },
    methods: {
        reserve () {
            this.loading = true

            setTimeout(() => (this.loading = false), 2000)
        },
    }
})