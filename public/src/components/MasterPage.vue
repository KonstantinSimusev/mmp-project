<script>
import DateForm from './forms/DateForm.vue';
import ReportForm from './forms/ReportForm.vue';

export default {
    name: 'MasterPage',
    components: { 
        DateForm,
        ReportForm,
    },
    props: [
        'addedTrainees',
        'addWorkers',
        'employee', 
        'employees',
        'production', 
        'reportBtn', 
        'shift',  
        'timesheet',
        'trainees',
    ],
}
</script>

<template>
    <div class="container">

        <div class="text-secondary fw-bold small mt-3">Мастер участка</div>
        <div>{{ employee[0].fullname }}</div>

        <div v-if="this.shift.length > 0">
            <div class="text-secondary fw-bold small mt-3">Информация о смене</div>
            <div v-if="this.shift.length > 0">{{ this.shift[0].day }}, смена {{ this.shift[0].number }}, бригада {{ this.shift[0].team }}</div>
        </div>

        <DateForm   
            :shift="shift"
            :employee="employee"
            v-if="this.shift.length == 0" />


        <!-- Button -->
        <div v-if="this.shift.length > 0" class="mt-5 text-center">
            <button style="width: 245px;" v-if="reportBtn.length == 0" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#report">Создать рапорт</button>

            <button style="width: 245px;" v-if="reportBtn.length > 0" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#report">Изменить рапорт</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="report" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <!-- <div v-if="(countTraineeError == 0 && countAreaError == 0 && countSheetError == this.timesheet.length) || (countTraineeError == 0 && countAreaError == 0 && countSheetError == 0)" class="modal-header bg-secondary shadow-sm">
                        <h5 class="modal-title text-light fw-bold">Рапорт</h5>
                    </div> -->

                    <!-- Modal Header -->
                    <!-- <div v-if="countTraineeError > 0 || countAreaError > 0 || (countSheetError > 0 && countSheetError != this.timesheet.length)">

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

                    </div> -->

                    <!-- Modal body -->
                    <div class="modal-body">

                        <ReportForm 
                            :addedTrainees="addedTrainees"
                            :addWorkers="addWorkers"
                            :employee="employee"
                            :employees="employees"
                            :production="production"
                            :reportBtn="reportBtn"    
                            :shift="shift"
                            :timesheet="timesheet"
                            :trainees="trainees" />

                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<style scoped>
.container { margin-top: 80px; }
</style>