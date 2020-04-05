export default {
    data: () => ({
        valid: true,
        renderComponent: true,
        attendance: {
            type: 'Staff',
            status: 'Active',
            vehicle: 'No-vehicle',
            out_time: null,
            staff: {},
            note: null,
            booking_id: null,
            person_quantity: 1,
            out_gate_no: null,
            vehicle_quantity: null,

        },
        gateNos: ['Gate 1', 'Gate 2', 'Gate 3', 'Gate 4'],
        staffs: [],
        buttonDisable: false,
        fingerPrintLoading: false,
        staffsAndVisitor: []
    }),
    created() {
        this.attendance.in_time = this.$moment(new Date()).format('YYYY-MM-DD hh:mm')
        axios.get('/ajax/attendance/create').then(res => {
            this.staffsAndVisitor = res.data.staffs
            if (this.$route.params.id) {
                this.attendance.type = 'Visitor'
            }
            this.getName(this.attendance.type)
        })

        if (this.$route.params.id) {

            axios.get('/ajax/booking/' + this.$route.params.id + '/get-booking').then(res => {
                this.attendance.staff = res.data.booking
                this.attendance.person_quantity = res.data.booking ? res.data.booking.guest_quantity : 1
            })
        }


    },
    mounted() {
        if (this.$store.state.guard_data) {
            this.gateNos = []
            this.gateNos.push(this.$store.state.guard_data.gate_no)
            this.attendance.gate_no = this.$store.state.guard_data.gate_no
        }
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    if (this.attendance.type == 'Visitor') {
                        this.attendance.booking_id = this.attendance.staff ?
                            this.attendance.staff.id : null
                    }
                    this.attendance.in_time = this.$moment(this.attendance.in_time)
                    this.attendance.out_time = this.$moment(this.attendance.out_time)

                    axios.post('/ajax/attendance/store', {
                        attendance: this.attendance
                    }).then(res => {
                        this.$root.message(res.data),
                            this.attendance = {
                                type: 'Staff',
                                status: 'Active',
                                in_time: this.$moment(new Date()).format('YYYY-MM-DD hh:mm'),
                                person_quantity: 1,
                                vehicle: 'No-vehicle',
                                staff: {},
                                out_time: null,
                                booking_id: null,
                                note: null,
                                out_gate_no: null,
                                vehicle_quantity: null,
                            },
                            this.$validator.reset(),
                            this.getName(this.attendance.type)

                        this.buttonDisable = false
                        this.rerender()


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
            this.attendance.staff = null
            if (type == 'Staff') {
                this.staffs = this.staffsAndVisitor.filter(d => d.model_type == 'staff')
            } else if (type == 'Visitor') {
                this.staffs = this.staffsAndVisitor.filter(d => d.model_type == 'booking')
            }
        },
        setTimeNow() {
            this.attendance.out_time = ''
            this.attendance.out_time = this.$moment(new Date()).format('YYYY-MM-DD hh:mm')
        },
        rerender() {
            this.renderComponent = false;
            this.$nextTick(() => {
                this.renderComponent = true;
            });
        }
    }

}