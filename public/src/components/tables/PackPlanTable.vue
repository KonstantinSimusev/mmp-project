<script>
import axios from 'axios';

class Area {
    constructor(
        id, 
        title, 
        productionCount, 
        workerCount,
        probationCount,
        ) {
        this.id = id;
        this.title = title;
        this.productionCount = productionCount;
        this.workerCount = workerCount;
        this.probationCount = probationCount;
    }
}

export default {
    name: 'PackPlanTable',
    data() {
        return {
            area: 'НТА (к)',
            packer: 'УКЛАДЧИК - УПАКОВЩИК',
            stacker: 'ШТАБЕЛИРОВЩИК МЕТАЛЛА',
            presence: 'ЯВКА',
            probation: 'СТАЖЕР',
            slug: 'pack',
            production: [],
            areas: [],
            baseAreas: [],
            timesheets: [],
        }
    },
    async mounted() {
        try {
            const dataBaseAreas = await axios
                .get('http://127.0.0.1:8000/api/area/?format=json');

            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            const dataBaseTimeSheets = await axios
                .get('http://127.0.0.1:8000/api/timesheet/?format=json');
            
            this.baseAreas = dataBaseAreas.data;
            this.production = dataBaseReport.data;
            this.timesheets = dataBaseTimeSheets.data;
        }
        catch (error) {
            console.log(error);
        }

        const baseReport = this.production[0].report;
        const baseSheet = this.timesheets.filter(sheet => 
            sheet.team == this.production[0].team)[0].timesheet;

        const parseReport = JSON.parse(baseReport);
        const parseSheet = JSON.parse(baseSheet);

        const packAreas = parseReport.filter(area => area.slug == this.slug);

        const newAreas = packAreas.map(area =>
            new Area(
                area.id,
                area.title,
                area.plan,
                this.countWorkers(area.title, parseSheet),
                this.countProbationers(area.title, parseSheet),
            )
        );

        this.areas = newAreas.filter(area => 
            area.productionCount != 0);
    },
    methods: {
        countWorkers(area, timesheet) {
            let total = ''

            if (area != this.area)
                total = this.countPacker(area, timesheet);
            else
                total = this.countStacker(area, timesheet);

            if(total == 0)
                total = '-';

            return total;
        },
        countProbationers(area, timesheet) {
            let total = ''

            if (area != this.area)
                total = this.countProbationPacker(area, timesheet);
            else
                total = this.countProbationStacker(area, timesheet);

            if(total == 0)
                total = '-';

            return total;
        },
        countPacker(area, timesheet) {
            const total = timesheet.filter(report =>
                report.area == area &&
                report.profession == this.packer &&
                report.presence == this.presence &&
                report.probation != this.probation
            ).length;

            return total;
        },
        countStacker(area, timesheet) {
            const total = timesheet.filter(report =>
                report.area == area &&
                report.profession == this.stacker &&
                report.presence == this.presence &&
                report.probation != this.probation
            ).length;

            return total;
        },
        countProbationPacker(area, timesheet) {
            const total = timesheet.filter(report =>
                report.area == area &&
                report.profession == this.packer &&
                report.presence == this.presence &&
                report.probation == this.probation
            ).length;

            return total;
        },
        countProbationStacker(area, timesheet) {
            const total = timesheet.filter(report =>
                report.area == area &&
                report.profession == this.stacker &&
                report.presence == this.presence &&
                report.probation == this.probation
            ).length;

            return total;
        },
    } 
}
</script>

<template>
    <div class="wrapper">
        <table class="mx-auto table table-hover table-sm align-middle small w-75 mb-4">
            <thead class="text-center small">
                <tr>
                    <th class="text-light bg__header__color">Участок</th>
                    <th class="text-light bg__header__color">шт</th>
                    <th class="text-light bg__header__color">Чел</th>
                    <th class="text-light bg__header__color">Стажер</th>
                </tr>
            </thead>
            <tbody class="text-center small">
                <tr v-for="area in this.areas" :key="area">
                    <td>{{ area.title }}</td>
                    <td>{{ area.productionCount }}</td>
                    <td>{{ area.workerCount }}</td>
                    <td>{{ area.probationCount }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.bg__header__color {
    background: #3d3d3d;
}
</style>