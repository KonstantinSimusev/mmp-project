<script>
import axios from 'axios';

import DateForm from './forms/DateForm.vue';
import ReportModal from './modals/ReportModal.vue';
import TimeSheetModal from './modals/TimeSheetModal.vue';
import AddModal from './modals/AddModal.vue';

export default {
    name: 'MasterPage',
    components: { 
        DateForm, 
        ReportModal, 
        TimeSheetModal, 
        AddModal 
    },
    props: [
        'employee', 
        'employees', 
        'notTeamWorkers',
        'production', 
        'reportBtn', 
        'sheetBtn', 
        'shift', 
        'timesheet'
    ],
    data() {
        return {
            areas: [],
            teamWorkers: [],
        }
    },
    async mounted() {
        try {
            const dataBaseAreas = await axios
                .get('http://127.0.0.1:8000/api/area/?format=json');
            
            this.areas = dataBaseAreas.data;
        }
        catch (error) {
            console.log(error);
        }

        let newAreas = this.areas.filter(area => area.slug != 'lpc_5');

        this.teamWorkers = this.employees.filter(employee =>
            employee.team == this.employee[0].team &&
            employee.schedule == '2-А' &&
            employee.slug != 'master');

        const notTeamEmployees = this.employees.filter(employee =>
            (employee.team != this.employee[0].team &&
            employee.slug != 'boss' &&
            employee.slug != 'master') ||
            (employee.schedule == '5-Б-1' &&
            employee.slug != 'master') ||
            employee.schedule == '9');

        this.notTeamWorkers.push(...notTeamEmployees);
        
        if (this.production.length == 0)
            this.production.push(newAreas);

        if (this.timesheet.length == 0)
            this.timesheet.push(this.teamWorkers);
    },
}
</script>

<template>
    <div class="container">

        <div v-if="this.shift.length > 0">

            <div class="text-secondary fw-bold small mt-3">Информация о смене</div>
            <div>{{ this.shift[0].day }}, смена {{ this.shift[0].number }}, бригада {{ this.shift[0].team }}</div>

            <div class="text-secondary fw-bold small mt-3">Мастер участка</div>
            <div>{{ employee[0].fullname }}</div>
        </div>

        <DateForm   :shift="shift"
                    :employee="employee"
                    v-if="this.shift.length == 0" />

        <ReportModal    :production="production"
                        :reportBtn="reportBtn"    
                        :shift="shift"
                        :timesheet="timesheet"
                        v-if="this.shift.length > 0"/>
                    
        <TimeSheetModal :sheetBtn="sheetBtn"
                        :shift="shift"
                        :timesheet="timesheet"
                        v-if="this.shift.length > 0"/>

        <AddModal   :notTeamWorkers="notTeamWorkers"
                    :shift="shift"
                    :timesheet="timesheet"
                    v-if="this.shift.length > 0"/>

    </div>
</template>

<style scoped>
.container {
    margin-top: 80px;
}
</style>