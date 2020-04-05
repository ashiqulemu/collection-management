require('./bootstrap');
import _ from 'lodash';
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import './scss/app.scss'
import VeeValidate from 'vee-validate';
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
import VueHtmlToPaper from 'vue-html-to-paper';

Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);

const options = {
    name: '_blank',
    specs: [
        'fullscreen=yes',
        'titlebar=yes',
        'scrollbars=yes'
    ],
    styles: [
        '/static/css/print.css',
        // '/static/css/app.css',
    ]
}
Vue.use(VueHtmlToPaper, options);
Vue.use(require('vue-moment'));
const Swal = require('sweetalert2');

Vue.use(VeeValidate)

Vue.config.productionTip = false

Vue.filter('removeUnderscore', function (value) {
    if (!value) return '';
    return value.replace('_', ' ');
})

Vue.component('side-bar', require('./views/partial/sidebar').default);
Vue.component('data-table', require('./components/table/dataTable').default);
Vue.component('date-time', require('./components/date-time').default);
Vue.component('print-data', require('./components/print/print').default);
Vue.component('staff-print', require('./components/print/staff-print').default);


new Vue({
    el: '#app',
    router,
    store,
    vuetify,
    render: function (h) {
        return h(App)
    },
    data: {
        drawer: null,
        is_superUser: false,
        permissions: [],
        role: '',
        user: {},
        otherUserData: null
    },
    created() {
        this.getUser()
    },
    computed: {
        isLoaded() {
            if (this.$store.state.user.hasOwnProperty('id')) {
                return true
            }
        }
    },
    methods: {
        getUser() {
            this.$store.dispatch('GET_USER_DATA')

        },
        message(data) {
            Swal.fire({
                position: 'center',
                type: data.type,
                title: data.message,
                showConfirmButton: false,
                allowOutsideClick: false,
                allowEscapeKey: false,
                timer: 1500
            })

        },
        is_access(model, field) {

            if (this.$store.state.is_superUser) {
                return true
            } else {
                if (this.$store.state.permissions.length) {
                    var permissions = this.$store.state.permissions
                    var permissionData = permissions.filter(data =>
                        data.moduled == model && data[field + '_permission'])

                    return permissionData.length ? true : false
                }

            }


        },

        is_any_access(model, field) {
            if (this.$store.state.is_superUser) {
                return true
            } else {
                if (this.$store.state.permissions.length) {
                    var permission = this.$store.state.permissions

                    var permissionData = permission.filter(data => {
                        if (data.moduled == model) {

                            if (data.view_permission || data.create_permission ||
                                data.edit_permission || data.delete_permission || data.share_permission) {
                                if (this.$store.state.role == 'Guard') {
                                    if (!this.$store.state.guard_duty && data.moduled != 'Duty') {
                                        return false
                                    } else {
                                        if (data.view_permission) {
                                            return true
                                        }
                                    }
                                } else {
                                    return true
                                }
                            } else {
                                return false
                            }
                        }
                    })
                    return permissionData.length ? true : false
                }
            }
        },
    }

});
