<template>
    <div>
        <div class="container-fluid">
            <data-table
                    :url="url"
                    :tableHeadline="'Duty History'"
                    :headers="headers"
                    :addBtnLink="'dutyCreate'"
                    :addButton="false"
                    class="custom-table-adjust"
                    ref="dataTable"
            >
                <template slot="table" slot-scope="props">
                    <td>{{props.data.guard?props.data.guard.name:''}}</td>
                    <td>{{props.data.gate_no}}</td>
                    <td>{{props.data.login_time|moment('DD-MM-YYYY hh:mm A')}}</td>
                    <td>{{props.data.logout_time|moment('DD-MM-YYYY hh:mm A')}}</td>
                    <td>{{getDifferentTime(props.data)}}</td>
                    <td class="justify-center layout px-0 align-center">
                        <!--                        <template v-if="$root.is_access('Duty','edit')">-->
                        <!--                            <router-link :to="{name:'dutyEdit',params:{id:props.data.id}}">-->
                        <!--                                <i class="mdi mdi-grease-pencil mr-2" title="Edit"></i>-->
                        <!--                            </router-link>-->
                        <!--                        </template>-->
                        <!--                        <template v-if="$root.is_access('Duty','delete')">-->
                        <!--                            <a @click="deleteItem(props.data.id)">-->
                        <!--                                <i title="Delete" class="mdi mdi-delete red&#45;&#45;text"></i>-->
                        <!--                            </a>-->
                        <!--                        </template>-->
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
            url: '/ajax/duty-history/',
            headers: [
                {
                    text: 'Guard',
                    align: 'left',
                    value: 'guard__name'
                },
                {text: 'Gate No', value: 'gate_no'},
                {text: 'Start Time', value: 'login_time'},
                {text: 'End Time', value: 'logout_time'},
                {text: 'Total Time', value: 'id'},
                {text: 'Actions', value: 'id', sortable: false}
            ],

        }),
        methods: {
            getDifferentTime(data) {
                var startDate = data.login_time ? new Date(data.login_time) : '';
                var endDate = data.logout_time ? new Date(data.logout_time) : '';
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
            deleteItem(id) {
                // if (confirm('Are you sure you want to delete this')) {
                //     axios.delete('ajax/duty/delete/' + id).then(res => {
                //         this.$refs.dataTable.getData()
                //         this.$root.message(res.data)
                //     })
                // }

            },

        }

    }
</script>

<style scoped>

</style>