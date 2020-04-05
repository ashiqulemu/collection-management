<template>
    <div>
        <div id="printMe" class="d-none pt-3">
            <div>
                <h4 class="text-center text-uppercase text-info mt-2 ">
                    {{headTitle}}
                </h4>
                <table class="table table-reflow mt-3">
                    <thead>
                    <tr>
                        <th class="text-center border-right border-left
                        border-top border-bottom text-center">#
                        </th>
                        <th class="text-center border-right border-top
                        border-bottom" v-for="item in columnName">
                            {{item}}
                        </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(item,index) in data">
                        <td class="border-right border-left border-bottom
                        text-center">{{index+1}}
                        </td>
                        <td class="border-right border-left border-bottom"
                            v-for="fieldItem in fieldName">
                            <div v-if="['date_time','in_time','out_time','to_time','from_time'].includes(fieldItem)">
                                {{item[fieldItem]|moment('DD-MM-YYYY hh:mm A')}}
                            </div>
                            <div v-else-if="fieldItem=='is_attendance' ">
                                {{item[fieldItem]?'Visited':'Not Visited Yet'}}
                            </div>
                            <div v-else-if="fieldItem=='is_active'">
                                {{item[fieldItem]?'Active':'Inactive'}}
                            </div>
                            <div v-else-if="fieldItem=='a_name' ">
                                {{item['type']=='Staff'?item.staff.name:item.booking.name}}
                            </div>
                            <div v-else-if="fieldItem=='a_company' ">
                                {{item['type']=='Staff'?item.staff.company.name:item.booking.company.name}}
                            </div>
                            <div v-else-if="item[fieldItem.split('.')[0]] && fieldItem.split('.').length>1 ">
                                {{item[fieldItem.split('.')[0]][fieldItem.split('.')[1]]}}
                            </div>
                            <div v-else v-html="item[fieldItem]">
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <br>
            <br>
            <br>
            <br>


        </div>


    </div>

</template>

<script>
    export default {
        name: "print.vue",
        props: {
            data: {
                type: Array,
                default: () => []

            },
            header: {
                type: Boolean,
                default: () => true

            },

        },
        data() {
            return {
                columnName: [],
                fieldName: [],
                headTitle: '',
            }
        },
        created() {
            this.getTableRelatedData()
        },

        mounted() {
            this.$htmlToPaper('printMe');
        },
        methods: {
            getTableRelatedData() {
                if (this.$route.path == '/staff') {
                    this.columnName = ['Staff ID', 'Name', 'Company Name', 'Mobile', 'RFID'];
                    this.fieldName = ['staff_id', 'name', 'company.name', 'mobile', 'rf_id'];
                    this.headTitle = 'Staff Details'
                }else if (this.$route.path == '/booking') {
                    this.columnName = ['Name', 'Company Name', 'Mobile', 'Guest Qty.','DateTime','Status'];
                    this.fieldName = ['name', 'company.name', 'mobile', 'guest_quantity', 'date_time','is_attendance'];
                    this.headTitle = 'Visitor Booking Details'
                }else if (this.$route.path == '/attendance') {
                    this.columnName = ['Type', 'Name', 'company', 'In Time','In gate','Out Time','Out Gate','Entry By'];
                    this.fieldName = ['type', 'a_name', 'a_company', 'in_time','gate_no','out_time','out_gate_no','authorized_by.username'];
                    this.headTitle = 'Entry Details'
                }else if (this.$route.path == '/attendance/queue') {
                    this.columnName = [ 'Name', 'company', 'Mobile','Guest Qty.', 'Date Time','Status'];
                    this.fieldName = ['name', 'company.name', 'mobile','guest_quantity', 'date_time','is_attendance'];
                    this.headTitle = 'Queue Entry Details'
                }
                else if (this.$route.path == '/company') {
                    this.columnName = ['Company Name', 'Owner Name', 'Authorizer', 'Level','Email','Mobile','status'];
                    this.fieldName = ['name', 'owner', 'authorize_person', 'building.name','email','mobile','status'];
                    this.headTitle = 'Company Details'
                }else if (this.$route.path == '/guard') {
                    this.columnName = ['Guard ID', 'Name', 'NID', 'Mobile', 'RFID'];
                    this.fieldName = ['guard_id', 'name', 'nid', 'mobile', 'rf_id'];
                    this.headTitle = 'Guard Details'
                }else if (this.$route.path == '/duty') {
                    this.columnName = ['Guard', 'Gate No', 'From Time', 'To Time'];
                    this.fieldName = ['guard.name', 'gate_no', 'from_time', 'to_time'];
                    this.headTitle = 'Guard Duty Details'
                }else if (this.$route.path == '/duty-history') {
                    this.columnName = ['Guard', 'Gate No', 'From Time', 'To Time'];
                    this.fieldName = ['guard.name', 'gate_no', 'from_time', 'to_time'];
                    this.headTitle = 'Duty History Details'
                }else if (this.$route.path == '/user') {
                    this.columnName = ['Username', 'Email', 'First Name', 'Last Name','Role','Status'];
                    this.fieldName = ['user.username', 'user.email', 'user.first_name', 'user.last_name','role.name','user.is_active'];
                    this.headTitle = 'User Details'
                }else if (this.$route.path == '/building') {
                    this.columnName = ['Name'];
                    this.fieldName = ['name'];
                    this.headTitle = 'Building Details'
                }


            }
        }

    }
</script>

<style scoped lang="css">

</style>
