<template>
    <div>
        <v-toolbar flat color="white" class="mt-4">
                    <v-toolbar-title>{{role}} Permission List</v-toolbar-title>
        </v-toolbar>
        <v-simple-table dense :class="'ow-table'"
        >
            <template v-slot:default>
                <thead>
                <tr>
                    <th>Module</th>
                    <th>View</th>
                    <th>Add</th>
                    <th>Edit</th>
                    <th>Delete</th>
                    <th>Share</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in permissions">
                    <td>{{item.moduled}}</td>
                    <td>
                        <input type="checkbox" v-model="item.view_permission"
                               @change="updateRole(item.view_permission, item.id, 'view_permission')"/>
                    </td>
                    <td>
                        <input type="checkbox" v-model="item.create_permission"
                               @change="updateRole(item.create_permission, item.id, 'create_permission')"/>
                    </td>
                    <td>
                        <input type="checkbox" v-model="item.edit_permission"
                               @change="updateRole(item.edit_permission, item.id, 'edit_permission')"/>
                    </td>
                    <td>
                        <input type="checkbox" v-model="item.delete_permission"
                               @change="updateRole(item.delete_permission, item.id, 'delete_permission')"/>
                    </td>
                    <td>
                        <input type="checkbox" v-model="item.share_permission"
                               @change="updateRole(item.share_permission, item.id, 'share_permission')"/>
                    </td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>

    </div>
</template>
<script>
    export default {
        data() {
            return {
                permissions: [],
                roles:[],
                role:''
            }
        },
        created() {
            this.getData()
        },

        methods: {
            updateRole(item, id, field) {
                axios.patch('/ajax/role-permission/' + this.$route.params.id + '/update', {
                    id: id,
                    field: field,
                    value: item
                }).then(response => {
                    this.$root.message(response.data),
                    this.$store.dispatch('GET_USER_DATA')
                    this.getData()
                })
            },
            getData() {
                axios.get('/ajax/role-permission/' + this.$route.params.id + '/edit').then(res => {
                    this.permissions = res.data.result
                    this.roles = res.data.roles
                    this.role = this.roles.filter(d=>d.id==this.permissions[0].role_id)[0].name;
                })
            }
        }

    }
</script>
