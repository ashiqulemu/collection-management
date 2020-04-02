export default {
        data: () => ({
            valid: true,
            name: '',
            unit: '',
            range: '',
        }),
        created(){
          axios.get('/ajax/tests/'+this.$route.params.id+'/edit').then(res=>{
                this.name=res.data.result[0].name
                this.unit=res.data.result[0].unit
                this.range=res.data.result[0].range
          })
        },

        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        axios.patch('/ajax/tests/'+this.$route.params.id+'/update', {
                            name: this.name,
                            unit: this.unit,
                            range: this.range,
                        }).then(res => {
                           this.$root.successMessage(res.data),
                               this.$router.push({name:'testsList'})
                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
            cancel() {
               this.$router.push({name:'testsList'})
            }
        }
    }