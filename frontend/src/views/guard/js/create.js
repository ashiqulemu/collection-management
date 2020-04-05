  export default {
        data: () => ({
            valid: true,
            guard: {
                status:'Active'
            },
            buttonDisable: false,
            menu1: false,
            fingerPrintLoading: false,

        }),
        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.post('/ajax/guard/create', {
                            guard: this.guard
                        }).then(res => {
                            this.$root.message(res.data),
                                this.guard = {}
                            this.$validator.reset()
                            this.buttonDisable = false

                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
            cancel() {
                this.$router.push({name: 'guardList'})
            }
        }
    }