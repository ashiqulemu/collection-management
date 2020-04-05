export default {
    data: () => ({
        buildings: [],
        company: {},
        buttonDisable: false
    }),
    created() {
        this.getData()
    },
    methods: {
        getData() {
            axios.get('/ajax/company/' + this.$route.params.id + '/edit').then(res => {
                this.company = res.data.result;
                this.company.building=res.data.result.building_id
                this.building = res.data.building;
            })
        },
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.patch('/ajax/company/' + this.$route.params.id + '/update', {
                        company: this.company
                    }).then(res => {
                        this.$root.message(res.data),
                            this.company = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'companyList'})

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