export default {
    data: () => ({
        buildings: [],
        company: {
            status: 'Active'
        },
        buttonDisable: false

    }),
    created() {
        axios.get('/ajax/company/create').then(res => {
            this.buildings = res.data.building
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true;
                    axios.post('/ajax/company/store', {
                        company: this.company
                    }).then(res => {
                        this.$root.message(res.data),
                            this.company = {},
                            this.$validator.reset(),
                            this.buttonDisable = false

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'companyList'})
        }
    }
}