<template>
    <v-form>
        <v-layout row wrap class="formBox layoutGraph">
            <v-flex xs12 md12>
                <div class="userDetails">
                    <h3 class="title">
                        change user information
                    </h3>
                </div>
            </v-flex>
            <v-flex xs12 md6>
                <img src="../../../public/images/undraw_onboarding_o8mv.svg" class="accountdetailsImage">
            </v-flex>

            <v-flex xs12 md6>
                <div class="details" v-if="isLoad">
                    <v-text-field
                            label="First Name"
                            v-validate="'required'"
                            v-model="user.first_name"
                            data-vv-name="first_name"
                            :error-messages="errors.collect('first_name')"
                            class="required mt-5"
                            required
                            outlined
                    ></v-text-field>
                    <v-text-field
                            label="last Name"
                            v-validate="'required'"
                            v-model="user.last_name"
                            data-vv-name="last_name"
                            :error-messages="errors.collect('last_name')"
                            class="required"
                            required
                            outlined
                    ></v-text-field>
                    <v-text-field
                            label="Email"
                            v-validate="'required|email'"
                            data-vv-name="email"
                            class="required"
                            v-model="user.email"
                            :error-messages="errors.collect('email')"
                            required
                            outlined
                    ></v-text-field>
                    <v-autocomplete
                            :items="[ 'Active', 'Inactive']"
                            label="Status"
                            v-model="user.status"
                            :error-messages="errors.collect('status')"
                            v-validate="'required'"
                            data-vv-name="status"
                            class="required"
                            outlined
                            required
                    ></v-autocomplete>
                    <v-btn class="" tile color="success" @click="submit">
                        update info!
                    </v-btn>
                </div>

            </v-flex>


        </v-layout>
    </v-form>
</template>

<script src="./js/change-details.js"></script>

<style scoped lang="scss">

    .formBox {
        padding: 20px;
    }


</style>