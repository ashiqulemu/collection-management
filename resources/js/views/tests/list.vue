<template>
    <data-table
            :url="url"
            :tableHeadline="'Manage Tests'"
            :headers="headers"
            :addBtnLink="'testsCreate'"
    >
        <template slot="table" slot-scope="props">
            <td>{{ props.data.name }}</td>
            <td class="text-xs-center">{{ props.data.unit }}</td>
            <td class="text-xs-center">{{ props.data.range }}</td>
            <td class="justify-center layout px-0">
                <router-link :to="{name:'testsEdit',params:{id:props.data.id}}"><v-icon small class="mr-2">edit</v-icon></router-link>
                <v-icon small @click="deleteItem(props.data)"> delete</v-icon>
            </td>

        </template>
    </data-table>


</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            url: 'ajax/tests/',
            headers: [
                {
                    text: 'Test Name',
                    align: 'left',
                    value: 'name'
                },
                {text: 'Test Unit', value: 'unit'},
                {text: 'Normal Range', value: 'range'},
                {text: 'Actions', value: 'name', sortable: false}
            ],

        }),
        methods: {},

    }
</script>

<style scoped>

</style>