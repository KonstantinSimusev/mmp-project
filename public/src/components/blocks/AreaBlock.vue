<script>
import axios from 'axios';

export default {
    name: 'AreaBlock',
    props: [
        'addedWorkers',
        'employee',
        'employees',
        'production', 
        'timesheet',
    ],
    data() {
        return {
            areas: [],
            nameOptions: [],
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

        this.createEmployeeInitials();
        this.createAreas();
        this.createWorkerNames();
    },
    methods: {
        // checkArea(chooseArea) {
        //     const checkArea = this.production.filter(area =>
        //         area == chooseArea);

        //     const error = checkArea.filter(area =>
        //         ((area.plan > 0 || area.residue > 0) && area.addWorkers.length == 0) ||
        //         (area.plan == 0 && area.residue == 0 && area.addWorkers.length > 0)).length;

        //     if (error > 0)
        //         checkArea[0].error = true;
        //     else
        //         checkArea[0].error = false;
        // },

        deleteWorker(worker, arrayOne, arrayTwo) {
            const index = arrayOne.findIndex(item =>
                item === worker);

            if (index !== -1) {
                arrayOne.splice(index, 1);
                arrayTwo.splice(index, 1);
                this.updateTimesheet(worker, this.timesheet, true)
            }
        },

        addWorker(worker, arrayOne, arrayTwo) {
            if (worker != 'Выберите ФИО') {
                const initials = this.createInitials(worker);
                const addedWorkers = this.production.map(area =>
                    area.workerInitials).flat();
                const addedWorker = addedWorkers.filter(name =>
                    name == initials);

                if (addedWorker.length == 0) {
                    arrayOne.push(initials);
                    arrayTwo.push(worker);
                    this.updateTimesheet(initials, this.timesheet, false);
                }
            }
        },

        updateTimesheet(worker, array, bool) {
            array.forEach(employee => {
                if (employee.initials === worker)
                    employee.visible = bool;
            });
        },

        createEmployeeInitials() {
            this.employees.forEach(employee => {
                employee.initials = this.createInitials(employee.fullname);
            });
        },

        createInitials(worker) {
            const string = worker;

            const surname = string.split(' ')[0];
            const initials = string.split(' ')[1][0] + string.split(' ')[2][0];
            const fullname = surname + ' ' + initials;

            return fullname;
        },
        
        createWorkerNames() {
            let optionName = {};
            let options = [];
            let names = this.getTeamWorkers().map(worker => 
                worker.fullname);

            names.push(...this.addedWorkers);
            names.sort();

            options.push('Выберите ФИО');
            options.push(...names);
            
            this.nameOptions = options.map(name => 
                optionName = { value: name });
        },

        getTeamWorkers() {
            const workers = this.employees.filter(employee =>
                employee.slug != 'boss' &&
                employee.slug != 'master' &&
                employee.team == this.employee[0].team &&
                employee.schedule == '2-А');

            return workers;
        },
    
        createAreas() {
            let newAreas = [];
            this.areas.forEach(area => {
                area.plan = '';
                area.residue ='';
                area.workerName = 'Выберите ФИО';
                area.workerInitials = [];
                area.addWorkers = [];
                // area.info = 'Измените поле';
                // area.error = false;

                newAreas.push(area);
            });

            if (this.production.length == 0)
                this.production.push(...newAreas);

            return newAreas;
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
                    <div class="mb-1 ps-1 text-secondary small">План, {{ area.unit }} :</div>
                    <input class="form-control ps-3" type="number" placeholder="Введите шт" v-model="area.plan">
                </div>
                <div class="col">
                    <div class="mb-1 ps-1 text-secondary small">Остаток, {{ area.unit }} :</div>
                    <input class="form-control ps-3" type="number" placeholder="Введите шт" v-model="area.residue"> 
                </div>
            </div>

            <div>
                <div class="mb-1 ps-1 text-secondary small">Состав бригады :</div>

                <select class="form-control form-select mb-3 ps-3" v-model="area.workerName" @focus="this.createWorkerNames()" @change="this.addWorker(area.workerName, area.workerInitials, area.addWorkers)">
                    <option v-for="option in this.nameOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                </select>

                <div class="small" v-for="(worker, number) in area.workerInitials.sort()" :key="worker">
                    <div class="d-flex justify-content-between align-items-center border border-secondary p-2 ps-3 rounded mt-2">
                        <div>#{{ number + 1 }} {{ worker }}</div>
                        <button class="btn btn-close btn-sm" @click="this.deleteWorker(worker, area.workerInitials, area.addWorkers)"></button>
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