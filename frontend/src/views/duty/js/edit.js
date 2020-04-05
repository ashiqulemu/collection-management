export default {
    data: () => ({
        valid: true,
        duty: {},
        guards: [],
        buttonDisable: false,
        fingerPrintLoading: false,
    }),
    created() {
        axios.get('/ajax/duty/'+this.$route.params.id+'/edit').then(res => {
            this.guards = res.data.guards;
            this.duty=res.data.duty;
            if (res.data.duty.hasOwnProperty('from_time')) {
                this.duty.from_time = this.$moment(res.data.duty.from_time).format('YYYY-MM-DD hh:mm')
            }
             if (res.data.duty.hasOwnProperty('to_time')) {
                this.duty.to_time = this.$moment(res.data.duty.to_time).format('YYYY-MM-DD hh:mm')
            }

        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true;
                    this.duty.from_time = this.$moment(this.duty.from_time);
                    this.duty.to_time = this.$moment(this.duty.to_time);
                    axios.patch('/ajax/duty/'+this.$route.params.id+'/update', {
                        duty: this.duty
                    }).then(res => {
                        this.$root.message(res.data),
                            this.duty = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                            this.$router.push({name: 'dutyList'})

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