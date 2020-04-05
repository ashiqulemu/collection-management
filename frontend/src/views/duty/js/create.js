export default {
    data: () => ({
        valid: true,
        duty: {},
        guards: [],
        buttonDisable: false,
        fingerPrintLoading: false,
    }),
    created() {
        axios.get('/ajax/duty/create').then(res => {
            this.guards = res.data.guards
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.post('/ajax/duty/store', {
                        duty: this.duty
                    }).then(res => {
                        this.$root.message(res.data),
                            this.duty = {},
                            this.$validator.reset(),
                            this.buttonDisable = false

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'dutyList'})
        }
    }

}