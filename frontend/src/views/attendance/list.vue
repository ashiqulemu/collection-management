<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Manage Entry'"
                    :headers="headers"
                    :addBtnLink="'attendanceCreate'"
                    :addButton="$root.is_access('Attendance','create')"
                    class="custom-table-adjust"
                    ref="dataTable"
                    :dateSearch="true"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.type}}</td>
                    <td>
                        <template v-if="props.data.type=='Staff'">
                             {{props.data.staff?props.data.staff.name:''}}
                        </template>
                         <template v-if="props.data.type=='Visitor'">
                             {{props.data.booking?props.data.booking.name:''}}
                        </template>

                    </td>
                    <td>
                        <template v-if="props.data.type=='Staff'">
                             {{props.data.staff?props.data.staff.company.name:''}}
                        </template>
                         <template v-if="props.data.type=='Visitor'">
                             {{props.data.booking?props.data.booking.company.name:''}}
                        </template>
                    </td>
                    <td>{{props.data.in_time|moment('DD-MM-YYYY hh:mm A')}}</td>
                    <td>{{props.data.gate_no}}</td>
                    <td>{{props.data.person_quantity}}</td>
                    <td>
                        <template v-if="props.data.out_time">
                            {{props.data.out_time|moment('DD-MM-YYYY hh:mm A')}}
                        </template>
                        <template v-else>
                            {{props.data.out_time}}
                        </template>

                    </td>
                    <td>{{props.data.out_gate_no}}</td>
                    <td>{{getDifferentTime(props.data)}}</td>
                    <td>{{props.data.vehicle}}</td>
                    <td>{{props.data.vehicle_quantity}}</td>
                    <td>{{props.data.authorized_by?props.data.authorized_by.username:''}}
                    </td>
                    <td class="justify-center px-0 align-center icon">
                        <template v-if="$root.is_access('Attendance','edit')">
                            <router-link :to="{name:'attendanceEdit',params:{id:props.data.id}}">
                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>
                            </router-link>
                        </template>
                        <template v-if="$root.is_access('Attendance','delete')">
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
            url: 'ajax/attendance/',
            headers: [
                {
                    text: 'Type',
                    align: 'left',
                    value: 'type'
                },
                {text: 'Name', value: 'staff_name'},
                {text: 'Company', value: 'company_name'},
                {text: 'In Time', value: 'in_time'},
                {text: 'In Gate ', value: 'gate_no'},
                {text: 'Person Qty', value: 'person_quantity'},
                {text: 'Out Time', value: 'out_time'},
                {text: 'Out Gate', value: 'out_gate_no'},
                {text: 'Time Stay', value: 'id'},
                {text: 'Vehicle', value: 'vehicle'},
                {text: 'Vehicle Qty', value: 'vehicle_quantity'},
                {text: 'Entry By', value: 'authorize_by'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            deleteItem(id) {
                if (confirm('Are you sure you want to delete this')) {
                    axios.delete('ajax/attendance/delete/' + id).then(res => {
                        this.$refs.dataTable.getData()
                        this.$root.message(res.data)
                    })
                }

            },
             getDifferentTime(data) {
                var startDate = data.in_time ? new Date(data.in_time) : '';
                var endDate = data.out_time ? new Date(data.out_time) : '';
                if (startDate && endDate) {
                    var seconds = (endDate.getTime() - startDate.getTime()) / 1000;
                    seconds = parseInt(seconds, 10);
                    var days = Math.floor(seconds / (3600 * 24));
                    seconds -= days * 3600 * 24;
                    var hrs = Math.floor(seconds / 3600);
                    seconds -= hrs * 3600;
                    var mnts = Math.floor(seconds / 60);
                    seconds -= mnts * 60;
                    hrs = hrs + (days * 24)
                    hrs = hrs.toString().length == 1 ? '0' + hrs : hrs
                    mnts = mnts.toString().length == 1 ? '0' + mnts : mnts
                    seconds = seconds.toString().length == 1 ? '0' + seconds : seconds
                    return hrs + ':' + mnts + ':' + seconds
                } else {
                    return 'Both Time need'
                }

            },

        }

    }
</script>

<style scoped>

</style>