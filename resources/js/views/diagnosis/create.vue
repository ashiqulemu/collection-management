
<template>

    <v-container grid-list-lg class="form-style">
        <v-form ref="form" v-model="valid" lazy-validation>
            <v-layout row wrap>
                <v-flex xs12 md12>
                    <v-toolbar card color="primary">
                        <v-toolbar-title class="body-2 white--text">Create New Patient</v-toolbar-title>
                    </v-toolbar>
                </v-flex>

                <v-flex xs12 md4>
                    <v-card-text class="px-0">
                        <v-menu
                                v-model="menu"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                lazy
                                transition="scale-transition"
                                offset-y
                                full-width
                                min-width="290px"
                        >
                            <v-text-field
                                    slot="activator"
                                    v-model="date"
                                    label="Date"
                                    prepend-icon="event"
                                    readonly
                            ></v-text-field>
                            <v-date-picker v-model="date" @input="menu = false"></v-date-picker>
                        </v-menu>
                    </v-card-text>
                </v-flex>

                <v-flex xs12 md4>
                    <v-card-text class="px-0">
                        <v-select
                                v-model="patient"
                                :items="['test1', 'test2', 'Other']"
                                label="Select Patient"
                        ></v-select>

                    </v-card-text>
                </v-flex>
                <v-flex xs12 md4>
                    <v-card-text class="px-0">
                        <v-select
                                v-model="referred_by"
                                :items="['test1', 'test2', 'Other']"
                                label="Select Referred By"
                        ></v-select>

                    </v-card-text>
                </v-flex>

                <template>
                <v-layout v-for="(item,index) in reportData" :key="index">

                <v-flex xs12 md3>
                    <v-card-text class="px-0">
                        <v-autocomplete
                                v-model="item.test"
                                :items="['FBS', 'CBC', 'RBS']"
                                label="Test Name"

                        ></v-autocomplete>

                    </v-card-text>
                </v-flex>
                <v-flex xs12 md3>
                    <v-card-text class="px-0">
                          <v-text-field
                                v-model="item.result"
                                label="Result"
                                required
                                data-vv-name="result"
                                :error-messages="errors.collect('result')"
                                clearable
                        ></v-text-field>

                    </v-card-text>
                </v-flex>

                  <v-flex xs1 md1 v-if="index==0">
                    <v-card-text class="px-0">
                          <v-btn @click="addMore()" color="primary">+ Add
                            <!--<v-icon dark right>check_circle</v-icon>-->
                        </v-btn>

                    </v-card-text>
                </v-flex>
                  <v-flex xs1 md1 v-if="index!=0">
                    <v-card-text class="px-0">
                          <v-btn @click="removeMore(index)" color="red white--text">X
                            <!--<v-icon dark right>check_circle</v-icon>-->
                        </v-btn>

                    </v-card-text>
                </v-flex>
                </v-layout>

            </template>

                <v-flex xs12 md12>
                    <v-card-actions>
                        <v-btn @click="submit()" color="primary">submit
                            <!--<v-icon dark right>check_circle</v-icon>-->
                        </v-btn>

                        <v-btn color="red" @click="clear()" dark>Decline
                            <!--<v-icon dark right>block</v-icon>-->
                        </v-btn>
                    </v-card-actions>
                </v-flex>
            </v-layout>
        </v-form>

        <template>
            <v-layout row justify-center>
                <v-dialog v-model="dialog" persistent max-width="40%">
                    <v-btn slot="activator" color="primary" dark>Open Modal</v-btn>
                    <v-card>
                         <div class="elements-title">Diagonostic Investigation</div>
                         <v-layout grid-list-md row wrap>
                              <v-flex md6 xs12>
                               <div class="table-title">Physical</div>
                              <div class="data-items">
                                  <div class="items-label">
                                      <span>Colour</span>
                                  </div>
                                  <div class="input-items">
                                      <input type="text" class="data-input">
                                  </div>
                              </div>
                              <div class="data-items">
                                  <div class="items-label">
                                      <span>Appearence</span>
                                  </div>
                                  <div class="input-items">
                                      <input type="text" class="data-input">
                                  </div>
                              </div>
                          </v-flex>
                          <v-flex md6 xs12>
                              <div class="table-title">Microscopic</div>
                              <div class="data-items">
                                  <div class="items-label">
                                      <span>Epithelial</span>
                                  </div>
                                  <div class="input-items">
                                      <input type="text" class="data-input">
                                  </div>
                              </div>
                          </v-flex>
                         </v-layout>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
                            <v-btn color="blue darken-1" flat @click="dialog = false">Save</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-layout>
        </template>

    </v-container>

</template>


<script src="./js/create.js"></script>
