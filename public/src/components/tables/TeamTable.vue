<script>
import axios from 'axios';


class ProfessionView {
    constructor(title, options) {
        this.title = title;
        this.options = options;
    }
}


class Option {
    constructor(title, total, teams) {
        this.title = title;
        this.total = total;
        this.teams = teams;
    }
}


class Total {
    constructor(total) {
        this.total = total;
    }
}


export default {
    name: 'TeamTable',
    components: {},
    props: [],
    data() {
        return {
            employees: [],
            timesheets: [],
            info: [],
            teams: [1, 2, 3, 4],
            options: [
                'КЛС',
                'ОТ',
                'Б',
                'СТАЖЕР'
            ],
            professions: [
                'УКЛАДЧИК - УПАКОВЩИК',
                'ШТАБЕЛИРОВЩИК МЕТАЛЛА',
                'ШТАМПОВЩИК',
            ],
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseTimeSheets = await axios
                .get('http://127.0.0.1:8000/api/timesheet/?format=json');

            this.employees = dataBaseEmployees.data;
            this.timesheets = dataBaseTimeSheets.data;
        }
        catch (error) {
            console.log(error);
        }
        
        


        this.info = this.professions.map(profession =>
            new ProfessionView(
                // title
                profession,
                // options
                this.options.map(option =>
                    new Option(
                        //title
                        option,
                        // total
                        this.countTotal(profession, option, this.timesheets),
                        // teams
                        this.countTeamTotal(profession, option, this.teams, this.timesheets)
                    )
                )
            )
        );
    },
    methods: {
        countTotal(profession, option, timesheets) {
            let total = 0;

            if (option != 'КЛС') {
                total = timesheets
                    .map(sheet => JSON.parse(sheet.timesheet))
                    .flat()
                    .filter(team => 
                        team.profession == profession &&
                        team.presence == option).length
            } else {
                total = timesheets
                    .map(sheet => JSON.parse(sheet.timesheet))
                    .flat()
                    .filter(team => 
                        team.profession == profession).length
            }

            if (total == 0)
                total = '-';

            return total;
        },
        countTeamTotal(profession, option, teams, timesheets) {
            let totals = [];

            if (option != 'КЛС') {
                totals = teams.map(team =>
                    new Total(
                        timesheets
                            .map(team => JSON.parse(team.timesheet))
                            .flat()
                            .filter(sheet => 
                                sheet.profession == profession &&
                                sheet.team == team &&
                                sheet.presence == option).length
                    )
                )
            } else {
                totals = teams.map(team =>
                    new Total(
                        timesheets
                            .map(team => JSON.parse(team.timesheet))
                            .flat()
                            .filter(sheet => 
                                sheet.profession == profession &&
                                sheet.team == team).length
                    )
                )
            }

            totals = totals.map(element =>
                new Total(
                    this.isNull(element.total)
                )
            );

            return totals;
        },
        isNull(number) {
            if (number == 0)
                number = '-';
            return number;
        }
    }     
}
</script>

<template>
    <div class="wrapper mt-3">

        <div v-for="profession in this.info" :key="profession" class="text-center">
            
        <div class="text-secondary fw-bold small">
            <div>Учаток упаковки металлопродукции ЛПЦ-5</div>
            <div>{{ profession.title }}</div>
        </div>

        <table class="mx-auto table table-bordered table-hover table-sm align-middle small mt-2">
            <thead class="table-success">   
                <tr>
                    <th class="text-center small">Показатель</th>
                    <th class="text-center small">бр1</th>
                    <th class="text-center small">бр2</th>
                    <th class="text-center small">бр3</th>
                    <th class="text-center small">бр4</th>
                    <th class="text-center small">Итого</th>
                </tr>
            </thead>
            <tbody class="table-light">
                <tr v-for="option in profession.options" :key="option">
                    <td>{{ option.title }}</td>
                    <td v-for="team in option.teams" :key="team" class="text-center small">{{ team.total }}</td>
                    <th class="text-center table-secondary">{{ option.total }}</th>
                </tr>
            </tbody>
        </table>

        </div>


    </div>
</template>

<style scoped>
.bg__color {
    background: rgba(237, 237, 237, 0.8);
}
</style>