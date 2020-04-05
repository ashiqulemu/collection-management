<template>
    <div>
        <v-form>


            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title"> Edit Role</div>
                    </div>
                </v-flex>
                <v-flex xs12 md12 class="px-1 mt-2 ">
                    <v-text-field
                            v-model="role.name"
                            label="Role Name"
                            v-validate="'required'"
                            data-vv-name="name"
                            :error-messages="errors.collect('name')"
                            required
                            outlined
                    ></v-text-field>
                </v-flex>

                <v-flex xs12 md12 xl12 class="mt-4">
                    <v-btn class="ma-2" tile @click="cancel()" color="text--white">
                        Cancel
                    </v-btn>
                    <v-btn class="ma-2" tile color="success"
                           @click.prevent="submit()"
                           :disabled="buttonDisable" dark>Update
                    </v-btn>

                </v-flex>
            </v-layout>

        </v-form>
    </div>
</template>

<script src="./js/edit.js"></script>