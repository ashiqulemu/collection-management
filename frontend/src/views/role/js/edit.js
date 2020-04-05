export default {
        data: () => ({
            role: {},
            buttonDisable: false

        }),
        created() {
            this.getData()
        },
        methods: {
            getData() {
                axios.get('/ajax/role/' + this.$route.params.id + '/edit').then(res => {
                    this.role = res.data.result
                })
            },
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.patch('/ajax/role/' + this.$route.params.id + '/update', {
                            role: this.role
                        }).then(res => {
                            this.$root.message(res.data),
                                this.role = {},
                                this.$validator.reset(),
                                this.buttonDisable = false
                            this.$router.push({name: 'roleList'})

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