<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Assign Role'"
                    :headers="headers"
                    :addBtnLink="'userCreate'"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.user?props.data.user.username:''}}</td>
                    <td>{{props.data.user?props.data.user.email:''}}</td>
                    <td>{{props.data.user?props.data.user.first_name:''}}</td>
                    <td>{{props.data.user?props.data.user.last_name:''}}</td>
                    <td>{{props.data.role?props.data.role.name:''}}</td>
                    <td class="justify-center layout px-0 align-center icon">
                        <a href="#" @click.prevent="openModal(props.data)">
                            <i class="mdi mdi-account-switch mr-2" title="Assign Role"></i>
                        </a>
                    </td>
                </template>
            </data-table>
            <v-row>
                <template>
                    <v-dialog v-model="dialog" persistent max-width="600">
                        <v-card>
                            <v-card-title class="headline">ASSIGN ROLE TO YOUR USER</v-card-title>
                            <hr>
                            <br>
                            <v-layout wrap class="mt-5">
                                <v-flex xs12 md1></v-flex>
                                <v-flex xs12 md5 class="px-1 m-2 ">
                                    <v-card-text>
                                        User : <span class="blue--text text--lighten-1">{{modalData.user?modalData.user.username:''}}
                                        {{modalData.user?modalData.user.first_name:''}}
                                        {{modalData.user?modalData.user.last_name:''}}
                                        </span>
                                    </v-card-text>
                                </v-flex>
                                <v-flex xs12 md4 class="px-1 m-2">
                                    <v-autocomplete
                                            v-model="role"
                                            :items="roles"
                                            label="role"
                                            v-validate="'required'"
                                            data-vv-name="role"
                                            item-text="name"
                                            :error-messages="errors.collect('role')"
                                            outlined
                                            class="required"
                                            return-object
                                    ></v-autocomplete>
                                </v-flex>
                                <v-flex xs12 md1></v-flex>
                            </v-layout>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="green darken-1" text @click="dialog = false">Close</v-btn>
                                <v-btn color="primary darken-1" text @click.prevent="doSubmit()"
                                       :disabled="buttonDisable">Submit
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </template>
            </v-row>

        </div>
    </div>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            url: 'ajax/role-user/get-role-user',
            role: {},
            roles: [],
            modalData: {},
            buttonDisable: false,
            headers: [
                {
                    text: 'Username',
                    align: 'left',
                    value: 'user__name'
                },
                {text: 'Email', value: 'user__owner'},
                {text: 'First Name', value: 'user__level'},
                {text: 'Last Name', value: 'user__email'},
                {text: 'Role', value: 'role__name'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        created() {
            axios.get('/ajax/role/get-role').then(res => {
                this.roles = res.data.roles
            })
        },
        methods: {
            openModal(data) {
                this.modalData = data
                this.role = data.role
                this.dialog = true
            },
            deleteItem(id) {
                // if (confirm('Are you sure you want to delete this')) {
                //     // axios.delete('ajax/account/delete/' + id).then(res => {
                //     //     this.$refs.dataTable.getData()
                //     //     this.$root.message(res.data)
                //     // })
                // }

            },
            doSubmit() {
                this.$validator.validateAll().then(value => {
                    if (value) {
                        this.buttonDisable = true
                        axios.post('/ajax/role-user/assign-role', {
                            role: this.role,
                            user: this.modalData.user
                        }).then(res => {
                            this.$root.message(res.data),
                                this.$validator.reset(),
                                this.buttonDisable = false
                            this.modalData = {}
                            this.role = {}
                            this.$refs.dataTable.getData()
                            this.dialog = false

                        }).catch(err => {
                            console.log(err)
                        })
                    }
                })
            }

        }

    }
</script>

<style scoped lang="scss">
    .v-card__title.headline {
        background: #282658;
        color: #fff;
        font-size: 15px !important;
    }
</style>