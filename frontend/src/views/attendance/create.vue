<template>
    <div v-if="renderComponent">
        <v-form>
            <v-layout row wrap class="formBox">
                <v-flex xs12 md12 class="mb-7">
                    <div class="form-header">
                        <div class="title"> Add Entry</div>
                    </div>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            class="required"
                            v-model="attendance.type"
                            :items="['Staff','Visitor']"
                            label="Type"
                            v-validate="'required'"
                            data-vv-name="type"
                            return-object
                            :error-messages="errors.collect('type')"
                            @input="getName(attendance.type)"
                            required
                            outlined
                    />
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="attendance.staff"
                            :items="staffs"
                            label="Select Name"
                            v-validate="'required'"
                            item-text="name"
                            data-vv-name="staff"
                            name="staff"
                            return-object
                            :error-messages="errors.collect('staff')"
                            required
                            class="required hasChip"
                            outlined
                    >
                        <template slot="selection" slot-scope="data">
                            <v-chip :input-value="data.selected" class="chip--select">
                                {{data.item.name}}
                            </v-chip>
                        </template>
                        <template slot="item" slot-scope="data">
                            <v-list-item-content>
                                <v-list-item-title>
                                    <span style="font-weight: bold; font-size: 13px;color: #1976d2">{{data.item.name+' '}}</span>
                                    <span style="opacity: .6; font-size: 12px;">
                                           Company: <span style="color: darkgreen">{{data.item.company__name}}
                                       </span></span>
                                </v-list-item-title>
                            </v-list-item-content>
                        </template>
                    </v-autocomplete>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2 inTime">
                    <date-time
                            label="In Time"
                            v-model="attendance.in_time"
                            v-validate="'required'"
                            data-vv-name="in_time"
                            :errorMessage="errors.collect('in_time')[0]"
                            :outlined="true"
                            required
                            :requiredClass="true"
                    ></date-time>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="attendance.gate_no"
                            :items="gateNos"
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
                    <v-text-field
                            v-model="attendance.person_quantity"
                            label="Person Quantity"
                            v-validate="'required'"
                            data-vv-name="person_quantity"
                            :error-messages="errors.collect('person_quantity')"
                            required
                            class="required"
                            outlined
                    ></v-text-field>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2 ow-time">
                    <date-time
                            label="Out Time"
                            :outlined="true"
                            v-model="attendance.out_time">
                    </date-time>
                    <span class="set-now" @click="setTimeNow()">Now</span>


                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="attendance.out_gate_no"
                            :items="gateNos"
                            label="Out Gate No"
                            outlined
                    ></v-autocomplete>
                </v-flex>

                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-autocomplete
                            v-model="attendance.vehicle"
                            :items="['Bicycle','Rikshaw', 'Motorcycle', 'Private','Mini-bus','Bus','Others','No-vehicle']"
                            label="Vehicle"
                            v-validate="'required'"
                            item-text="vehicle"
                            data-vv-name="vehicle"
                            :error-messages="errors.collect('vehicle')"
                            required
                            class="required"
                            outlined
                    ></v-autocomplete>
                </v-flex>
                <v-flex xs12 md3 class="px-1 mt-2">
                    <v-text-field
                            v-model="attendance.vehicle_quantity"
                            label="Vehicle Quantity"
                            outlined
                            type="number"
                            :disabled="attendance.vehicle=='No-vehicle'"
                    ></v-text-field>
                    <!--                    <div v-for="(i,index) in Number(attendance.vehicle_quantity)">-->
                    <!--                        <v-text-field-->
                    <!--                                v-model="attendance.vehicle_number[index]"-->
                    <!--                                label="Vehicle Number"-->
                    <!--                                outlined-->
                    <!--                        ></v-text-field>-->
                    <!--                    </div>-->


                </v-flex>

                <v-flex xs12 md9 class="px-1 mt-2">
                    <v-text-field
                            v-model="attendance.note"
                            label="Note"
                            outlined
                    ></v-text-field>
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
<style scoped lang="scss">
    .ow-time {
        position: relative;
    }

    .set-now {
        position: absolute;
        top: 40px;
        right: 5px;
        color: #3F51B5;
        cursor: pointer;
    }
</style>