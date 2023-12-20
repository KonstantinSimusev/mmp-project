<script>

export default {
    name: 'TraineeBlock',
    props: [
        'addedTrainees',
        'addedWorkers',
        'employee',
        'employees',
        'trainees',
    ],
    data() {
        return {
            workerName: 'Выберите ФИО',
            nameOptions: [],
        }
    },
    mounted() {
        this.createWorkerNames();
    },
    methods: {
        deleteWorker(worker, arrayOne, arrayTwo) {
            const index = arrayOne.findIndex(item =>
                item === worker);

            if (index !== -1) {
                arrayOne.splice(index, 1);
                arrayTwo.splice(index, 1);
            }
        },

        addWorker() {
            if (this.workerName != 'Выберите ФИО') {
                const initials = this.createInitials(this.workerName);
                const addedWorker = this.trainees.filter(name =>
                    name == initials);

                if (addedWorker.length == 0) {
                    this.trainees.push(initials);
                    this.addedTrainees.push(this.workerName);
                }
            }
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
    }
}
</script>

<template>
    <div class="wrapper px-3 p-3 mb-5 mt-3 rounded-4 shadow-sm">

        <div class="mb-1 ps-1 text-secondary small">Стажировка на рабочем месте :</div>

        <select class="form-control form-select ps-3 mb-3" v-model="workerName" @change="this.addWorker()" @focus="this.createWorkerNames()">
            <option v-for="option in this.nameOptions" :key="option.id" v-bind:value="option.value">{{ option.value }}</option>
        </select>

        <div class="worker__block small d-flex justify-content-between align-items-center mt-2 border border-secondary p-2 ps-3 rounded" v-for="(worker, number) in this.trainees.sort()" :key="worker">

            <div>#{{ number + 1 }} {{ worker }}</div>

            <button class="btn btn-close btn-sm" @click="this.deleteWorker(worker, this.trainees, this.addedTrainees)"></button> 

        </div>

    </div>
</template>

<style scoped>
.wrapper { background: #c1dcc6; }

select:focus { box-shadow: none }
</style>