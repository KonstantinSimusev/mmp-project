<script>

import { Doughnut } from 'vue-chartjs';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    Title,
    Tooltip,
    Legend,
    Colors,
    ArcElement
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, Title, Tooltip, Legend, Colors, ArcElement);

export default {
    name: 'Stacker',
    components: { Doughnut },
    props: ['employees'],
    data() {
        return {
            loaded: false,
            data: {
                labels: [
                    `бр 1 ( ${this.countWorkers(1)} )`, 
                    `бр 2 ( ${this.countWorkers(2)} )`,
                    `бр 3 ( ${this.countWorkers(3)} )`,
                    `бр 4 ( ${this.countWorkers(4)} )`,
                ],
                datasets: [
                    {
                        data: [
                            this.countWorkers(1),
                            this.countWorkers(2),
                            this.countWorkers(3),
                            this.countWorkers(4),
                        ],
                        // backgroundColor: 'rgba(205, 92, 92, 0.6)',
                    },
                    // {
                    //     label: 'Укладчик-упаковщик, чел',
                    //     data: [
                    //         this.teamOne(1, 'Штамповщик'),
                    //         this.teamOne(2, 'Штамповщик'),
                    //         this.teamOne(3, 'Штамповщик'),
                    //         this.teamOne(4, 'Штамповщик'),
                    //     ],
                    //     backgroundColor: 'rgba(128, 128, 128, 0.6)',
                    // },
                ]
            },
            options: {
                hoverOffset: 4,
                plugins: {
                    title: {
                        display: true,
                        // position: "right",
                        text: "Штабелировщик металла",
                        font: {
                            size: 20
                        }
                    },
                    legend: {
                        position: "right",
                        // align: "center"
                    },
                    tooltip: {
                        // enabled: true,
                        // usePointStyle: true,
                        // position: 'nearest',
                        // external: externalTooltipHandler
                    }
    }
            }
        }
    }, 
    methods: {
        countWorkers(teamNumber) {
            const numbers = this.employees.filter(employee =>
            employee.team == teamNumber && employee.profession == 'Штабелировщик металла');
            return numbers.length;
        }
    }
}
</script>

<template>
    <div class="container w-75">
        <Doughnut  :data="data" :options="options" />
    </div>
</template>

<style scoped>

</style>
