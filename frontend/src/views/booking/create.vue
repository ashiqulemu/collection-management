<template>
    <div>
        <v-form>

            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title">CREATE VISITOR BOOKING</div>
                    </div>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="booking.name"
                            label="Name"
                            v-validate="'required'"
                            data-vv-name="name"
                            :error-messages="errors.collect('name')"
                            outlined
                            required
                            class="required"
                    ></v-text-field>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="booking.company"
                            :items="companies"
                            label="Company"
                            item-text="name"
                            v-validate="'required'"
                            data-vv-name="company"
                            :error-messages="errors.collect('company')"
                            item-value="id"
                            return-object
                            @input.native="loadStates"
                            outlined
                            required
                            class="required"
                    ></v-autocomplete>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="booking.mobile"
                            outlined
                            label="Mobile"
                    ></v-text-field>
                </v-flex>


                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="booking.guest_quantity"
                            label="Guest Quantity"
                            v-validate="'required'"
                            data-vv-name="guest_quantity"
                            :error-messages="errors.collect('guest_quantity')"
                            outlined
                            required
                            type="number"
                            class="required"
                    ></v-text-field>
                </v-flex>


                <v-flex xs12 md3 class="px-1 mt-2 dateTime">
                    <date-time
                            label="Date Time"
                            v-model="booking.date_time"
                            v-validate="'required'"
                            data-vv-name="date_time"
                            :error-messages="errors.collect('date_time')"
                            :outlined="true"
                            required
                            class="required"
                    ></date-time>
                </v-flex>
                <v-flex xs12 md9 class="px-1 mt-2">
                    <v-text-field
                            v-model="booking.note"
                            label="Note"
                            outlined
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md12 class="px-1 mt-2">
                    <v-btn class="ma-2" tile color="text--white" @click="cancel()">
                        Cancel
                    </v-btn>
                    <v-btn class="ma-2" tile color="success"
                           @click.prevent="submit()"
                           :disabled="buttonDisable" dark>Submit
                    </v-btn>
                </v-flex>

            </v-layout>


        </v-form>
    </div>
</template>

<script src="./js/create.js"></script>