<template>
    <div>
        <dashboard v-if="!($store.state.role=='Company' ||  $store.state.role=='Guard')"></dashboard>
        <company-dashboard v-if="$store.state.role=='Company'"></company-dashboard>
        <guard-dashboard v-if="$store.state.role=='Guard'"></guard-dashboard>
    </div>
</template>

<script>
    import Dashboard from "../components/dashboard/dashboard.vue";
    import CompanyDashboard from "../components/dashboard/dashboard-company";
    import GuardDashboard from "../components/dashboard/dashboard-guard";
    export default {
        name: "home.vue",
        components:{
          Dashboard,CompanyDashboard,GuardDashboard
        },
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
                axios.get('/ajax/report/dashboard-report').then(res => {
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