export default {
    data: () => ({
        user: {},
        roles: [],
        buttonDisable: false

    }),
    created() {
        axios.get('/ajax/account/' + this.$route.params.id + '/edit').then(res => {
            this.user = res.data.user.user
            this.user.role = res.data.user.role
            this.roles = res.data.roles
            this.user.status=res.data.user.is_active?'Active':'Inactive'
            this.user.password=null
        })
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.patch('/ajax/account/'+this.$route.params.id+'/update', {
                        user: this.user
                    }).then(res => {
                        this.$root.message(res.data),
                            this.user = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                            this.$router.push({name: 'userList'})

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        cancel() {
            this.$router.push({name: 'userList'})
        }
    }
}