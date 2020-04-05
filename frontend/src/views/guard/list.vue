<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Guard'"
                    :headers="headers"
                    :addBtnLink="'guardCreate'"
                    :addButton="$root.is_access('Guard','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.guard_id}}</td>
                    <td>{{props.data.name}}</td>
                    <td>{{props.data.nid}}</td>
                    <td>{{props.data.mobile}}</td>
                    <td>{{props.data.rf_id}}</td>
                    <td class="justify-center px-0 align-center">
                        <template v-if="$root.is_access('Guard','edit')">
                            <router-link :to="{name:'guardEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Guard','delete')">
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
            url: 'ajax/guard/',
            headers: [
                {
                    text: 'Guard ID',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Name', value: 'name'},
                {text: 'NID', value: 'nid'},
                {text: 'Mobile', value: 'mobile'},
                {text: 'RFID', value: 'rf_id'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/guard/delete/' + id).then(res => {
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