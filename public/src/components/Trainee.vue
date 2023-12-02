<script>

export default {
    name: 'Trainee',
    props: [
        'nameOptions',
        'notTeamWorkers',
        'teamWorkers',
        'trainees',
    ],
    data() {
        return {
            workerName: 'Выберите работника',
        }
    },
    methods: {
        deleteWorker(worker, array) {
            const index = array.findIndex(name =>
                name == worker);

            if (index !== -1)
                array.splice(index, 1);
        },

        addTrainee(worker, trainees) {
            if (worker !== 'Выберите работника') {

                const fullname = this.getWorker(worker).initials;

                const repeatNames = trainees.filter(name =>
                    name == fullname);

                if (repeatNames.length == 0) 
                    trainees.push(fullname);
                
                trainees.sort();
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
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="block__color rounded-4 px-3 p-3 mb-5 mt-3 shadow-sm">

            <div class="mb-1 text-secondary small">Стажировка на рабочем месте :</div>

            <select class="form-control form-select ps-3 mb-3" v-model="workerName" @change="this.addTrainee(this.workerName, this.trainees)">
                <option v-for="option in this.nameOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
            </select>

            <div class="small" v-for="(worker, number) in this.trainees" :key="worker">
                <div class="d-flex justify-content-between align-items-center mt-2 border border-secondary p-2 ps-3 rounded">
                    <div>#{{ number + 1 }} {{ worker }}</div>
                    <button class="btn btn-close btn-sm" @click="this.deleteWorker(worker, this.trainees)"></button>
                </div>                                          
            </div>

        </div>

    </div>
</template>

<style scoped>
.block__color { background: #c1dcc6; }

input:focus,
button:focus,
select:focus { box-shadow: none }
</style>