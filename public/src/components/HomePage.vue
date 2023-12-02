<script>
import axios from 'axios';
import PackResidueChart from './charts/PackResidueChart.vue';
import PackPlanChart from './charts/PackPlanChart.vue';
import FastenPlanChart from './charts/FastenPlanChart.vue';
import SheetTable from './tables/SheetTable.vue';
import BookTable from'./tables/BookTable.vue';
import TeamTable from './tables/TeamTable.vue';

export default {
    name: 'HomePage',
    components: { 
        PackResidueChart, 
        PackPlanChart, 
        FastenPlanChart,
        SheetTable,
        BookTable,
        TeamTable,
    },
    data() {
        return {
            employees: [],
            report: [],
            master: '',
            date: '',
            shift: '',
            team: '',
            loaded: false,
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            this.employees = dataBaseEmployees.data;
            this.report = dataBaseReport.data;

        } catch (error) {
            console.log(error);
        }

        this.date = this.report[0].date;
        this.shift = this.report[0].shift;
        this.team = this.report[0].team;
        
        this.master = this.employees.filter(employee => 
            employee.team == this.team &&
            employee.slug == 'master')[0].fullname;

        this.loaded = true;
    },

}
</script>

<template>
    <div class="container">

        <div v-if="!loaded" class="loading__spinner d-flex align-items-center text-secondary px-5">
            <strong role="status">Идет загрузка...</strong>
            <div class="spinner-border ms-auto" aria-hidden="true"></div>
        </div>

        <div v-if="loaded" class="row">
            <div class="col-md-9 col-lg-7 col-xl-6 col-xxl-5">

                <div class="text-secondary fw-bold small">Структурное подразделение</div>
                <div>ЛПЦ-5 ПАО ММК</div>

                <div class="text-secondary fw-bold small mt-3">Информация о смене</div>
                <div>{{ date }}, смена {{ shift }}, бригада {{ team }}</div>

                <div class="text-secondary fw-bold small mt-3">Мастер участка</div>
                <div class="small">{{ master }}</div>

                <SheetTable />

                <PackPlanChart />
                <FastenPlanChart />
                <PackResidueChart />
       
                <BookTable />
                <TeamTable />

            </div>
        </div>
    </div>
</template>

<style scoped>
.container { margin-top: 80px; }

.bg__color {
    background: #fef3e0;
}
</style>