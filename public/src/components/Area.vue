<script>
import axios from 'axios';

export default {
    name: 'Area',
    props: [
        'nameOptions',
        'notTeamWorkers',
        'production', 
        'teamWorkers',
    ],
    data() {
        return {
            areas: [],
        }
    },
    async mounted() {
        try {
            const dataBaseAreas = await axios
                .get('http://127.0.0.1:8000/api/area/?format=json');
            
            this.areas = dataBaseAreas.data;

        } catch (error) {
            console.log(error);
        }

        this.createAreas();
    },
    methods: {
        checkArea(chooseArea) {
            const checkArea = this.production.filter(area =>
                area == chooseArea);

            const error = checkArea.filter(area =>
                ((area.plan > 0 || area.residue > 0) && area.addWorkers.length == 0) ||
                (area.plan == 0 && area.residue == 0 && area.addWorkers.length > 0)).length;

            if (error > 0)
                checkArea[0].error = true;
            else
                checkArea[0].error = false;
        },

        deleteWorker(worker, array) {
            const workers = [];

            workers.push(...this.teamWorkers);
            workers.push(...this.notTeamWorkers);

            const employee = workers.filter(employee =>
                employee.initials == worker)[0];

            employee.visible = true;

            const index = array.findIndex(name =>
                name == worker);

            if (index !== -1)
                array.splice(index, 1);
        },

        addAreaName(worker, addWorkers) {
            if (worker !== 'Выберите работника') {

                const fullname = this.getWorker(worker).initials;
                
                const repeatAreaNames = addWorkers.filter(name =>
                    name == fullname);
                
                const areaWorkers = this.production.map(area =>
                    area.addWorkers).flat();

                const repeatAreasNames = areaWorkers.filter(name =>
                    name == fullname);

                if (repeatAreaNames.length == 0 && repeatAreasNames == 0)
                    addWorkers.push(fullname);
                    
                addWorkers.sort();

                this.getWorker(worker).visible = false;
            }
        },

        getWorker(worker) {
            const workers = [];

            workers.push(...this.teamWorkers);
            workers.push(...this.notTeamWorkers);

            const employee = workers.filter(employee =>
                employee.fullname == worker)[0];

            return employee;
        },
        
        createAreas() {
            let newArea = {};
            const newAreas = this.areas.map(area => 
                newArea = {
                    id: area.id,
                    slug: area.slug,
                    title: area.title,
                    unit: area.unit,
                    plan: '',
                    residue: '',
                    workerName: 'Выберите работника',
                    addWorkers: [],
                    info: 'Измените поле',
                    error: false,
                }
            );

            if (this.production.length == 0)
                this.production.push(...newAreas);
        }
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="block__color rounded-4 p-3 mb-5 shadow-sm" v-for="area in this.production.sort((a, b) => a.id - b.id)" :key="area.id">

            <div class="d-flex justify-content-between mt-1 mb-4 align-items-center">
                <div class="small px-3 py-2 rounded-4 text-light fw-bold bg-secondary">{{ area.title }}</div>
                <div v-if="area.error" class="small fw-bold text-danger pe-2">{{ area.info }}</div>
            </div>

            

            <div class="row d-flex mb-3">
                <div class="col">
                    <div class="mb-1 text-secondary small">План, {{ area.unit }} :</div>
                    <input class="form-control ps-3" type="number" placeholder="Введите шт" v-model="area.plan" @input="this.checkArea(area)">
                </div>
                <div class="col">
                    <div class="mb-1 text-secondary small">Остаток, {{ area.unit }} :</div>
                    <input class="form-control ps-3" type="number" placeholder="Введите шт" v-model="area.residue" @input="this.checkArea(area)"> 
                </div>
                
            </div>

            <div>
                <div class="mb-1 text-secondary small">Состав бригады, ФИО :</div>

                <select class="form-control form-select mb-3 ps-3" v-model="area.workerName" @change="this.addAreaName(area.workerName, area.addWorkers), this.checkArea(area)">
                    <option v-for="option in this.nameOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                </select>

                <div class="small" v-for="(worker, number) in area.addWorkers" :key="worker">
                    <div class="d-flex justify-content-between align-items-center border border-secondary p-2 ps-3 rounded mt-2">
                        <div>#{{ number + 1 }} {{ worker }}</div>
                        <button class="btn btn-close btn-sm" @click="this.deleteWorker(worker, area.addWorkers), this.checkArea(area)"></button>
                    </div>                                
                </div>
            </div>   

        </div>

    </div>
</template>

<style scoped>
.block__color { background: #d1d6da; }

input::placeholder { color: #333333; }

input:focus,
button:focus,
select:focus { box-shadow: none }
</style>