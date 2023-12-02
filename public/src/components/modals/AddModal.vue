<script>

export default {
    name: 'AddModal',
    props: [
        'addEmployee',
        'employee',
        'employees',
        'notTeamWorkers',
    ],
    data() {
        return {
            names: [],
            workerName: 'Выберите работника',
            nameOptions: this.createWorkerNames(),
        }
    },
    methods: {

        addWorker() {
            if (this.workerName != 'Выберите работника') {
                if (this.names.length > 0) {
                    const newName = this.names.filter(name => 
                        name == this.workerName);

                    if (newName.length == 0) 
                        this.appendWorker(); 
                } else
                    this.appendWorker();
            }
            this.workerName = 'Выберите работника';
        },

        appendWorker() {
            const worker = this.notTeamWorkers.filter(worker =>
                worker.fullname == this.workerName);

            this.names.push(this.workerName);
            this.addEmployee.push(...worker);
    
        },

        createWorkerNames() {
            let optionName = {};
            let options = [];
            const names = this.notTeamWorkers.map(worker => 
                worker.fullname).sort();

            options.push('Выберите работника');
            options.push(...names);

            const nameOptions = options.map(name => 
                optionName = { value: name });

            return nameOptions;
        },
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="mt-5 text-center">
            <button style="width: 245px;" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#add">Добавить работника</button>
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
                            
                            <select class="form-control form-select text-center my-5 shadow-sm" v-model="workerName">
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