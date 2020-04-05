export default {
    data: () => ({
        valid: true,
        attendance: {},
        staffs: [],
        buttonDisable: false,
        fingerPrintLoading: false,
        staffsAndVisitor: [],
        count: 0,
    }),
    created() {
        axios.get('/ajax/attendance/' + this.$route.params.id + '/edit').then(res => {
            this.staffsAndVisitor = res.data.staffs
            this.attendance = res.data.attendance
            this.getName(this.attendance.type)
            if (this.attendance.booking) {
                this.attendance.staff = this.attendance.booking
            }

            if (res.data.attendance.hasOwnProperty('in_time')) {
                this.attendance.in_time = this.$moment(res.data.attendance.in_time).format('YYYY-MM-DD hh:mm')
            }
            if (res.data.attendance.hasOwnProperty('out_time')) {
                if (res.data.attendance.out_time) {
                    this.attendance.out_time = this.$moment(res.data.attendance.out_time).format('YYYY-MM-DD hh:mm')
                } else {
                    this.attendance.out_time = null
                }

            }


        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    this.attendance.in_time = this.$moment(this.attendance.in_time)
                    this.attendance.out_time = this.$moment(this.attendance.out_time)
                    axios.patch('/ajax/attendance/' + this.$route.params.id + '/update', {
                        attendance: this.attendance
                    }).then(res => {
                        this.$root.message(res.data),
                            this.attendance = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'attendanceList'})

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'attendanceList'})
        },
        getName(type) {
            if (this.count > 0) {
                this.attendance.staff = {}
            }
            if (type == 'Staff') {
                this.staffs = this.staffsAndVisitor.filter(d => d.model_type == 'staff')
            } else if (type == 'Visitor') {
                this.staffs = this.staffsAndVisitor.filter(d => d.model_type == 'booking')
            }
            this.count++
        },
        setTimeNow() {
            this.attendance.out_time = ''
            this.attendance.out_time = this.$moment(new Date()).format('YYYY-MM-DD hh:mm')
        }
    }

}