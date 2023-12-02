<script>
import { RouterView } from 'vue-router';

export default {
    data() {
        return {
            addEmployee: [],
            employee: [],
            employees: [],
            nameOptions: [],
            notTeamWorkers: [],
            production: [],
            reportBtn: [],
            shift: [],
            timesheet: [],
            trainees: [],
            teamWorkers: [],
        }
    },
}

</script>

<template>
    <RouterView :addEmployee="addEmployee"
                :employee="employee"
                :employees="employees"
                :nameOptions="nameOptions"
                :notTeamWorkers="notTeamWorkers"
                :production="production"
                :reportBtn="reportBtn"
                :shift="shift" 
                :timesheet="timesheet"
                :trainees="trainees"
                :teamWorkers="teamWorkers" />
</template>

<style>

</style>