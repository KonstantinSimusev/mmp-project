<script>
import axios from 'axios';

class TeamProfession {
    constructor(title, probation, presence, total) {
        this.title = title;
        this.probation = probation;
        this.presence = presence;
        this.total = total;
    }
}

class Profession {
    constructor(title, probation, presence) {
        this.title = title;
        this.probation = probation;
        this.presence = presence;
    }
}

export default {
    name: 'SheetTable',
    props: [],
    data() {
        return {
            employees: [],
            report: [],
            timesheets: [],
            team: '',
            timesheet: [],
            professions: [],
        }
    },
    async mounted() {
        try 
        {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            const dataBaseTimeSheets = await axios
                .get('http://127.0.0.1:8000/api/timesheet/?format=json');

            this.employees = dataBaseEmployees.data;
            this.report = dataBaseReport.data;
            this.timesheets = dataBaseTimeSheets.data;
        }
        catch (error) {
            console.log(error);
        }

        this.team = this.report[0].team;

        const sheet = this.timesheets.filter(sheet =>
            sheet.team == this.team);

        const parseSheet = JSON.parse(sheet[0].timesheet);
        
        // создаем массив неповторяющихся объектов
        const strSheet = parseSheet.map(worker => 
            worker.profession + '__' +
            worker.probation + '__' +
            worker.presence
        ).filter((element, index, array) =>
            array.indexOf(element) === index)
            .sort((a, b) => a > b ? 1 : -1)
            .map(element => element.split('__'));

        this.professions = strSheet.map(array =>
            new Profession(
                array[0],
                array[1],
                array[2],
            )
        );

        console.log(this.professions);

        const newTeamProfessions = this.professions.map(profession =>
            new TeamProfession(
                profession.title,
                this.createProbation(profession.probation),
                profession.presence,
                parseSheet.filter(sheet =>
                    sheet.profession == profession.title &&
                    sheet.probation == profession.probation &&
                    sheet.presence == profession.presence).length
            )
        );

        this.timesheet = newTeamProfessions.filter(profession =>
            profession.total != 0);
    },
    methods: {
        createProbation(probation) {
            if (probation == 'СТАЖЕР')
                return probation;
            else
                return probation = '';
        }
    } 
}
</script>

<template>
    <div class="wrapper mt-5">
        <div class="row">
            <div class="text-secondary fw-bold small">Табель. Бригада {{ this.team }}</div>
        </div>
        <div class="row mt-2">
            <div class="col">
                

        <table class="table table-hover table-sm align-middle small mb-4">
            <thead class="small">
                <tr>
                    <th class="text-light bg__header__color ps-2">Профессия</th>
                    <th class="text-center text-light bg__header__color"></th>
                    <th class="text-center text-light bg__header__color">Статус</th>
                    <th class=" text-center text-light bg__header__color">Чел</th>
                </tr>
            </thead>
            <tbody class="small">
                <tr v-for="profession in this.timesheet" :key="profession">
                    <td class="ps-2">{{ profession.title }}</td>
                    <td class="text-center">{{ profession.probation }}</td>
                    <td class="text-center">{{ profession.presence }}</td>
                    <td class="text-center">{{ profession.total }}</td>
                </tr>
            </tbody>
            <tfoot class="table-secondary">
                <tr >
                    <th colspan="4" class="text-end pe-3 small">Итого: {{ this.timesheet.length }}</th>
                </tr>
            </tfoot>
        </table>                
            </div>
        </div>
    </div>
</template>

<style scoped>
.bg__header__color {
    background: #3d3d3d;
}
</style>