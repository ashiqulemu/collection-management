export default {
    data: () => ({
        valid: true,
        staff: {
            status: 'Active'
        },
        companies: [],
        buttonDisable: false,
        fingerPrintLoading: false,
    }),
    created() {
        axios.get('/ajax/staff/create').then(res => {
            this.companies = res.data.companies
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true;
                    var data = new FormData();
                    var imagefile = document.querySelector('#image');
                    data.append("image", imagefile.files[0]);
                    for(var key in this.staff){
                        data.append(key,this.staff[key])
                    }
                    // data.append('staff', this.staff);
                    axios.post('/ajax/staff/store', data, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        },
                        body:data
                    }).then(res => {
                        this.$root.message(res.data),
                            this.staff = {
                                status: 'Active'
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
            this.$router.push({name: 'staffList'})
        }
    }

}