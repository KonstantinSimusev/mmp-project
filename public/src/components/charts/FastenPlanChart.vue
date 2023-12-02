<script>
import axios from 'axios';

import FastenPlanTable from '../tables/FastenPlanTable.vue';

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

export default {
    name: 'FastenPlanChart',
    components: { 
        Bar,
        FastenPlanTable
    },
    props: [],
    data() {
        return {
            production: [],
            areas: [],
            visible: true,
            loaded: false,
            data: {
                labels: [],
                datasets: [
                    {
                        label: 'Отгрузка, ваг',
                        data: [],
                        backgroundColor: 'rgba(112, 128, 144, 0.8)',
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
                        },
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
            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            this.production = dataBaseReport.data;
            
            this.loaded = true;
        }
        catch (error) {
            console.log(error);
        }

        this.areas = JSON.parse(this.production[0].report)
            .filter(area => area.slug == 'fasten');

        const packLabels = this.areas.map(area => area.title);
        const planPackData = this.areas.map(area => area.plan);

        const summa = planPackData.reduce((sum, next) => sum + Number(next));

        if (summa == 0)
            this.visible = false;

        this.data.labels.push(...packLabels);
        this.data.datasets[0].data.push(...planPackData);
    },
}
</script>

<template>
    <div class="wrapper mt-5 text-center shadow p-4 rounded-4">
        
        <div class="text-secondary fw-bold small mb-2">Планируемая отгрузка</div>

        <div class="small" v-if="!visible">Нет отгрузки</div>

        <FastenPlanTable v-if="visible" />
            
        <Bar    :data="data" 
                :options="options"
                v-if="loaded && visible" />

    </div>
</template>

<style scoped>
.bg__color {
    background: rgba(237, 237, 237, 0.5);
}
</style>
