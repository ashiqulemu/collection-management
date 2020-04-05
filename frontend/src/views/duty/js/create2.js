export default {
    data: () => ({
        valid: true,
        duty: {},
        guards: [],
        buttonDisable: false,
        fingerPrintLoading: false,
        menu: false,
        menu2: false,
        menu3: false,
        from_time: '',
        to_time: '',
        dates: [],
        dutyItem: [],
        submitBtn: false,
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
                    this.buttonDisable = true;
                    axios.post('/ajax/duty/multi-store', {
                        duty: this.duty,
                        dutyItem: this.dutyItem
                    }).then(res => {
                        this.$root.message(res.data),
                            this.duty = {};
                        this.dates = [];
                        this.dutyItem = [];
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
        },
        dutyItemCreate() {
            this.submitBtn = true;
            this.dutyItem = [],
                this.dates.forEach(d => {
                    let next_date = ''
                    next_date = new Date(new Date(d).getTime() + 24 * 60 * 60 * 1000).toISOString().substr(0, 10)
                    this.dutyItem.push(
                        {
                            gate: '',
                            date: d,
                            from_time: d + ' ' + this.from_time + ':00',
                            to_time: this.from_time.substr(0, 2) > this.to_time.substr(0, 2) ? (next_date + ' ' + this.to_time + ':00') : (d + ' ' + this.to_time + ':00'),
                        }
                    )
                })
        }
    }

}