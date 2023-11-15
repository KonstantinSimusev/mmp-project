<script>

class Option {
    constructor(value) {
        this.value = value;
    }
}

export default {
    name: 'AddModal',
    props: [
        'notTeamWorkers',
        'shift',
        'timesheet',
    ],
    data() {
        return {
            workerName: 'Выберите работника',
            nameOptions: [],
            visible: true,
        }
    },
    mounted() {
        const names = this.notTeamWorkers.map(worker => worker.fullname).sort();

        this.nameOptions.push('Выберите работника');
        this.nameOptions.push(...names);

        this.nameOptions = this.nameOptions
        .filter((worker, index, workers) => workers.indexOf(worker) === index);

        this.nameOptions = this.nameOptions.map(name => new Option(name));
    },
    methods: {
        addWorker() {
            const addEmployee = this.notTeamWorkers.filter(employee => 
                employee.fullname == this.workerName);
            
            this.timesheet[0].push(...addEmployee);
            
            this.timesheet[0] = this.timesheet[0].map(str => JSON.stringify(str))
            .filter((worker, index, workers) => workers.indexOf(worker) === index);
            
            this.timesheet[0] = this.timesheet[0].map(worker => JSON.parse(worker));

            this.workerName = 'Выберите работника';
        },
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="mt-5 text-center">
            <button style="width: 245px;" v-if="visible" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#add">Добавить работника</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="add" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <div class="modal-header bg-secondary">
                        <h4 class="modal-title text-light fw-bold">Архив</h4>
                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">
                        <form @submit.prevent="addWorker()">
                            
                            <select class="form-control form-select text-center my-5 shadow" v-model="workerName">
                                <option v-for="option in nameOptions" :key="option.id" v-bind:value="option.value">{{ option.value }}</option>
                            </select>

                            <!-- Modal footer -->
                            <div class="text-end">
                                <button class="btn btn-danger" data-bs-dismiss="modal">Добавить</button>
                            </div>
                            
                        </form>
                    </div>

                </div>
            </div>
        </div>
        
    </div>
</template>

<style scoped>
input:focus,
select:focus,
button:focus { box-shadow: none }
</style>