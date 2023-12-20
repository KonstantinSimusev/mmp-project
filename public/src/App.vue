<script>
import { RouterView } from 'vue-router';

export default {
    data() {
        return {
            addedTrainees: [],
            addWorkers: [],
            employee: [],
            employees: [],
            production: [],
            reportBtn: [],
            shift: [],
            timesheet: [],
            trainees: [],
        }
    },
}
</script>

<template>

    <RouterView 
        :addedTrainees="addedTrainees"
        :addWorkers="addWorkers"
        :employee="employee"
        :employees="employees"
        :production="production"
        :reportBtn="reportBtn"
        :shift="shift" 
        :timesheet="timesheet"
        :trainees="trainees" />

</template>

<style>

</style>