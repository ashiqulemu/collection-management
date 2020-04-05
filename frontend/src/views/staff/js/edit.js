export default {
    data: () => ({
        valid: true,
        staff: {},
        companies: [],
        buttonDisable: false,
        fingerPrintLoading: false,
    }),
    created() {
        this.getData()
    },

    methods: {
        getData() {
            axios.get('/ajax/staff/' + this.$route.params.id + '/edit').then(res => {
                this.companies = res.data.companies;
                this.staff = res.data.staff
                this.staff.company=this.staff.company.id
            })
        },
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true;
                    var data = new FormData();
                    var imagefile = document.querySelector('#image');
                    data.append("image", imagefile.files[0]);
                    for (var key in this.staff) {
                        data.append(key, this.staff[key])
                    }
                    axios.post('/ajax/staff/' + this.$route.params.id + '/update', data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }).then(res => {
                        this.$root.message(res.data),
                            this.staff = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'staffList'})

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'staffList'})
        },
        removeImage() {
            this.staff.profile_image = ''
        }
    }

}