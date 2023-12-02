<script>
import axios from 'axios';


class Profession {
    constructor(id, title, count) {
        this.id = id;
        this.title = title;
        this.count = count;
    }
}


class TeamProfession {
    constructor(title, teams) {
        this.title = title;
        this.teams = teams;
    }
}


class TeamCount {
    constructor(number, total) {
        this.number = number;
        this.total = total;
    }
}


export default {
    name: 'BookTable',
    data() {
        return {
            employees: [],
            professions: [],
            teamProfessions: [
                'УКЛАДЧИК - УПАКОВЩИК',
                'ШТАБЕЛИРОВЩИК МЕТАЛЛА',
                'ШТАМПОВЩИК',
            ],
            teams: [1, 2, 3, 4],
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseProfessions = await axios
                .get('http://127.0.0.1:8000/api/profession/?format=json');
            
            this.employees = dataBaseEmployees.data;
            this.professions = dataBaseProfessions.data;
        }
        catch (error) {
            console.log(error);
        }
        
        this.professions = this.professions.map(profession =>
            new Profession(
                profession.id,
                profession.name,
                this.employees.filter(employee => 
                    employee.slug == profession.slug).length
            )
        );
        
        this.teams = this.teams.map(team =>
            new TeamCount(
                team,
                this.employees.filter(employee =>
                    employee.team == team &&
                    employee.schedule == '2-А' &&
                    employee.slug != 'master').length
            )
        );

        this.teamProfessions = this.teamProfessions.map(profession =>
            new TeamProfession(
                profession,
                this.teams.map(team =>
                    new TeamCount (
                        team,
                        this.employees.filter(employee =>
                            employee.profession == profession &&
                            employee.team == team.number &&
                            employee.schedule == '2-А' &&
                            employee.slug != 'master').length
                    )
                )
            )
        );
    }, 
}
</script>

<template>
    <div class="wrapper mt-5">

        <div class="text-center text-secondary fw-bold small">Книга личного состава</div>

        <div class="row mt-3">
            <div class="col">
                
                <table class="table table-hover table-sm align-middle small mb-4">
                    <thead class="small">
                        <tr>
                            <th class="text-light bg__header__color text-center">#</th>
                            <th class="text-light bg__header__color">Профессия</th>
                            <th class="text-light bg__header__color text-center">Чел</th>
                        </tr>
                    </thead>
                    <tbody class="small">
                        <tr v-for="(profession, number) in this.professions.sort((a,b) => a.id - b.id)" :key="profession">
                            <th class="text-center">{{ number + 1 }}</th>    
                            <td>{{ profession.title }}</td>
                            <td class="text-center">{{ profession.count }}</td>
                        </tr>
                    </tbody>
                    <tfoot class="table-secondary small">
                        <tr>
                            <th colspan="2" class="text-end">Итого:</th>
                            <th class="text-center">{{ employees.length }}</th>
                        </tr>
                    </tfoot>
                </table> 

            </div>
        </div>

        <div class="row mt-3">
            <div class="col">
                <div class="text-center text-secondary fw-bold small">Состав бригады (КЛС)</div>

                <table class="table table-hover table-sm align-middle small mt-3">
                    <thead class="small">
                        <tr>
                            <th class="text-light bg__header__color ps-2">Профессия</th>
                            <th v-for="team in this.teams" :key="team" class="text-light bg__header__color text-center">бр{{ team.number }}</th>
                        </tr>
                    </thead>
                    <tbody class="small">
                        <tr v-for="profession in this.teamProfessions" :key="profession">
                            <td class="ps-2">{{ profession.title }}</td>
                            <td v-for="team in profession.teams" :key="team" class="text-center">{{ team.total }}</td>
                        </tr>
                    </tbody>
                    <tfoot class="table-secondary small">
                        <tr>
                            <th class="ps-2 text-end">Итого:</th>
                            <th v-for="team in this.teams" :key="team" class="text-center">{{ team.total }}</th>
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