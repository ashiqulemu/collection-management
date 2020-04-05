<template>
    <v-layout row wrap class="formBox">
        <v-flex xs12 md12>
            <div class="userDetails">
                <h3 class="title">
                    My Profile
                    <div class="top-links">
                        <router-link :to="{name:'userChangePassword'}"  class="buttonOnHead"> change Password</router-link>
                        <router-link :to="{name:'userChangeAccountDetails'}"  class="buttonOnHead"> Edit Profile</router-link>
                    </div>
                </h3>
            </div>
        </v-flex>
        <v-flex xs12 md5>
            <div class="profileInfo">
                <div class="rows">
                    <div class="items">First Name</div>
                    <div class="items">: {{ $store.state.user.first_name}}</div>
                </div>
                <div class="rows">
                    <div class="items">Last Name</div>
                    <div class="items">: {{ $store.state.user.last_name}}</div>
                </div>
                <div class="rows">
                    <div class="items">Email</div>
                    <div class="items">: {{ $store.state.user.email}}</div>
                </div>
                <div class="rows">
                    <div class="items">Username</div>
                    <div class="items">: {{ $store.state.user.username}}</div>
                </div>
                <div class="rows">
                    <div class="items">Status</div>
                    <div class="items">: {{ $store.state.user.is_active?'Active':'Inactive'}}</div>
                </div>
            </div>
        </v-flex>

        <v-flex xs12 md2>  </v-flex>

        <v-flex xs12 md5>
            <br>
            <img src="../../../public/images/undraw_files_6b3d.svg" alt="" class="accountProfile">
        </v-flex>
        <v-flex xs12 md1></v-flex>
    </v-layout>
</template>


<style scoped lang="scss">
    .formBox {
        padding: 20px;
    }


</style>