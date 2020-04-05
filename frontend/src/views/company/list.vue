<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Company'"
                    :headers="headers"
                    :addBtnLink="'companyCreate'"
                    :addButton="$root.is_access('Company','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.name}}</td>
                    <td>{{props.data.owner}}</td>
                    <td>{{props.data.authorize_person}}</td>
                    <td>{{props.data.building.name}}</td>
                    <td>{{props.data.email}}</td>
                    <td>{{props.data.mobile}}</td>
                    <td>{{props.data.status}}</td>
                    <td class="justify-center px-0 align-center icon">
                        <template v-if="$root.is_access('Company','edit')">
                            <router-link :to="{name:'companyEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Company','delete')">
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
            url: 'ajax/company/',
            headers: [
                {
                    text: 'Company Name',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Owner Name', value: 'owner'},
                {text: 'Authorizer', value: 'authorized_person'},
                {text: 'Level', value: 'building'},
                {text: 'Email', value: 'email'},
                {text: 'Mobile', value: 'mobile'},
                {text: 'Status', value: 'status'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/company/delete/' + id).then(res => {
                        this.$refs.dataTable.getData()
                        this.$root.message(res.data)
                    })
                }

            },

        }

    }
</script>

<style scoped>

</style>