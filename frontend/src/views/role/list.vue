<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Role & Permission'"
                    :headers="headers"
                    :addBtnLink="'roleCreate'"
                    :addButton="$root.is_access('Role-Permission','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>
                        <router-link :to="{name:'rolePermissionEdit', params:{id:props.data.id}}">
                            {{props.data.name}}
                        </router-link>
                    </td>
                    <td class="text-center" md2>
                        <router-link :to="{name:'rolePermissionEdit', params:{id:props.data.id}}">
                            <i class="mdi mdi-account-switch mr-2" title="Assign"></i>
                        </router-link>
                    </td>

                    <td class="justify-center px-0 align-center icon">


                        <template v-if="$root.is_access('Role-Permission','edit')">
                            <router-link :to="{name:'roleEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Role-Permission','delete')">
                            <a @click="deleteItem(props.data.id)">
                                <i title="Delete" class="mdi mdi-delete red--text"></i>
                            </a>
                        </template>
                    </td>
                </template>
            </data-table>
        </div>
    </div>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            url: '/ajax/role/',
            headers: [
                {
                    text: 'Role Name',
                    align: 'left',
                    value: 'name'
                },

                {text: 'Assign Permission', value: 'id', align: 'center' ,sortable: false},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    if (confirm('Sorry for re-check, Are you sure?')) {
                        axios.delete('ajax/role/' + id + '/delete').then(res => {
                            this.$refs.dataTable.getData()
                            this.$root.message(res.data)
                        })
                    }

                }

            },

        }

    }
</script>

<style scoped>

</style>