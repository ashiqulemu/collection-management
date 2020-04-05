<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Visitor Booking'"
                    :headers="headers"
                    :addBtnLink="'bookingCreate'"
                    :addButton="$root.is_access('Booking','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
                    :dateSearch="true"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.name}}</td>
                    <td>{{props.data.company?props.data.company.name:''}}</td>
                    <td>{{props.data.mobile}}</td>
                    <td>{{props.data.guest_quantity}}</td>
                    <td>
                        <template v-if="props.data.date_time">
                            {{props.data.date_time|moment('DD-MM-YYYY hh:mm A')}}
                        </template>
                        <template v-else>
                            {{props.data.date_time}}
                        </template>
                    </td>
                    <td>{{props.data.is_attendance?'Visited':'Not Visited Yet'}}</td>
                    <td>{{props.data.note}}</td>
                    <td>{{getEntityBy(props.data)}}</td>
                    <td class="justify-center px-0 align-center icon">
                        <!--                        <template v-if="!props.data.is_attendance">-->
                        <!--                            <router-link :to="{name:'attendanceCreate',params:{id:props.data.id}}">-->
                        <!--                                <i class="mdi mdi-clock-end mr-2" title="Make Attendance"></i>-->
                        <!--                            </router-link>-->
                        <!--                        </template>-->
                        <template v-if="$root.is_access('Booking','edit')">
                            <router-link :to="{name:'bookingEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Booking','delete')">
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
            url: 'ajax/booking/',
            headers: [
                {
                    text: 'Name',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Company Name', value: 'company__name'},
                {text: 'Mobile', value: 'mobile'},
                {text: 'Guest Quantity', value: 'guest_quantity'},
                {text: 'Date Time', value: 'date_time'},
                {text: 'Status', value: 'status'},
                {text: 'Note', value: 'note'},
                {text: 'Entry By', value: 'id'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/booking/delete/' + id).then(res => {
                        this.$refs.dataTable.getData()
                        this.$root.message(res.data)
                    })
                }

            },
            getEntityBy(data) {
                if (data.user) {
                    var companyUser = data.company.name.replace(/\s+/g, "").toLowerCase()
                    if (data.user.username == companyUser) {
                        return data.company.authorize_person
                    } else {
                        return data.user.username
                    }
                }
            }

        }

    }
</script>

<style scoped>

</style>