 export default {
        data: () => ({
            building:{},
            buttonDisable: false

        }),
        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.post('/ajax/building/store', {
                            building: this.building
                        }).then(res => {
                            this.$root.message(res.data),
                                this.building = {},
                                this.$validator.reset(),
                                this.buttonDisable = false

                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
            cancel() {
                this.$router.push({name: 'buildingList'})
            }
        }
    }