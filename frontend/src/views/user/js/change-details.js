export default {
    name: "change-password",
    data() {
        return {
            user: {},
            buttonDisable: false
        }
    },
    created() {

    },
    computed: {
        isLoad() {
            this.user = this.$store.state.user
            this.user.status = this.user.is_active ? 'Active' : 'Inactive'
            if(this.user.hasOwnProperty('id')){
                return true
            }
        }
    },
    methods: {
        submit() {
            this.$validator.validateAll().then(value => {
                if (value) {
                    this.buttonDisable = true
                    axios.patch('/ajax/account/change-details', {
                        user: this.user
                    }).then(res => {
                        this.$root.message(res.data),
                            this.user = {},
                            this.$validator.reset(),
                            this.buttonDisable = false
                        this.$router.push({name: 'userShow'})

                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
    }

}