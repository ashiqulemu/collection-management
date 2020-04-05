export default {
    data: () => ({
        buttonDisable: false,
        companies: [],
        booking: {
            guest_quantity: 1,
            date_time: new Date(),
            mobile: null,
            note: null,
        },
    }),
    created() {
        axios.get('/ajax/booking/' + this.$route.params.id + '/edit').then(res => {
            this.companies = res.data.companies
            this.booking = res.data.booking
            if (res.data.booking.hasOwnProperty('date_time')) {
                this.booking.date_time = this.$moment(res.data.booking.date_time).format('YYYY-MM-DD HH:mm ')
            }

        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.booking.date_time = this.$moment(this.booking.date_time).format('YYYY-MM-DD HH:mm:ss')
                    this.buttonDisable = true
                    axios.patch('/ajax/booking/' + this.$route.params.id + '/update', {
                        booking: this.booking
                    }).then(res => {
                        this.$root.message(res.data),
                            this.booking = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'bookingList'})

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
    },

}