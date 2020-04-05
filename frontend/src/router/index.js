import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/dashboard',
        name: 'home',
        component: require('../views/home').default
    },
    {path: '/', redirect: '/dashboard'},
    {
        path: '/company/create',
        name: 'companyCreate',
        component: require('../views/company/create.vue').default
    },
    {
        path: '/company',
        name: 'companyList',
        component: require('../views/company/list.vue').default
    },
    {
        path: '/company/:id/edit',
        name: 'companyEdit',
        component: require('../views/company/edit.vue').default
    },
    {
        path: '/booking/create',
        name: 'bookingCreate',
        component: require('../views/booking/create.vue').default
    },
    {
        path: '/booking',
        name: 'bookingList',
        component: require('../views/booking/list.vue').default
    },
    {
        path: '/booking/:id/edit',
        name: 'bookingEdit',
        component: require('../views/booking/edit.vue').default
    },

    {
        path: '/guard/create',
        name: 'guardCreate',
        component: require('../views/guard/create.vue').default
    },
    {
        path: '/guard',
        name: 'guardList',
        component: require('../views/guard/list.vue').default
    },
    {
        path: '/guard/:id/edit',
        name: 'guardEdit',
        component: require('../views/guard/edit.vue').default
    },
    {
        path: '/building/create',
        name: 'buildingCreate',
        component: require('../views/building/create.vue').default
    },
    {
        path: '/building',
        name: 'buildingList',
        component: require('../views/building/list.vue').default
    },
    {
        path: '/building/:id/edit',
        name: 'buildingEdit',
        component: require('../views/building/edit.vue').default
    },
    {
        path: '/staff/create',
        name: 'staffCreate',
        component: require('../views/staff/create.vue').default
    },
    {
        path: '/staff',
        name: 'staffList',
        component: require('../views/staff/list.vue').default
    },
    {
        path: '/staff/:id/edit',
        name: 'staffEdit',
        component: require('../views/staff/edit.vue').default
    },
    {
        path: '/attendance',
        name: 'attendanceList',
        component: require('../views/attendance/list.vue').default
    },
    {
        path: '/attendance/create',
        name: 'attendanceCreate',
        component: require('../views/attendance/create.vue').default
    },
    {
        path: '/attendance/:id/edit',
        name: 'attendanceEdit',
        component: require('../views/attendance/edit.vue').default
    },
    {
        path: '/attendance/queue',
        name: 'attendanceQueue',
        component: require('../views/attendance/listQueue.vue').default
    },
    {
        path: '/user',
        name: 'userList',
        component: require('../views/user/list.vue').default
    },
    {
        path: '/user/create',
        name: 'userCreate',
        component: require('../views/user/create.vue').default
    },
    {
        path: '/user/:id/edit',
        name: 'userEdit',
        component: require('../views/user/edit.vue').default
    },
    {
        path: '/role/create',
        name: 'roleCreate',
        component: require('../views/role/create.vue').default
    },
    {
        path: '/role/:id/edit',
        name: 'roleEdit',
        component: require('../views/role/edit.vue').default
    },
    {
        path: '/role',
        name: 'roleList',
        component: require('../views/role/list.vue').default
    },
    {
        path: '/role-permission/:id/edit',
        name: 'rolePermissionEdit',
        component: require('../views/permission/list.vue').default
    },
    {
        path: '/role-user',
        name: 'roleUserList',
        component: require('../views/role/assign.vue').default
    },
    {
        path: '/support/show',
        name: 'supportShow',
        component: require('../views/support/show.vue').default
    },
     {
        path: '/user/show',
        name: 'userShow',
        component: require('../views/user/show.vue').default
    },
    {
        path: '/user/change-password',
        name: 'userChangePassword',
        component: require('../views/user/change-password.vue').default
    },
     {
        path: '/user/change-account-details',
        name: 'userChangeAccountDetails',
        component: require('../views/user/change-details.vue').default
    },
    {
        path: '/duty/create',
        name: 'dutyCreate',
        component: require('../views/duty/create.vue').default
    },
    {
        path: '/duty/create2',
        name: 'dutyCreate2',
        component: require('../views/duty/create2.vue').default
    },
    {
        path: '/duty',
        name: 'dutyList',
        component: require('../views/duty/list.vue').default
    },
    {
        path: '/duty/:id/edit',
        name: 'dutyEdit',
        component: require('../views/duty/edit.vue').default
    },
     {
        path: '/duty-history',
        name: 'dutyHistory',
        component: require('../views/duty/history.vue').default
    },
    {
        path: '/*',
        name: 'not-found',
        component: require('../views/errors/404').default
    },

]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
