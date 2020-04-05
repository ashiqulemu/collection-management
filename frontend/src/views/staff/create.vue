<template>
    <v-form v-model="valid">
        <v-layout row wrap class="formBox">
            <v-flex xs12 md12   class="mb-7">
                <div class="form-header">
                    <div class="title">Add Employee</div>
                </div>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-text-field
                        v-model="staff.staff_id"
                        label="Staff ID"
                        v-validate="'required'"
                        data-vv-name="staff_id"
                        :error-messages="errors.collect('staff_id')"
                        required
                        outlined
                        class="required"
                ></v-text-field>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-text-field
                        v-model="staff.name"
                        label="Name"
                        v-validate="'required'"
                        data-vv-name="name"
                        :error-messages="errors.collect('name')"
                        required
                        outlined
                        class="required"
                ></v-text-field>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-autocomplete
                        v-model="staff.company"
                        :items="companies"
                        label="Company"
                        v-validate="'required'"
                        item-text="name"
                        data-vv-name="company"
                        item-value="id"
                        :error-messages="errors.collect('company')"
                        required
                        class="required"
                        outlined
                ></v-autocomplete>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-text-field
                        v-model="staff.mobile"
                        label="Mobile"
                        v-validate="'required'"
                        data-vv-name="mobile"
                        :error-messages="errors.collect('mobile')"
                        required
                        class="required"
                        outlined
                ></v-text-field>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-text-field
                        v-model="staff.rf_id"
                        label="RF ID"
                        v-validate="'required'"
                        data-vv-name="rf_id"
                        :error-messages="errors.collect('rf_id')"
                         class="required"
                        outlined
                ></v-text-field>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-file-input
                        id="image"
                        label="Staff Profile Image"
                        data-vv-name="profile_image"
                        accept="image/*"
                        placeholder="Pick an avatar"
                        prepend-icon="mdi-camera"
                        outlined
                ></v-file-input>
            </v-flex>

            <v-flex xs12 md3 class="px-1 mt-2">
                <v-autocomplete
                        v-model="staff.status"
                        :items="['Active','Inactive']"
                        label="Status"
                        v-validate="'required'"
                        data-vv-name="status"
                        :error-messages="errors.collect('status')"
                        outlined
                        class="required"
                ></v-autocomplete>
            </v-flex>
<!--            <v-flex xs12 md3 class="px-1 mt-2">-->
<!--                <v-btn title="Put finger print"-->
<!--                       :loading="fingerPrintLoading"-->
<!--                       :disabled="fingerPrintLoading"-->
<!--                       color="blue-grey"-->
<!--                       class="white&#45;&#45;text fingerPrint"-->
<!--                       fab-->
<!--                       @click="loader = 'fingerPrintLoading'"-->
<!--                >-->
<!--                    <i class="mdi mdi-fingerprint  headline"></i>-->
<!--                </v-btn>-->
<!--            </v-flex>-->
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