 export default {
        data: () => ({

            role: {},
            buttonDisable: false

        }),
        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.post('/ajax/role/create', {
                            role: this.role
                        }).then(res => {
                            this.$root.message(res.data),
                                this.role = {},
                                this.$validator.reset(),
                                this.buttonDisable = false

                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
            cancel() {
                this.$router.push({name: 'roleList'})
            }
        }
    }