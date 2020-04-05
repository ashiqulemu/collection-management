<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Employee'"
                    :headers="headers"
                    :addBtnLink="'staffCreate'"
                    :addButton="$root.is_access('Staff','create')"
                    :companySearch="true"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.staff_id}}</td>
                    <td>{{props.data.name}}</td>
                    <td>{{props.data.company?props.data.company.name:''}}</td>
                    <td>{{props.data.mobile}}</td>
                    <td>{{props.data.rf_id}}</td>
                    <td class="justify-center px-0 align-center">
                        <template v-if="$root.is_access('Staff','edit')">
                            <router-link :to="{name:'staffEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Staff','delete')">
                            <i @click="deleteItem(props.data.id)" title="Delete" class="mdi mdi-delete red--text"></i>
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
            url: 'ajax/staff/',
            headers: [
                {
                    text: 'Employee ID',
                    align: 'left',
                    value: 'staff_id'
                },
                {text: 'Name', value: 'name'},
                {text: 'Company Name', value: 'company__name'},
                {text: 'Mobile', value: 'mobile'},
                {text: 'RF ID', value: 'rf_id'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/staff/delete/' + id).then(res => {
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