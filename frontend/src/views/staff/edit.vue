<template>
    <v-form v-model="valid">
        <v-layout row wrap class="formBox">
            <v-flex xs12 md12 class="mb-7">
                <div class="form-header">
                    <div class="title"> Update Employee</div>
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
                        class="required"
                        outlined
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
                        class="required"
                        outlined
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
                        outlined
                        class="required"
                ></v-text-field>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
                <v-text-field
                        v-model="staff.rf_id"
                        label="RF ID"
                        required
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
                        class="required"
                        data-vv-name="status"
                        :error-messages="errors.collect('status')"
                        outlined
                ></v-autocomplete>
            </v-flex>
            <v-flex xs12 md3 class="px-1 mt-2">
            <div class="card profileView" v-if="staff.profile_image">
                <div class="card-header text-right">
                    <i @click.prevent="removeImage"
                       class="delete-icon mdi mdi-delete"
                       title="Remove This Image"></i>
                </div>
                <div class="card-body">
                    <img :src="staff.profile_image"
                         class="mx-auto img-fluid d-block pr-image">
                </div>
            </div>
            </v-flex>
            <!--            <v-flex xs12 md3 class="px-1 mt-2">-->
            <!--                <v-btn title="Put finger print"-->
            <!--                       :loading="fingerPrintLoading"-->
            <!--                       :disabled="fingerPrintLoading"-->
            <!--                       color="blue-grey"-->
            <!--                       class="ma-2 white&#45;&#45;text"-->
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
                <v-btn class="ma-2" tile color="warning"
                       @click.prevent="submit()"
                       :disabled="buttonDisable" dark>Update
                </v-btn>

            </v-flex>
        </v-layout>

    </v-form>
</template>

<script src="./js/edit.js"></script>
