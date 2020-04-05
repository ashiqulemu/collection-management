<template>
    <div>
        <v-form v-model="valid">
            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title"> Create Guard</div>
                    </div>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.guard_id"
                            label="Guard ID"
                            v-validate="'required'"
                            data-vv-name="guard_id"
                            :error-messages="errors.collect('guard_id')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.first_name"
                            label="Guard First Name"
                            v-validate="'required'"
                            data-vv-name="first_name"
                            :error-messages="errors.collect('first_name')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.last_name"
                            label="Guard Last Name"
                            v-validate="'required'"
                            data-vv-name="last_name"
                            :error-messages="errors.collect('last_name')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.nid"
                            label="Guard NID"
                            v-validate="'required'"
                            data-vv-name="nid"
                            :error-messages="errors.collect('nid')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.mobile"
                            label="Guard Mobile"
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
                            v-model="guard.rf_id"
                            label="Guard RFID"
                            v-validate="'required'"
                            data-vv-name="rf_id"
                            :error-messages="errors.collect('rf_id')"
                            required
                            class="required"
                            outlined
                    ></v-text-field>
                </v-flex>


                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="guard.profile_image"
                            label="Guard Profile Image"
                            accept="image/png, image/jpeg, image/bmp"
                            placeholder="Pick an avatar"
                            prepend-icon="mdi-camera"
                            outlined
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md2 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="guard.status"
                            :items="['Active','Inactive']"
                            label="Status"
                            v-validate="'required'"
                            data-vv-name="status"
                            :error-messages="errors.collect('status')"
                            outlined
                            class="required"
                    ></v-autocomplete>
                </v-flex>
                <v-flex xs12 md1 class="px-2">
                    <v-btn title="Put finger print"
                           :loading="fingerPrintLoading"
                           :disabled="fingerPrintLoading"
                           color="blue-grey"
                           class="ma-2 white--text"
                           fab
                           @click="loader = 'fingerPrintLoading'"
                    >
                        <i class="mdi mdi-fingerprint  headline"></i>
                    </v-btn>
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
    </div>
</template>

<script src="./js/create.js"></script>