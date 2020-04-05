export default {
    data: () => ({
        user: {
            status:'Active'
        },
        roles: [],
        buttonDisable: false

    }),
    created() {
        axios.get('/ajax/account/create').then(res => {
            this.roles = res.data.roles
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.post('/ajax/account/store', {
                        user: this.user
                    }).then(res => {
                        this.$root.message(res.data),
                            this.user = {status:'Active'},
                            this.$validator.reset(),
                            this.buttonDisable = false

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'userList'})
        }
    }
}