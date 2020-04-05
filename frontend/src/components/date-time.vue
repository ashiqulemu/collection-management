<template>
    <v-dialog v-model="display" :width="dialogWidth">
        <template v-slot:activator="{ on }">

            <v-text-field
                    v-bind="textFieldProps"
                    :disabled="disabled"
                    :loading="loading"
                    :label="label"
                    :value="formattedDatetime"
                    v-on="on"
                    :error-messages="errorMessage"
                    :outlined="outlined"
                    :class="{'ow-date-time':true, 'required':requiredClass}"
            >
                <template v-slot:progress>
                    <slot name="progress">
                        <v-progress-linear color="primary" indeterminate absolute height="2"></v-progress-linear>
                    </slot>
                </template>
            </v-text-field>
        </template>

        <v-card>
            <v-card-text class="px-0 py-0">
                <v-tabs fixed-tabs v-model="activeTab">
                    <v-tab key="calendar">
                        <slot name="dateIcon">
                            Date
                            <i class="mdi mdi-event mr-2" title="Date"></i>
                            <!--<v-icon>event</v-icon>-->
                        </slot>
                    </v-tab>
                    <v-tab key="timer" :disabled="dateSelected">
                        <slot name="timeIcon">
                            Time
                            <i class="mdi mdi-event mr-2" title="Date"></i>
                            <!--<v-icon>access_time</v-icon>-->
                        </slot>
                    </v-tab>
                    <v-tab-item key="calendar">
                        <v-date-picker v-model="date" v-bind="datePickerProps" @input="showTimePicker"
                                       full-width></v-date-picker>
                    </v-tab-item>
                    <v-tab-item key="timer">
                        <v-time-picker
                                ref="timer"
                                class="v-time-picker-custom"
                                v-model="time"
                                v-bind="timePickerProps"
                                full-width
                        ></v-time-picker>
                    </v-tab-item>
                </v-tabs>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <slot name="actions" :parent="this">
                    <v-btn color="grey lighten-1" text @click.native="clearHandler">{{ clearText }}</v-btn>
                    <v-btn color="green darken-1" text @click="okHandler">{{ okText }}</v-btn>
                </slot>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    import {format, parse} from 'date-fns'

    var DEFAULT_DATE = '';
    const DEFAULT_TIME = '00:00:00'
    const DEFAULT_DATE_FORMAT = 'yyyy-MM-dd'
    const DEFAULT_TIME_FORMAT = 'HH:mm:ss'
    const DEFAULT_DIALOG_WIDTH = 340
    const DEFAULT_CLEAR_TEXT = 'CLEAR'
    const DEFAULT_OK_TEXT = 'OK'
    export default {
        name: 'v-datetime-picker',
        model: {
            prop: 'datetime',
            event: 'input'
        },
        props: {
            datetime: {
                type: [Date, String, Object],
                default: null
            },
            disabled: {
                type: Boolean
            },
            loading: {
                type: Boolean
            },
            label: {
                type: String,
                default: ''
            },
            dialogWidth: {
                type: Number,
                default: DEFAULT_DIALOG_WIDTH
            },
            dateFormat: {
                type: String,
                default: DEFAULT_DATE_FORMAT
            },
            timeFormat: {
                type: String,
                default: 'HH:mm'
            },
            clearText: {
                type: String,
                default: DEFAULT_CLEAR_TEXT
            },
            okText: {
                type: String,
                default: DEFAULT_OK_TEXT
            },
            textFieldProps: {
                type: Object
            },
            datePickerProps: {
                type: Object
            },
            timePickerProps: {
                type: Object
            },
            outlined: {
                type: Boolean,
                default: false
            },
            requiredClass: {
                type: Boolean,
                default: false
            },
            errorMessage: {
                type: String,
                default: ''
            }
        },
        data() {
            return {
                display: false,
                activeTab: 0,
                date: DEFAULT_DATE,
                time: DEFAULT_TIME
            }
        },

        mounted() {
           this.DEFAULT_DATE=this.formatDate(new Date())
            this.init()
        },
        computed: {
            dateTimeFormat() {
                return this.dateFormat + ' ' + this.timeFormat
            },
            defaultDateTimeFormat() {
                return DEFAULT_DATE_FORMAT + ' ' + DEFAULT_TIME_FORMAT
            },
            formattedDatetime() {
                return this.selectedDatetime ? format(this.selectedDatetime, this.dateTimeFormat) : ''
            },
            selectedDatetime() {
                if (this.date && this.time) {
                    let datetimeString = this.date + ' ' + this.time
                    if (this.time.length === 5) {
                        datetimeString += ':00'
                    }
                    return parse(datetimeString, this.defaultDateTimeFormat, new Date())
                } else {
                    return null
                }
            },
            dateSelected() {
                return !this.date
            }
        },
        methods: {
            init() {
                if (!this.datetime) {
                    return null
                }
                let initDateTime=null
                if (this.datetime instanceof Date) {
                    initDateTime = this.datetime
                } else if (typeof this.datetime === 'string' || this.datetime instanceof String) {
                    initDateTime = parse(this.datetime, this.dateTimeFormat, new Date())
                } else if(this.datetime instanceof Object)
                {
                    initDateTime=this.datetime._i?parse(this.datetime._i, this.dateTimeFormat, new Date()):null
                }
                this.date = format(initDateTime, DEFAULT_DATE_FORMAT)
                this.time = format(initDateTime, DEFAULT_TIME_FORMAT)
            },
            okHandler() {
                this.resetPicker()
                this.$emit('input', this.selectedDatetime)
            },
            clearHandler() {
                this.resetPicker()
                this.date = DEFAULT_DATE
                this.time = DEFAULT_TIME
                this.$emit('input', null)
            },
            resetPicker() {
                this.display = false
                this.activeTab = 0
                if (this.$refs.timer) {
                    this.$refs.timer.selectingHour = true
                }
            },
            showTimePicker() {
                this.activeTab = 1
            },
            formatDate(date) {
                var day = date.getDate();
                var monthIndex = date.getMonth();
                var year = date.getFullYear();
                return year+' '+monthIndex+' '+day

            }
        },
        watch: {
            datetime: function () {
                this.init()
            }
        }
    }
</script>