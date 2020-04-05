export default {
    data: () => ({
        building: {},
        buttonDisable: false

    }),
    created() {
        this.getData()
    },
    methods: {
        getData() {
            axios.get('/ajax/building/' + this.$route.params.id + '/edit').then(res => {
                this.building = res.data.result
            })
        },
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.patch('/ajax/building/' + this.$route.params.id + '/update', {
                        building: this.building
                    }).then(res => {
                        this.$root.message(res.data),
                            this.building = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'buildingList'})

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