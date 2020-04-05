<template>
    <v-form v-model="valid">
        <v-layout row wrap class="formBox">
            <v-flex xs12 md12 class="mb-7">
                <div class="form-header">
                    <div class="title"> Create Duty</div>
                </div>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
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
                ></v-autocomplete>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-autocomplete
                        v-model="duty.gate_no"
                        :items="['Gate 1','Gate 2', 'Gate 3', 'Gate 4']"
                        label="In Gate No"
                        v-validate="'required'"
                        data-vv-name="gate_no"
                        :error-messages="errors.collect('gate_no')"
                        required
                        class="required"
                        outlined
                ></v-autocomplete>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <date-time
                        label="From Time"
                        :outlined="true"
                        v-model="duty.from_time"
                        :validateName="'from_time'"
                        name="from_time"
                        data-vv-name="from_time"
                        :errorMessage="errors.collect('from_time')[0]"
                        required
                        v-validate="'required'"
                        :requiredClass="true"
                >
                </date-time>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <date-time
                        label="To Time"
                        :outlined="true"
                        v-model="duty.to_time"
                        :validateName="'to_time'"
                        name="to_time"
                        data-vv-name="to_time"
                        :errorMessage="errors.collect('to_time')[0]"
                        v-validate="'required'"
                        :requiredClass="true"
                        required
                >

                </date-time>
            </v-flex>

            <v-flex xs12 md12 xl12 class="mt-4">
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

<script src="./js/create.js"></script>

<style scoped>

</style>