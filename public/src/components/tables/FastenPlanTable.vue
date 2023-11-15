<script>
import axios from 'axios';

class Area {
    constructor(id, title, unit, plan, workersCount) {
        this.id = id;
        this.title = title;
        this.unit = unit;
        this.plan = plan;
        this.workersCount = workersCount;
    }
}

export default {
    name: 'FastenPlanTable',
    props: [],
    data() {
        return {
            areas: [],
            baseAreas: [],
            professions: [],
            production: [],
            timesheets: [],
        }
    },
    async mounted() {
        try {
            const dataBaseAreas = await axios
                .get('http://127.0.0.1:8000/api/area/?format=json');
            
            const dataBaseProfessions = await axios
                .get('http://127.0.0.1:8000/api/profession/?format=json');

            const dataBaseReport = await axios
                .get('http://127.0.0.1:8000/api/report/?format=json');

            const dataBaseTimeSheets = await axios
                .get('http://127.0.0.1:8000/api/timesheet/?format=json');
            
            this.baseAreas = dataBaseAreas.data;
            this.professions = dataBaseProfessions.data;
            this.production = dataBaseReport.data;
            this.timesheets = dataBaseTimeSheets.data;
        }
        catch (error) {
            console.log(error);
        }

        const packAreas = this.baseAreas.filter(area => area.slug == 'fasten');
    
        const teamSheet = this.timesheets.filter(sheet => 
            sheet.team == this.production[0].team)[0].timesheet;

        const newAreas = packAreas.map(area =>
            new Area(
                area.id,
                area.title,
                area.unit,

                // area.plan
                Number(JSON.parse(this.production[0].report)
                    .filter(reportArea => reportArea.title == area.title)[0].plan), 

                // area.workersCount
                JSON.parse(teamSheet)
                    .filter(report => 
                        report.area == area.title &&
                        report.profession == 'ШТАБЕЛИРОВЩИК МЕТАЛЛА' &&
                        report.presence == 'ЯВКА').length,
            )
        );

        this.areas = newAreas.filter(area => area.plan != 0 || area.workersCount != 0);
    }, 
}
</script>

<template>
    <div class="wrapper">
        <table class="mx-auto table table-hover table-sm align-middle small w-75 mb-4">
            <thead class="small text-center">
                <tr>
                    <th class="text-light bg__header__color">Участок</th>
                    <th class="text-light bg__header__color">шт</th>
                    <th class="text-light bg__header__color">Чел</th>
                </tr>
            </thead>
            <tbody class="text-center small">
                <tr v-for="area in this.areas.sort((a,b) => a.id - b.id)" :key="area">
                    <td>{{ area.title }}</td>
                    <td>{{ area.plan }}</td>
                    <td>{{ area.workersCount }}</td>
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