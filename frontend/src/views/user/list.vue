<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage User'"
                    :headers="headers"
                    :addBtnLink="'userCreate'"
                    :addButton="$root.is_access('User','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <template v-if="!props.data.is_superuser">
                        <td>{{props.data.user.username}}</td>
                        <td>{{props.data.user.email}}</td>
                        <td>{{props.data.user.first_name+' '+props.data.user.last_name}}</td>
                        <td>{{props.data.role.name}}</td>
                        <td>{{props.data.user.is_active?'Active':'Inactive'}}</td>
                        <td class="justify-center  px-0 align-center icon">
                            <template v-if="$root.is_access('User','edit')">
                                <router-link :to="{name:'userEdit',params:{id:props.data.user.id}}">
                                    <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                                </router-link>
                            </template>
                            <template v-if="$root.is_access('User','delete')">
                                <a @click="deleteItem(props.data.user.id)">
                                    <i title="Delete" class="mdi mdi-delete red--text"></i>
                                </a>
                            </template>
                        </td>
                    </template>

                </template>
            </data-table>
        </div>
    </div>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            url: 'ajax/account/',
            headers: [
                {
                    text: 'Username',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Email', value: 'owner'},
                {text: 'Name', value: 'first_name'},
                {text: 'Role', value: 'role'},
                {text: 'Status', value: 'status'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    if (confirm('If user has any company, then company will be deleted also with this company staff will be deleted. ')) {
                        if (confirm('Are you sure? ')) {
                            axios.delete('ajax/account/delete/' + id).then(res => {
                                this.$refs.dataTable.getData()
                                this.$root.message(res.data)
                            })
                        }
                    }

                }

            },

        }

    }
</script>

<style scoped>

</style>