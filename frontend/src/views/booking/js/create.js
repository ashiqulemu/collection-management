export default {
    data: () => ({
        buttonDisable: false,
        companies: [],
        booking: {
            name: "",
            date_time: "",
            mobile: "",
            note: '',
            company: '',
            guest_quantity: 1,
        },
    }),
    created() {
        axios.get('/ajax/booking/create').then(res => {
            this.companies = res.data.companies
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    this.booking.date_time=this.$moment(this.booking.date_time).format('YYYY-MM-DD HH:mm:ss')
                    axios.post('/ajax/booking/store', {
                        booking: this.booking,

                    }).then(res => {
                        this.$root.message(res.data),
                            this.booking = {
                                guest_quantity: 1,
                                date_time: new Date(),
                                mobile: null,
                                note: null,
                            },
                            this.$validator.reset(),
                            this.buttonDisable = false

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'bookingList'})
        },
        loadStates: _.debounce(function (event) {
            axios.get(`/ajax/company/get-company?name=${event.target.value}`).then(res => {
                this.companies = res.data.companies
            })
        }, 200)
    }
}
