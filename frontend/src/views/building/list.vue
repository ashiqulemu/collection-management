<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Building'"
                    :headers="headers"
                    :addBtnLink="'buildingCreate'"
                    :addButton="$root.is_access('Building','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.name}}</td>
                    <td class="justify-center px-0 align-center icon">
                        <template v-if="$root.is_access('Building','edit')">
                            <router-link :to="{name:'buildingEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Building','delete')">
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
            url: 'ajax/building/',
            headers: [
                {
                    text: 'Building Name',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/building/delete/' + id).then(res => {
                        this.$refs.dataTable.getData()
                        this.$root.message(res.data)
                    })
                }
            },
        }
    }
</script>