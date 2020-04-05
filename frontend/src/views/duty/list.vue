<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Duty'"
                    :headers="headers"
                    :addBtnLink="'dutyCreate'"
                    class="custom-table-adjust"
                    ref="dataTable"
                    :dateSearch="true"
                    :addButton="$root.is_access('Duty','create')"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.guard?props.data.guard.name:''}}</td>
                    <td>{{props.data.gate_no}}</td>
                    <td>{{props.data.from_time|moment('DD-MM-YYYY hh:mm A')}}</td>
                    <td>{{props.data.to_time|moment('DD-MM-YYYY hh:mm A')}}</td>
                    <td class="justify-center px-0 align-center">
                        <template v-if="$root.is_access('Duty','edit')">
                            <router-link :to="{name:'dutyEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Duty','delete')">
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
            url: 'ajax/duty/',
            headers: [
                {
                    text: 'Guard',
                    align: 'left',
                    value: 'guard__name'
                },
                {text: 'Gate No', value: 'gate_no'},
                {text: 'From Time', value: 'from_time'},
                {text: 'To Time', value: 'to_time'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/duty/delete/' + id).then(res => {
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