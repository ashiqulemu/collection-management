<template>
    <div>
        <v-form>


            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title"> Create User</div>
                    </div>
                </v-flex>

                <v-flex xs12 md4 class="px-1 mt-2">
                    <v-text-field
                            v-model="user.first_name"
                            label="First Name"
                            required
                            v-validate="'required'"
                            data-vv-name="first_name"
                            :error-messages="errors.collect('first_name')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 class="px-1 mt-2">
                    <v-text-field
                            v-model="user.last_name"
                            label="Last Name"
                            required
                            v-validate="'required'"
                            data-vv-name="last_name"
                            :error-messages="errors.collect('last_name')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>


                <v-flex xs12 md4 class="px-1 mt-2">
                    <v-text-field
                            v-model="user.email"
                            label="Email"
                            required
                            v-validate="'required|email'"
                            data-vv-name="email"
                            :error-messages="errors.collect('email')"
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>

                <v-flex xs12 md4 class="px-1 mt-2 ">
                    <v-text-field
                            v-model="user.username"
                            label="Username"
                            v-validate="'required'"
                            data-vv-name="username"
                            :error-messages="errors.collect('username')"
                            required
                            outlined
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 class="px-1 mt-2 ">
                    <v-text-field
                            v-model="user.password"
                            label="Password"
                            v-validate="'required'"
                            data-vv-name="password"
                            :error-messages="errors.collect('password')"
                            required
                            outlined
                            :type="'password'"
                            class="required"
                    ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="user.role"
                            :items="roles"
                            label="Role"
                            v-validate="'required'"
                            data-vv-name="role"
                            :error-messages="errors.collect('role')"
                            return-object
                            item-text="name"
                            outlined
                            class="required"
                    ></v-autocomplete>
                </v-flex>


                <v-flex xs12 md12 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="user.status"
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