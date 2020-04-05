<template>
    <div class="pl-3 pr-3">
        <v-layout row wrap>
            <v-flex xs12 class="tableShadow">
                <v-toolbar flat color="white">
                    <v-toolbar-title>{{tableHeadline}}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-text-field
                            v-model="search"
                            label="Search"
                            single-line
                            hide-details
                            class="px-3"
                            @keyup="getData"
                    ></v-text-field>
                    <div class="col-md-4" v-if="dateSearch">
                        <v-menu
                                v-model="menu"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                transition="scale-transition"
                                offset-y
                                min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                                <v-text-field
                                        v-model="date"
                                        label="Date"
                                        readonly
                                        v-on="on"
                                        single-line
                                        hide-details
                                         @input="getData()"
                                        clearable
                                ></v-text-field>
                            </template>
                            <v-date-picker v-model="date"
                                           @input="menu = false,getData()">

                            </v-date-picker>
                        </v-menu>
                    </div>
                    <div class="col-md-3" v-if="companySearch">
                        <v-autocomplete
                                v-model="company"
                                label="Company"
                                :items="companies"
                                item-text="name"
                                return-object
                                single-line
                                hide-details
                                @input="getData"
                                clearable
                        ></v-autocomplete>
                    </div>

                    <div class="actions">
                        <router-link :to="{name:addBtnLink}" v-if="addButton" class="mr-1">
                            <i class="mdi mdi-plus-circle-outline px-2"
                               title="Add New"
                            >
                            </i>
                        </router-link>

                        <i class="mdi mdi-printer-settings"
                           @click.prevent="printMe"
                        >
                        </i>

                    </div>
                </v-toolbar>
                <v-data-table
                        :headers="headers"
                        :search="search"
                        :options.sync="options"
                        :server-items-length="totalItems"
                        :footer-props="{
                            'items-per-page-options': [10, 20, 50, 100, 200, 500]
                          }"
                        :items-per-page="10"
                        :loading="loading"
                        class="elevation-1"
                        :items="items"
                        :mobile-breakpoint='0'
                        @update:options="getData"
                >
                    <template v-slot:body="{ items }">
                        <tbody>
                        <tr v-for="item in items" :key="item.id">
                            <slot name="table" :data="item"></slot>
                        </tr>
                        </tbody>
                    </template>

                    <template slot="no-data">
                        <v-btn color="primary" @click="getData">Reset</v-btn>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
        <print-data v-if="needPrint"
                    :data="items"
        >
        </print-data>
        <staff-print v-if="staffPrint"
                     :data="items"
                     :company="this.company"
        >

        </staff-print>
    </div>


</template>

<script>
    export default {
        props: {
            data: {
                type: Array,
                default: () => []
            },
            url: {
                type: String,
                default: () => ''
            },
            tableHeadline: {
                type: String,
                default: () => ''
            },
            headers: {
                type: Array,
                default: () => []
            },
            addBtnLink: {
                type: String,
                default: () => ''
            },
            searchField: {
                type: String,
                default: () => ''
            },
            addButton: {
                type: Boolean,
                default: () => true
            },
            dateSearch: {
                type: Boolean,
                default: () => false
            },
            companySearch: {
                type: Boolean,
                default: () => false
            },

        },
        data: () => ({
            search: '',
            dialog: false,
            loading: false,
            items: [],
            options: {},
            needPrint: false,
            staffPrint: false,
            totalItems: 0,
            menu: false,
            date: '',
            company: '',
            companies: []

        }),
        mounted() {
            if (this.$route.path == '/staff') {
                axios.get('/ajax/staff/create').then(res => {
                    this.companies = res.data.companies
                })
            }
        },
        methods: {
            getData() {
                this.loading = true
                axios(this.url, {
                    params: {
                        rowsPerPage: this.options.itemsPerPage,
                        sortBy: this.options.sortBy[0] ? this.options.sortBy[0] : 'id',
                        sortOrder: this.options.sortDesc[0] ? 'ASC' : 'DESC',
                        page: this.options.page,
                        searchValue: this.search,
                        date: this.date,
                        company: this.company ? this.company.id : '',
                        // searchField:this.searchField
                    }
                }).then(res => {
                    this.items = res.data.data;
                    this.totalItems = res.data.totalItems
                    this.loading = false
                    // this.$root.roleList = res.data.roleList ? res.data.roleList : []
                })
            },


            printMe() {
                if (this.company) {
                    this.needPrint = false;
                    this.staffPrint = true
                } else {
                    this.needPrint = true
                }
                setTimeout(function () {
                    location.reload()
                }, 1500);


            },
        }
    }
</script>

<style scoped>

</style>