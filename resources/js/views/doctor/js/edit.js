export default {
        data: () => ({
            valid: true,
            name: '',
            mobile:'',
            email:'',
            emailRules: [
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
        }),
        created(){
          axios.get('/ajax/doctor/'+this.$route.params.id+'/edit').then(res=>{
                this.name=res.data.result[0].name
                this.email=res.data.result[0].email
                this.mobile=res.data.result[0].mobile
          })
        },

        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        axios.patch('/ajax/doctor/'+this.$route.params.id+'/update', {
                            name: this.name,
                            email: this.email,
                            mobile: this.mobile,
                        }).then(res => {
                           this.$root.successMessage(res.data),
                               this.$router.push({name:'doctorList'})
                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
            cancel() {
               this.$router.push({name:'doctorList'})
            }
        }
    }