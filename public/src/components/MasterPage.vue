<script>
import DateForm from './forms/DateForm.vue';
import ReportModal from './modals/ReportModal.vue';
import AddModal from './modals/AddModal.vue';

export default {
    name: 'MasterPage',
    components: { 
        DateForm, 
        ReportModal,
        AddModal,
    },
    props: [
        'addEmployee',
        'employee', 
        'employees',
        'nameOptions', 
        'notTeamWorkers',
        'production', 
        'reportBtn', 
        'shift',  
        'timesheet',
        'trainees',
        'teamWorkers',
    ],
    mounted() {
        this.createTeamWorkers();
        this.createNotTeamWorkers();
    },
    methods: {
        createNotTeamWorkers() {
            const workers = this.createWorkers().filter(worker =>
                worker.team != this.employee[0].team);

            if (this.notTeamWorkers.length == 0)
                this.notTeamWorkers.push(...workers);
        },

        createTeamWorkers() {
            const workers = this.createWorkers().filter(worker =>
                worker.team == this.employee[0].team &&
                worker.schedule == '2-А');

            if (this.teamWorkers.length == 0)
                this.teamWorkers.push(...workers);
        },

        createWorkers() {
            let newWorker = {};
            const workers = this.employees.filter(employee =>
                employee.slug != 'boss' &&
                employee.slug != 'master');

            const newWorkers = workers.map(worker =>
                newWorker = {
                    id: worker.id,
                    slug: worker.slug,
                    fullname: worker.fullname, 
                    profession: worker.profession, 
                    schedule: worker.schedule, 
                    team: worker.team,
                    area: 'ЛПЦ-5',
                    initials: this.createInitials(worker.fullname),
                    presence: 'Выберите причину',
                    probation: 'ПРОЙДЕНА',
                    info: 'Измените поле',
                    error: true,
                    visible: true,
                }
            )
            return newWorkers;
        },

        createInitials(worker) {
            const string = worker;
            const surname = string.split(' ')[0];
            const initials = string.split(' ')[1][0] + string.split(' ')[2][0];
            const fullname = surname + ' ' + initials;

            return fullname;
        },
    }
}
</script>

<template>
    <div class="container">

        <div class="text-secondary fw-bold small mt-3">Мастер участка</div>
        <div>{{ employee[0].fullname }}</div>

        <div v-if="this.shift.length > 0">
            <div class="text-secondary fw-bold small mt-3">Информация о смене</div>
            <div v-if="this.shift.length > 0">{{ this.shift[0].day }}, смена {{ this.shift[0].number }}, бригада {{ this.shift[0].team }}</div>
        </div>

        <DateForm   
            :shift="shift"
            :employee="employee"
            v-if="this.shift.length == 0" />

        <ReportModal
            :addEmployee="addEmployee"
            :employee="employee"
            :employees="employees"
            :nameOptions="nameOptions"
            :notTeamWorkers="notTeamWorkers"
            :production="production"
            :reportBtn="reportBtn"    
            :shift="shift"
            :timesheet="timesheet"
            :trainees="trainees"
            :teamWorkers="teamWorkers"
            v-if="this.shift.length > 0" />

        <AddModal    
            :addEmployee="addEmployee"
            :employee="employee"
            :employees="employees"
            :notTeamWorkers="notTeamWorkers"
            v-if="this.shift.length > 0" />

    </div>
</template>

<style scoped>
.container { margin-top: 80px; }
</style>