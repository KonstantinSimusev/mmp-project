<script>
import axios from 'axios';

import { Bar } from 'vue-chartjs';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    Colors,
} from 'chart.js';

ChartJS.register(
    CategoryScale, 
    LinearScale,
    BarElement, 
    Title, 
    Tooltip, 
    Legend, 
    Colors,
);

class Book {
    constructor(team, total) {
        this.team = team;
        this.total = total;
    }
}


export default {
    name: 'PackerChart',
    components: { Bar },
    props: [],
    data() {
        return {
            employees: [],          
            teams: [
                'Бригада 1',
                'Бригада 2',
                'Бригада 3',
                'Бригада 4',
            ],
            loaded: false,
            data: {
                labels: [],
                datasets: [
                    {
                        label: 'Производство, шт',
                        data: [],
                        backgroundColor: 'rgba(47, 79, 79, 0.8)',
                    },
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false,
                    },
                },
                scales: {
                    yAxes: {
                        display: false
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        display: false
                    }
                }         
            }
        }
    },
    async mounted() {
        this.loaded = false;

        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            this.employees = dataBaseEmployees.data;

            this.loaded = true;
        }
        catch (error) {
            console.log(error);
        }

        const book = this.teams.map(team =>
            new Book(
                team,
                this.employees.filter(employee =>
                    employee.team == team.at(-1) &&
                    employee.profession == 'УКЛАДЧИК - УПАКОВЩИК' &&
                    employee.schedule == '2-А' &&
                    employee.slug != 'master').length
            )
        ).map(team => team.total);

        this.data.labels.push(...this.teams);
        this.data.datasets[0].data.push(...book);
    },
}
</script>

<template>
    <div class="wrapper mt-5 text-center shadow p-4 bg__color rounded-4">

        <Bar    :data="data" 
                :options="options"
                v-if="loaded" />
    </div>
</template>

<style scoped>
.bg__color {
    background: rgba(237, 237, 237, 0.5);
}
</style>
