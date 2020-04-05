<template>
    <div>
        <v-form>
            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title"> Create Company</div>
                    </div>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2 ">
                    <v-text-field
                            v-model="company.name"
                            label="Company Name"
                            v-validate="'required'"
                            data-vv-name="name"
                            :error-messages="errors.collect('name')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="company.owner"
                            label="Owner Name"
                            required
                            v-validate="'required'"
                            data-vv-name="owner"
                            :error-messages="errors.collect('owner')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="company.authorize_person"
                            label="Authorize Person"
                            required
                            v-validate="'required'"
                            data-vv-name="authorize_person"
                            :error-messages="errors.collect('authorize_person')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="company.building"
                            :items="buildings"
                            item-text="name"
                            item-value="id"
                            label="Level"
                            v-validate="'required'"
                            data-vv-name="level"
                            :error-messages="errors.collect('level')"
                            outlined
                            class="required"
                    ></v-autocomplete>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="company.email"
                            label="Email"
                            required
                            v-validate="'required|email'"
                            data-vv-name="email"
                            :error-messages="errors.collect('email')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="company.mobile"
                            label="Mobile"
                            required
                            v-validate="'required'"
                            data-vv-name="mobile"
                            :error-messages="errors.collect('mobile')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="company.status"
                            :items="['Active','Inactive']"
                            label="Status"
                            v-validate="'required'"
                            data-vv-name="status"
                            :error-messages="errors.collect('status')"
                            outlined
                            class="required"
                    ></v-autocomplete>
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