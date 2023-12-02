<script>
import axios from 'axios';

class Option {
    constructor(value) {
        this.value = value;
    }
}

export default {
    name: 'ReportModal',

    props: [
        'addEmployee',
        'employee',
        'employees',
        'production', 
        'reportBtn', 
        'shift',
        'timesheet',
        'trainees',
    ],

    data() {
        return {
            // Database Properties
            areas: [], 

            // Installed Properties
            workerName: 'Выберите работника',
            nameOptions: [],
            // addWorkers: [],

            // Button Properties
            visibleBtn: true,

            // Timesheet Properties
            workers: [],
            info: 'Заполните поле',
            sheetError: false,
            areaErrorCount: 0,
            sheetErrorCount: 0,
            presenceOptions: [
                new Option('Выберите причину'),
                new Option('Б'),
                new Option('ОТ'),
                new Option('НБ'),
                new Option('Д'),
                new Option('ПТД'),
                new Option('ОС'),
                new Option('У'),
                new Option('КУ'),
                new Option('НД'),
                new Option('РВ'),
                new Option('ОИ'),
                new Option('НН'),
                new Option('ПР'),
                new Option('ДНД'),
                new Option('К'),
                new Option('В'),
                new Option('УВОЛЕН'),
                new Option('БР 1'),
                new Option('БР 2'),
                new Option('БР 3'),
                new Option('БР 4'),
                new Option('БР 5'),
                new Option('ЛПЦ-4'),
                new Option('ЛПЦ-7'),
                new Option('ЛПЦ-8'),
                new Option('ЛПЦ-10'),
                new Option('ЛПЦ-11'),
                new Option('ПМП (сб)'),
                new Option('ПМП (юб)'),
                new Option('УВС'),
            ],
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

        this.createTeamWorkers();
        this.createAreas();
        this.createTimesheet();
    },

    methods: {
        createTimesheet() {
            if (this.timesheet.length == 0)
                this.timesheet.push(...this.workers);
        },

        chooseReason(id) {
            const employee = this.workers.filter(employee => 
                employee.id == id)[0];
            
            if (employee.presence !== 'Выберите причину')
                employee.error = false;
            else
                employee.error = true;
        },

        deleteWorker(worker, array) {
            const index = array.findIndex(name =>
                name == worker);

            if (index !== -1)
                array.splice(index, 1);
        },

        addAreaName(worker, addWorkers) {
            if (worker !== 'Выберите работника') {

                const fullname = this.createInitials(worker);

                const repeatAreaNames = addWorkers.filter(name =>
                    name == fullname);

                const areaWorkers = this.production.map(area =>
                    area.addWorkers).flat();

                const repeatAreasNames = areaWorkers.filter(name =>
                    name == fullname);

                if (repeatAreaNames.length == 0 && repeatAreasNames == 0)
                    addWorkers.push(fullname);
                    
                addWorkers.sort();
            }
        },

        addTrainee(worker, trainees) {
            if (worker !== 'Выберите работника') {

                const fullname = this.createInitials(worker);

                const repeatNames = trainees.filter(name =>
                    name == fullname);

                if (repeatNames.length == 0) 
                    trainees.push(fullname);
                
                trainees.sort();
            }
        },

        saveReport() {
            const data = {
                date: this.shift[0].day,
                shift: this.shift[0].number,
                team: this.shift[0].team,
                report: JSON.stringify(this.production[0])
            }

            // axios.put(`http://127.0.0.1:8000/api/report/1/`, data);

            if (this.reportBtn.length == 0)
                this.reportBtn.push(this.visibleBtn);
        },

        createInitials(worker) {
            const string = worker;
            const surname = string.split(' ')[0];
            const initials = string.split(' ')[1][0] + string.split(' ')[2][0];
            const fullname = surname + ' ' + initials;
            
            return fullname;
        },

        createWorkerNames() {
            let options = [];

            const names = this.workers.map(worker => 
                worker.fullname);

            const addNames = this.addEmployee.map(worker => 
                    worker.fullname);

            names.push(...addNames);
            names.sort();

            options.push('Выберите работника');
            options.push(...names);

            this.nameOptions = options.map(name => 
                new Option(name))
        },

        createTeamWorkers() {
            let newWorker = {};
            const workers = this.getTeamWorkers().map(worker =>
                newWorker = {
                    id: worker.id,
                    slug: worker.slug,
                    fullname: worker.fullname, 
                    profession: worker.profession, 
                    schedule: worker.schedule, 
                    team: worker.team,
                    area: 'ЛПЦ-5',
                    presence: 'Выберите причину',
                    probation: 'ПРОЙДЕНА',
                    info: 'Измените поле',
                    error: true,
                }
            )
            this.workers = workers;
        },

        getTeamWorkers() {
            const workers = this.employees.filter(employee =>
                employee.team == this.employee[0].team &&
                employee.slug != 'master' &&
                employee.schedule == '2-А');
            return workers;
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

        <div class="mt-5 text-center">
            <button style="width: 245px;" v-if="reportBtn.length == 0" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#report" @click="this.createWorkerNames()">Создать рапорт</button>

            <button style="width: 245px;" v-if="reportBtn.length > 0" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#report" @click="this.createWorkerNames()">Изменить рапорт</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="report" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <div class="modal-header bg-secondary">
                        <h4 class="modal-title text-light fw-bold">Рапорт</h4>
                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">

                        <form class="p-2" @submit.prevent="this.saveReport()">


                            <div class="probation rounded-4 p-3 mb-5 shadow-sm">
                                <div class="mb-1 text-secondary small">Стажировка на рабочем месте :</div>

                                    <select class="form-control form-select mb-4 ps-3" v-model="workerName" @change="this.addTrainee(this.workerName, this.trainees)">
                                        <option v-for="option in this.nameOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                    </select>

                                    <div class="small" v-for="(worker, number) in this.trainees" :key="worker">

                                    <div class="d-flex justify-content-between align-items-center mb-2 border border-secondary p-2 ps-3 rounded">
                                        <div>#{{ number + 1 }} {{ worker }}</div>
                                        <button class="btn btn-danger btn-sm" @click="deleteWorker(worker, this.trainees)">Удалить</button>
                                    </div>                  
                                        
                                </div>
                            </div>



            
                            <div class="area rounded-4 p-3 mb-5 shadow-sm" v-for="area in this.production.sort((a, b) => a.id - b.id)" :key="area.id">
                                <div class="small d-inline-flex px-3 py-2 mb-4 rounded-4 text-light fw-bold bg-secondary">{{ area.title }}</div>

                                <div class="mb-1 text-secondary small">Производство, {{ area.unit }} :</div>

                                <div class="d-flex mb-3">
                                    <input class="form-control ps-3 me-2" type="number" placeholder="План" v-model="area.plan">

                                    <input class="form-control ps-3 ms-2" type="number" placeholder="Остаток" v-model="area.residue"> 
                                </div>

                                <div>
                                    <div class="mb-1 text-secondary small">Состав бригады, ФИО :</div>

                                    <select class="form-control form-select mb-4 ps-3" v-model="area.workerName" @change="addAreaName(area.workerName, area.addWorkers)">
                                        <option v-for="option in this.nameOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                    </select>

                                    <div class="small" v-for="(worker, number) in area.addWorkers" :key="worker">

                                        <div class="d-flex justify-content-between align-items-center mb-2 border border-secondary p-2 ps-3 rounded">
                                            <div>#{{ number + 1 }} {{ worker }}</div>
                                            <button class="btn btn-danger btn-sm" @click="deleteWorker(worker, area.addWorkers)">Удалить</button>
                                        </div>                  
                                        
                                    </div>
                                </div>
                            
                            </div> 



                            <div class="timesheet rounded-4 p-3 mb-5 shadow-sm" v-for="(worker, number) in this.timesheet.sort((a, b) => (a.slug + a.fullname) > (b.slug + b.fullname) ? 1 : -1)" :key="worker.id">

                                <div class="d-flex justify-content-between mb-3">
                                    <div class="px-3 rounded-4 text-light fw-bold bg-secondary">{{ number + 1 }}</div>
                                    <div v-if="worker.error" class="small fw-bold text-danger pe-2">{{ worker.info }}</div>
                                </div>

                                <div class="mb-2 fw-bold small fw-bold">{{ worker.fullname }}</div>


                                <div class="mb-1 text-secondary small">Профессия :</div>
                                <div class="small mb-2">{{ worker.profession }}</div>

                                <div class="mb-1 text-secondary small">Причина отсутствия :</div>
                                <select class="form-control form-select mb-2 ps-3" v-model="worker.presence" @change="chooseReason(worker.id)">
                                    <option v-for="option in presenceOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                </select>

                            </div>                            

                            <!-- Modal footer -->
                            <div class="text-end">
                                <button class="btn btn-danger" data-bs-dismiss="modal">Сохранить</button>
                            </div>

                        </form>
                    </div>

                </div>
            </div>
        </div>
        
    </div>
</template>

<style scoped>
.probation { background: #c1dcc6; }

.timesheet { background: #cdc9a6; }

.area { background: #d1d6da; }

input::placeholder { color: #333333; }

input:focus,
button:focus,
select:focus { box-shadow: none }
</style>