<script>
import axios from 'axios';

import PackResidueTable from '../tables/PackResidueTable.vue';

import { Bar } from 'vue-chartjs';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    Colors
} from 'chart.js';

ChartJS.register(
    CategoryScale, 
    LinearScale, 
    BarElement, 
    Title, 
    Tooltip, 
    Legend, 
    Colors
);

export default {
    name: 'PackResidueChart',
    components: {
        Bar,
        PackResidueTable,
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
                        label: 'Остаток, шт',
                        data: [],
                        backgroundColor: 'rgba(210, 105, 30, 0.8)',
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
            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            this.production = dataBaseReport.data;

            this.loaded = true;
        }
        catch (error) {
            console.log(error);
        }

        this.areas = JSON.parse(this.production[0].report)
            .filter(area => area.slug == 'pack');

        const packLabels = this.areas.map(area => area.title);
        const residuePackData = this.areas.map(area => area.residue);

        const summa = residuePackData.reduce((sum, next) => sum + Number(next));

        if (summa == 0)
            this.visible = false;

        this.data.labels.push(...packLabels); 
        this.data.datasets[0].data.push(...residuePackData);
    },
}
</script>

<template>
    <div class="wrapper mt-5 text-center shadow p-4 rounded-4">

        <div class="text-secondary fw-bold small mb-2">Неупакованная продукция</div>

        <div class="small" v-if="!visible">Нет остатков</div>

        <PackResidueTable v-if="visible" />

        <Bar    :data="data" 
                :options="options"
                v-if="loaded && visible" />

    </div>
</template>

<style scoped>

</style>
