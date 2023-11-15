<script>
import axios from 'axios';

class Area {
    constructor(id, title, unit, residue) {
        this.id = id;
        this.title = title;
        this.unit = unit;
        this.residue = residue;
    }
}

export default {
    name: 'PackResidueTable',
    props: [],
    data() {
        return {
            areas: [],
            baseAreas: [],
            professions: [],
            production: [],
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
            
            this.baseAreas = dataBaseAreas.data;
            this.professions = dataBaseProfessions.data;
            this.production = dataBaseReport.data;
        }
        catch (error) {
            console.log(error);
        }
        
        const packAreas = this.baseAreas.filter(area => area.slug == 'pack');

        const newAreas = packAreas.map(area =>
            new Area(
                area.id,
                area.title,
                area.unit,

                // area.residue
                Number(JSON.parse(this.production[0].report)
                    .filter(reportArea => reportArea.title == area.title)[0].residue), 
            )
        );

        this.areas = newAreas.filter(area => area.residue != 0);
    }, 
}
</script>

<template>
    <div class="wrapper">
        <table class="mx-auto table table-hover table-sm align-middle small w-50 mb-4">
            <thead class="small text-center">
                <tr>
                    <th class="text-light bg__header__color">Участок</th>
                    <th class="text-light bg__header__color">шт</th>
                </tr>
            </thead>
            <tbody class="small text-center">
                <tr v-for="area in this.areas.sort((a,b) => a.id - b.id)" :key="area">
                    <td>{{ area.title }}</td>
                    <td>{{ area.residue }}</td>
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