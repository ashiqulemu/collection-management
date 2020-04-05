<template>
    <div class="layout wrap dashBoardContent">
        <div class="flex xs12 md4">
            <div class="reportBox first">
                <div class="left">
                    <span class="mdi mdi-account-check"></span>
                </div>
                <div class="right">
                    <div>
                        {{visitor_today}}<br>
                        Visitors Today
                    </div>
                </div>
                <img src="../../../public/images/overlay.svg" class="overlayShade" width="100%">
            </div>
        </div>
        <div class="flex xs12 md4">
            <div class="reportBox second">
                <div class="left">
                    <span class="mdi mdi-worker"></span>
                </div>
                <div class="right">
                    <div>
                        {{total_company}}<br>
                        Total Company
                    </div>
                </div>
                <img src="../../../public/images/overlay.svg" class="overlayShade" width="100%">

            </div>
        </div>
        <div class="flex xs12 md4">
            <div class="reportBox forth">
                <div class="left">
                    <span class="mdi mdi-cards"></span>
                </div>
                <div class="right">
                    <div>
                        {{total_staff}} <br>
                        Total Staff
                    </div>
                </div>
                <img src="../../../public/images/overlay.svg" class="overlayShade" width="100%">

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "home.vue",
        data() {
            return {
                visitor_today: 0,
                total_company: 0,
                security_guard: 0,
                total_staff: 0,
            }
        },
        created() {
            this.getDashboardData()
        },
        methods: {
            getDashboardData() {
                axios.get('/ajax/report/dashboard-report?type=guard').then(res => {
                    this.visitor_today = res.data.visitor_today,
                        this.total_company = res.data.total_company,
                        this.security_guard = res.data.security_guard,
                        this.total_staff = res.data.total_staff
                })
            }
        }
    }
</script>

<style scoped>

</style>