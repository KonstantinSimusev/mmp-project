<script>
import axios from 'axios';

class SickProfession {
    constructor(name, workers) {
        this.name = name;
        this.workers = workers;
    }
}

class SickWorker {
    constructor(name, profession, team) {
        this.name = name;
        this.profession = profession;
        this.team = team;
    }
}

export default {
    name: 'SickTable',
    props: [],
    data() {
        return {
            employees:[],
            professions: [],
            sicksInfo: [],
            sicksList: [],
            sickWorkers: [],
            sickWorkersName: [],
            sumSicks: [],
            timesheet: [],
            timesheets: []
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseProfessions = await axios
                .get('http://127.0.0.1:8000/api/profession/?format=json');

            const dataBaseTimeSheets = await axios
                .get('http://127.0.0.1:8000/api/timesheet/?format=json');

            this.employees = dataBaseEmployees.data;
            this.professions = dataBaseProfessions.data;
            this.timesheets = dataBaseTimeSheets.data;
        }
        catch (error) {
            console.log(error);
        }

        this.timesheet = this.timesheets.map(teams => 
            JSON.parse(teams.timesheet)).flat();

        this.sickWorkersName = this.timesheet.filter(employee => 
            employee.presence == 'Б');

        this.sickWorkers = this.sickWorkersName.map(worker =>
            new SickWorker(
                worker.fullname,
                worker.profession,
                this.employees.filter(employee => 
                    worker.fullname == employee.fullname)[0].team
            )
        );

        this.sicksInfo = this.professions.map(profession =>
            new SickProfession(
                profession.name,
                this.sickWorkers.filter(worker => 
                    worker.profession == profession.name)
            )
        );

        this.sicksList = this.sicksInfo.filter(sick => sick.workers.length > 0);
        
        const flatSicksList = this.sicksList.flat();
        this.sumSicks = flatSicksList.map(sum => sum.workers).flat().length;
    },  
}
</script>

<template>
    <div class="wrapper mt-4 shadow mt-4 px-4 p-3  bg__color rounded-4">
        <div class="text-secondary text-center fw-bold small pb-2">Временная нетрудоспособность</div>
 
        <table class="table table-bordered table-hover table-sm align-middle small">
            <thead class="table-success">
                <tr>
                    <th class="text-center">Профессия</th>
                    <th class="text-center">Чел</th>
                </tr>
            </thead>
            <tbody class="table-light">
                <tr v-for="profession in this.sicksList" :key="profession">
                    <td class="text-center">{{ profession.name }}</td>  
                    <td class="text-center">{{ profession.workers.length }}</td>
                </tr>
            </tbody>
            <tfoot class="table-secondary">
                <tr>
                    <th colspan="3" class="text-end pe-2">Итого: {{ sumSicks }}</th>
                </tr>
            </tfoot>
        </table>

    </div>
</template>

<style scoped>
.bg__color {
    background: rgba(237, 237, 237, 0.5);
}
</style>