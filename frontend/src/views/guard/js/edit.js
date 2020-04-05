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
       created() {
            this.getData()
        },
        methods: {
             getData() {
                axios.get('/ajax/guard/' + this.$route.params.id + '/edit').then(res => {
                    this.guard = res.data.result
                })
            },
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                       axios.patch('/ajax/guard/' + this.$route.params.id + '/update', {
                            guard: this.guard
                        }).then(res => {
                            this.$root.message(res.data),
                             this.guard = {}
                            this.$validator.reset()
                            this.buttonDisable = false
                            this.$router.push({name: 'guardList'})

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