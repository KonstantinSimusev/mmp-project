<script>
import { RouterView } from 'vue-router';

export default {
    data() {
        return {
            employee: [],
            employees: [],
            notTeamWorkers: [],
            production: [],
            reportBtn: [],
            sheetBtn: [],
            shift: [],
            timesheet: [],
        }
    },
}

</script>

<template>
    <RouterView :employee="employee"
                :employees="employees"
                :notTeamWorkers="notTeamWorkers"
                :production="production"
                :reportBtn="reportBtn"
                :sheetBtn="sheetBtn"
                :shift="shift" 
                :timesheet="timesheet" />
</template>

<style>

</style>