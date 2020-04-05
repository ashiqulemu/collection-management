<template>
    <div>
        <div id="printMe" class="d-none pt-3">
            <div>

                <h3 class="text-center text-uppercase text-info mt-2 ">
                    {{headTitle}}
                </h3>
                <h4 class="text-center text-uppercase text-info mt-2 ">
                    Company: {{company?company.name:'All'}}
                </h4>
                <h5 class="text-center text-uppercase mt-2">Powered by TechCity</h5>
                <table class="table table-reflow mt-3">
                    <thead>
                    <tr>
                        <th class="text-center border-right border-left
                        border-top border-bottom text-center">Sl. No.
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
                        <td class="border-right border-left border-bottom">
                            {{item['name']}}
                        </td>
                        <td class="border-right border-left border-bottom text-center">
                            {{item['staff_id']}}
                        </td>
                        <td class="border-right border-left border-bottom text-center">
                            {{item['mobile']}}
                        </td>
                        <td class="border-right border-left border-bottom text-center">
                            {{item['rf_id']}}
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
            company: {
                type: Object,
                default: () => {}

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
                    this.columnName = [ 'Name','Employee ID', 'Mobile', 'RFID'];
                    // this.fieldName = [ 'name','staff_id', 'mobile', 'rf_id'];
                    this.headTitle = 'List Of Employee'
                }
            }
        }

    }
</script>

<style scoped lang="css">

</style>
