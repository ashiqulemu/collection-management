<template>
    <v-form>
        <v-layout row wrap class="formBox">
            <v-flex xs12 md5>
                <div class="changePassArea">
                    <h3 class="passTitle">Change Password !</h3>
                    <v-text-field
                            label="Existing password"
                            v-validate="'required'"
                            data-vv-name="existing_password"
                            v-model="existing_password"
                            required
                            :error-messages="errors.collect('existing_password')"
                            class="required mt-5"
                            outlined
                            :type="'password'"

                    ></v-text-field>
                    <v-text-field
                            label="New password"
                            v-validate="'required|min:6'"
                            data-vv-name="new_password"
                            v-model="new_password"
                            :error-messages="errors.collect('new_password')"
                            required
                            ref="password"
                            class="required"
                            outlined
                            :type="'password'"
                    ></v-text-field>
                    <v-text-field
                            label="Retype New password"
                            data-vv-name="confirm_password"
                            required
                            v-validate="'required|confirmed:password|min:6'"
                            :error-messages="errors.collect('confirm_password')"
                            v-model="confirm_password"
                            class="required"
                            outlined
                            :type="'password'"
                    ></v-text-field>
                    <v-btn class="" tile color="success" @click.prevent="submit()" :disabled="buttonDisable">
                        Change Now!
                    </v-btn>
                </div>
            </v-flex>
            <v-flex xs12 md6>
                <img src="../../../public/images/undraw_authentication_fsn5.svg" class="changePass"
                     alt="change password"
                     width="100%">
            </v-flex>
        </v-layout>
    </v-form>
</template>

<script>
    export default {
        name: "change-password",
        data() {
            return {
                existing_password: '',
                new_password: '',
                confirm_password: '',
                buttonDisable: false,
            }
        },
        methods: {
            submit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.post('/ajax/account/change-password', {
                            existing_password: this.existing_password,
                            new_password: this.new_password,
                            confirm_password: this.confirm_password
                        }).then(res => {
                            this.$root.message(res.data),
                                this.existing_password = '',
                                this.new_password = '',
                                this.confirm_password = '',
                                this.$validator.reset(),
                                this.buttonDisable = false
                            if (res.data.type == 'success') {
                                window.location.reload()
                            }


                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            },
        }
    }
</script>

<style scoped lang="scss">

    .formBox {
        padding: 20px;
    }

</style>