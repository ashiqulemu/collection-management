import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: {},
        is_superUser: false,
        permissions: [],
        role: '',
        otherUserData: null,
        guard_data: null,
        guard_duty:false
    },
    mutations: {
        SET_USER_DATA(state, data) {
            let user = data ? data.user : ''
            if (user.is_superuser) {
                state.is_superUser = true
                state.role = 'Admin'
            } else {
                state.role = data.role_data ? data.role_data.name : ''
                state.permissions = data.permission
            }
            state.otherUserData = data.otherData ? data.otherData[0] : null
            state.guard_data = data.guard_data.length ? data.guard_data[0] : null
            state.guard_duty = data.guard_duty?data.guard_duty:false
            state.user = user
        },

    },
    actions: {
        GET_USER_DATA({commit}) {
            axios.get('/ajax/account/get-user').then(res => {
                commit('SET_USER_DATA', res.data)
            })

        }
    },
    modules: {}
})
