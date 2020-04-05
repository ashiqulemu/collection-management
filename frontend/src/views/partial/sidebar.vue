<template>
    <v-expansion-panels class="customiseable_menu">

        <v-list-item class=" singleItems">
            <v-list-item-content class="singleItemsContent">
                <v-list-item-title class="listTitle">
                    <router-link :to="{name:'home'}">
                        <span class="mdi mdi-view-dashboard"></span> Dashboard
                    </router-link>
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
        <template v-if="$root.isLoaded">
            <v-expansion-panel v-if="$root.is_any_access('Booking')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-calendar-clock"></span> Visitor Booking
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Booking','create')">
                            <router-link :to="{'name':'bookingCreate'}">
                                <span class="mdi mdi-calendar-plus"> </span>
                                Add Booking
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Booking','edit') ||
                        $root.is_access('Booking','delete') || $root.is_access('Booking','view')">
                            <router-link :to="{'name':'bookingList'}">
                                <span class="mdi mdi-settings"></span>
                                Manage Booking
                            </router-link>
                        </div>

                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Attendance')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-account-edit"></span>
                    Entry
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title">
                            <router-link :to="{'name':'attendanceCreate'}" v-if="$root.is_access('Attendance','create')">
                                <span class="mdi mdi-account-check"></span>
                                Add Entry
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Attendance','edit') ||
                        $root.is_access('Attendance','delete') || $root.is_access('Attendance','view')">
                            <router-link :to="{'name':'attendanceList'}">
                                <span class="mdi mdi-tooltip-edit"></span>
                                Manage Entry
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Attendance','view') && $store.state.role!='Company'">
                            <router-link :to="{'name':'attendanceQueue'}">
                                <span class="mdi mdi-tooltip-edit"></span>
                                Queue Entry
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Building')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-city"></span> Building
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Building','create')">
                            <router-link :to="{'name':'buildingCreate'}">
                                <span class="mdi mdi-account-multiple-plus"></span>
                                Add Building
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Building','edit') ||
                        $root.is_access('Building','delete') || $root.is_access('Building','view')">
                            <router-link :to="{'name':'buildingList'}">
                                <span class="mdi mdi-account-switch"></span>
                                Manage Building
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Company')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-home-modern"></span>
                    Company
                </v-expansion-panel-header>

                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Company','create')">
                            <router-link :to="{'name':'companyCreate'}">
                                <span class="mdi mdi-loupe"></span>
                                Add Company
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Company','edit') ||
                        $root.is_access('Company','delete') || $root.is_access('Company','view')">
                            <router-link :to="{'name':'companyList'}">
                                <span class="mdi mdi-comment-check-outline"></span>
                                Manage Company
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Staff')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-worker"></span> Employee
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Staff','create')">
                            <router-link :to="{'name':'staffCreate'}">
                                <span class="mdi mdi-account-multiple-plus"></span>
                                Add Employee
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Staff','edit') ||
                        $root.is_access('Staff','delete') || $root.is_access('Staff','view')">
                            <router-link :to="{'name':'staffList'}">
                                <span class="mdi mdi-account-switch"></span>
                                Manage Employee
                            </router-link>
                        </div>

                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Guard')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-security"></span>
                    Security Guard
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Guard','create')">
                            <router-link :to="{'name':'guardCreate'}">
                                <span class="mdi mdi-worker"></span>
                                Add Guard
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Guard','edit') ||
                        $root.is_access('Guard','delete') || $root.is_access('Guard','view')">
                            <router-link :to="{'name':'guardList'}">
                                <span class="mdi mdi-settings"></span>
                                Manage Guard
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Duty') || $root.is_any_access('Duty-History') ">
                <v-expansion-panel-header>
                    <span class="mdi mdi-security"></span>
                    Guard Duty Schedule
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('Duty','create')">
                            <router-link :to="{'name':'dutyCreate'}">
                                <span class="mdi mdi-worker"></span>
                                Add Duty Schedule
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('Duty','edit') ||
                        $root.is_access('Duty','delete') || $root.is_access('Duty','view')">

                            <router-link :to="{'name':'dutyList'}">
                                <span class="mdi mdi-settings"></span>
                                Manage Duty Schedule
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_any_access('Duty-History')">

                            <router-link :to="{'name':'dutyHistory'}">
                                <span class="mdi mdi-settings"></span>
                                Duty Record
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel v-if="$root.is_any_access('User')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-account-multiple-outline"></span>
                    User
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content">
                        <div class="v-list__tile__title" v-if="$root.is_access('User','create')">
                            <router-link :to="{'name':'userCreate'}">
                                <span class="mdi mdi-account-multiple-plus"></span>
                                Add User
                            </router-link>
                        </div>
                        <div class="v-list__tile__title" v-if="$root.is_access('User','edit') ||
                        $root.is_access('User','delete') || $root.is_access('User','view')">
                            <router-link :to="{'name':'userList'}">
                                <span class="mdi mdi-comment-check-outline"></span>
                                Manage User
                            </router-link>
                        </div>
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel v-if="$root.is_any_access('Role-Permission')">
                <v-expansion-panel-header>
                    <span class="mdi mdi-account-multiple-outline"></span>
                    Role & Permission
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="v-list__tile__content" v-if="$root.is_access('Role-Permission','create') || $root.is_access('Role-Permission','edit') ||
                        $root.is_access('Role-Permission','delete') || $root.is_access('Role-Permission','view')">
                        <div class="v-list__tile__title">
                            <router-link :to="{'name':'roleList'}">
                                <span class="mdi mdi-account-multiple-plus"></span>
                                Manage
                            </router-link>
                        </div>
                        <div class="v-list__tile__title">
                            <router-link :to="{'name':'roleUserList'}">
                                <span class="mdi mdi-account-multiple-plus"></span>
                                Assign Role
                            </router-link>
                        </div>
                        <!--                     <div class="v-list__tile__title">-->
                        <!--                        <router-link :to="{'name':'permissionList'}">-->
                        <!--                            <span class="mdi mdi-account-multiple-plus"></span>-->
                        <!--                            Manage Permission-->
                        <!--                        </router-link>-->
                        <!--                    </div>-->
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </template>
    </v-expansion-panels>
</template>

<script>
    export default {
        name: "sidebar"
    }
</script>
