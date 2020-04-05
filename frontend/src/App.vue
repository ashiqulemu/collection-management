<template>

    <v-app id="inspire">
        <v-navigation-drawer
                v-model="drawer"
                app
        >
            <div class="brand-name">
                <router-link :to="{name:'home'}"> SHSTP SOFT</router-link>
            </div>
            <side-bar></side-bar>
        </v-navigation-drawer>

        <v-app-bar app color="#F5F5F5" class="headerBarCustomise">
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <div class="top-right">
                <!--user icon-->

                <div class="user" @click="openSettings =! openSettings">
                    <span class="mdi mdi-account"></span>
                </div>

                <!--user setting items-->

                <div class="userSettingItems" :class="{'open':openSettings}" @mouseleave="openSettings = false">
                    <div class="title">Welcome! <span>{{$store.state.user.hasOwnProperty('id')?
                        $store.state.user.username:''}}</span></div>
                    <router-link :to="{name:'userShow'}"  class="linkItems">
                        <span class="mdi mdi-account"></span>
                        My profile
                    </router-link>

                    <router-link :to="{name:'userChangePassword'}"  class="linkItems">
                        <span class="mdi mdi-settings"></span>
                         Change Password
                    </router-link>

                    <router-link :to="{name:'userChangeAccountDetails'}" class="linkItems">
                        <span class="mdi mdi-calendar-clock"></span>
                        Change Other Info
                    </router-link>

                   <router-link :to="{name:'supportShow'}"  class="linkItems">
                        <span class="mdi mdi-fan"></span>
                       Support</router-link>
                    <a href="" class="linkItems" @click.prevent="doLogout()">
                        <span class="mdi mdi-logout"></span>
                        logout
                    </a>

                </div>

            </div>
        </v-app-bar>

        <v-content>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-content>

        <v-footer
                color="white"
                app
        >
            <span class="black--text"> </span>

        </v-footer>
    </v-app>
</template>

<script>
    import HelloWorld from './components/HelloWorld';

    export default {
        name: 'App',

        components: {
            HelloWorld
        },
        data() {
            return {
                drawer: null,
                openSettings: false,
                csrfToken: '',

            }
        },
        methods: {
            doLogout() {
                axios.post('/ajax/logout').then(res=>{
                   if(res.data.result=='success'){
                       window.location.href='/accounts/login'
                   }
                })

            }
        },
        mounted() {
            document.body.addEventListener('click', function (event) {
                if (event.target.closest('.userSettingItems')) return
                if (event.target.closest('.user')) return
                this.openSettings = false
            }.bind(this));
        }
    }


</script>


<style lang="scss" scoped>
    .dashBoardContent {
        box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
    }

    .v-expansion-panel-content__wrap {
        padding: 8px 20px 8px !important;
        background: #f3f3f3 !important;
        a {
            padding: 0 5px;
            display: block;
            &:hover {
                background: #1976d2;
                display: block;
                color: #fff;
            }
        }
    }

    .v-expansion-panel-header {
        height: 42px !important;
        border-top: 1px solid #e8e8e8;
        min-height: auto !important;
    }

    .customiseable_menu {
        .v-expansion-panel--active, .v-expansion-panel--active + .v-expansion-panel {
            margin-top: 0 !important;
        }

    }

</style>

