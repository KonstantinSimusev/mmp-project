<script>
import ReportForm from '../forms/ReportForm.vue';

export default {
    name: 'ReportModal',
    components: { ReportForm },
    props: [
        'addEmployee',
        'employee',
        'employees',
        'nameOptions',
        'notTeamWorkers',
        'production', 
        'reportBtn', 
        'shift',
        'timesheet',
        'trainees',
        'teamWorkers',
    ],
    computed: {
        countTraineeError() {
            let error = 0;
            let workers = [];

            workers.push(...this.getAreaWorkers());
            workers.push(...this.getSheetWorkers());
            
            this.trainees.flat().forEach(function(trainee) {
                const findWorkers = workers.filter(worker =>
                    worker == trainee);

                if (findWorkers.length == 0)
                    error++;
            });

            return error;
        },
    
        countSheetError() {
            const sheetErrorCount = this.timesheet.filter(worker =>
                worker.presence == 'Выберите причину' &&
                worker.visible == true).length;
            return sheetErrorCount;
        },

        countAreaError() {
            const areaErrorCount = this.production.filter(area =>
                ((area.plan > 0 || area.residue > 0) && area.addWorkers.length == 0) ||
                (area.plan == 0 && area.residue == 0 && area.addWorkers.length > 0)).length;
            return areaErrorCount;
        },
    },
    methods: {
        createWorkerNames() {
            let option = {};
            let options = [];

            const names = this.teamWorkers.map(worker => 
                worker.fullname);

            const addNames = this.addEmployee.map(worker => 
                    worker.fullname);

            names.push(...addNames);
            names.sort();

            options.push('Выберите работника');
            options.push(...names);

            options = options.map(name => 
                option = { value: name });
            
            this.nameOptions.length = 0;
            this.nameOptions.push(...options);
        },

        getAreaWorkers() {
            const workers = this.production.map(area =>
                area.addWorkers.map(worker =>
                    worker)).flat();

            return workers;
        },

        getSheetWorkers() {
            const workers = this.timesheet
                .filter(worker =>
                    worker.presence != 'Выберите причину')
                        .map(worker =>
                            worker.initials);
            
            return workers;
        },

    }
}
</script>

<template>
    <div class="wrapper">

        <!-- Button -->
        <div class="mt-5 text-center">
            <button style="width: 245px;" v-if="reportBtn.length == 0" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#report" @click="this.createWorkerNames()">Создать рапорт</button>

            <button style="width: 245px;" v-if="reportBtn.length > 0" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#report" @click="this.createWorkerNames()">Изменить рапорт</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="report" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <div v-if="(countTraineeError == 0 && countAreaError == 0 && countSheetError == this.timesheet.length) || (countTraineeError == 0 && countAreaError == 0 && countSheetError == 0)" class="modal-header bg-secondary shadow-sm">
                        <h5 class="modal-title text-light fw-bold">Рапорт</h5>
                    </div>

                    <!-- Modal Header -->
                    <div v-if="countTraineeError > 0 || countAreaError > 0 || (countSheetError > 0 && countSheetError != this.timesheet.length)">

                        <div class="error__title modal-header">
                            <h5 class="modal-title fw-bold">Внимание!</h5>  
                        </div>
                        <div class="border border-danger text-danger fw-bold small p-3 rounded-4 m-4">
                            <div class="row" v-if="countTraineeError > 0">
                                <div class="col-10">Ошибка в стажировке :</div>
                                <div class="col text-end">{{ countTraineeError }}</div>
                            </div>
                            <div class="row" v-if="countSheetError != this.timesheet.length && countSheetError > 0">
                                <div class="col-10">Ошибка в табеле :</div>
                                <div class="col text-end">{{ countSheetError }}</div>
                            </div>
                            <div class="row" v-if="countAreaError > 0">
                                <div class="col-10">Ошибка в участке :</div>
                                <div class="col text-end">{{ countAreaError }}</div>
                            </div>
                        </div> 

                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">

                        <ReportForm 
                            :addEmployee="addEmployee"
                            :employee="employee"
                            :employees="employees"
                            :nameOptions="nameOptions"
                            :notTeamWorkers="notTeamWorkers"
                            :production="production"
                            :reportBtn="reportBtn"    
                            :shift="shift"
                            :timesheet="timesheet"
                            :trainees="trainees"
                            :teamWorkers="teamWorkers" />

                    </div>

                </div>
            </div>
        </div>
        
    </div>
</template>

<style scoped>
.error__title { 
    background: #ffc7c7; 
    color: #a25959;
}
</style>