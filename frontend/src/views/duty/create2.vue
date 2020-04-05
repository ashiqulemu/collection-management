<template>
    <v-form v-model="valid">
        <v-layout row wrap class="formBox">
            <v-flex xs12 md12 class="mb-7">
                <div class="form-header">
                    <div class="title"> Create Duty</div>
                </div>
            </v-flex>
            <v-flex xs12 md4 class="px-1 mt-2">
                <v-autocomplete
                        v-model="duty.guard"
                        :items="guards"
                        label="Guard"
                        v-validate="'required'"
                        item-text="name"
                        data-vv-name="guard"
                        item-value="id"
                        return-object
                        :error-messages="errors.collect('guard')"
                        required
                        class="required"
                        outlined
                />
            </v-flex>

            <v-flex xs12 md4 class="px-1 mt-2">
                <v-menu
                        ref="menu2"
                        v-model="menu2"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="from_time"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                >
                    <template v-slot:activator="{ on }">
                        <v-text-field
                                v-model="from_time"
                                label="Start Time"
                                readonly
                                required
                                v-on="on"
                                outlined
                        ></v-text-field>
                    </template>
                    <v-time-picker
                            v-if="menu2"
                            v-model="from_time"
                            full-width
                            @click:minute="$refs.menu2.save(from_time)"
                    ></v-time-picker>
                </v-menu>
            </v-flex>
            <v-flex xs12 md4 class="px-1 mt-2">
                <v-menu
                        ref="menu3"
                        v-model="menu3"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="to_time"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                >
                    <template v-slot:activator="{ on }">
                        <v-text-field
                                v-model="to_time"
                                label="End Time"
                                readonly
                                required
                                outlined
                                v-on="on"
                        ></v-text-field>
                    </template>
                    <v-time-picker
                            v-if="menu3"
                            v-model="to_time"
                            full-width
                            @click:minute="$refs.menu3.save(to_time)"
                    ></v-time-picker>
                </v-menu>
            </v-flex>
            <v-flex xs12 md10 class="px-1 mt-2">
                <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :return-value.sync="dates"
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="290px"
                >
                    <template v-slot:activator="{ on }">
                        <v-combobox
                                v-model="dates"
                                multiple
                                chips
                                small-chips
                                label="Dates"
                                v-on="on"
                                single-line
                                outlined
                        ></v-combobox>
                    </template>
                    <v-date-picker v-model="dates" multiple no-title>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu.save(dates)">OK</v-btn>
                    </v-date-picker>
                </v-menu>
            </v-flex>
            <v-flex xs12 md2 class="px-1 mt-2">
                <v-btn @click.prevent="dutyItemCreate" color="primary">Assign Gate</v-btn>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2" v-for="(item,index) in dutyItem" :key="index">
                <v-autocomplete
                        v-model="item.gate"
                        :items="['Gate 1','Gate 2', 'Gate 3', 'Gate 4']"
                        :label="item.date"
                        v-validate="'required'"
                        :data-vv-name="'gate_no'+index"
                        :error-messages="errors.collect('gate_no'+index)"
                        required
                        class="required"
                        outlined
                />
            </v-flex>
            <!--            <v-flex xs12 md3 class="px-1 mt-2">-->
            <!--                <VueCtkDateTimePicker-->
            <!--                        label="Start time"-->
            <!--                        v-model="duty.from_time"-->
            <!--                        formatted="DD-MM-YYYY HH:mm"-->
            <!--                        outlined-->
            <!--                        v-validate="'required'"-->
            <!--                        data-vv-name="from_time"-->
            <!--                        :error-messages="errors.collect('from_time')"-->
            <!--                        required-->
            <!--                        class="required"-->
            <!--                />-->
            <!--            </v-flex>-->
            <!--            <v-flex xs12 md3 class="px-1 mt-2">-->
            <!--                <VueCtkDateTimePicker-->
            <!--                        label="End time"-->
            <!--                        v-model="duty.to_time"-->
            <!--                        formatted="DD-MM-YYYY HH:mm"-->
            <!--                        v-validate="'required'"-->
            <!--                        data-vv-name="to_time"-->
            <!--                        :error-messages="errors.collect('to_time')"-->
            <!--                        required-->
            <!--                        class="required"-->
            <!--                        outlined-->
            <!--                />-->
            <!--            </v-flex>-->

            <v-flex xs12 md12 xl12 class="mt-4" v-if="submitBtn">
                <v-btn class="ma-2" tile @click="cancel()" color="text--white">
                    Cancel
                </v-btn>
                <v-btn class="ma-2" tile color="success"
                       @click.prevent="submit()"
                       :disabled="buttonDisable" dark>Submit
                </v-btn>

            </v-flex>
        </v-layout>

    </v-form>
</template>

<script src="./js/create2.js"></script>
