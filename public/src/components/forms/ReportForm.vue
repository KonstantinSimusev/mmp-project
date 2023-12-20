<script>
import axios from 'axios';
import AddWorkerBlock from '../blocks/AddWorkerBlock.vue';
import TraineeBlock from '../blocks/TraineeBlock.vue';
import AreaBlock from '../blocks/AreaBlock.vue'
import NotPresenceBlock from '../blocks/NotPresenceBlock.vue';


class Worker {
    constructor(
        id,
        slug,
        fullname, 
        profession, 
        schedule, 
        team,
        area,
        initials,
        presence,
        trainee,
    ) {
        this.id = id;
        this.slug = slug;
        this.fullname = fullname;
        this.profession = profession;
        this.schedule = schedule;
        this.team = team;
        this.area = area;
        this.initials = initials;
        this.presence = presence;
        this.trainee = trainee;
    }
}


export default {
    name: 'ReportForm',
    components: {
        AddWorkerBlock,
        TraineeBlock,
        AreaBlock,
        NotPresenceBlock,
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
    data() {
        return {
            visibleBtn: true,
        }
    },
    computed: {
        countAreaError() {
            const areaErrorCount = this.production.filter(area =>
                ((area.plan > 0 || area.residue > 0) && area.addWorkers.length == 0) ||
                (area.plan == 0 && area.residue == 0 && area.addWorkers.length > 0)).length;
            return areaErrorCount;
        },

        countSheetError() {
            const sheetErrorCount = this.timesheet.filter(worker =>
                worker.presence == 'Выберите причину' &&
                worker.visible == true).length;
            return sheetErrorCount;
        }
    },
    methods: {
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
    }
}
</script>

<template>
    <div class="wrapper">
        <form class="p-2 mb-5" @submit.prevent="this.saveReport()">

            <AddWorkerBlock
                :addWorkers="addWorkers"
                :employee="employee"
                :employees="employees" />

            <!-- <TraineeBlock
                :addedTrainees="addedTrainees" 
                :addedWorkers="addedWorkers"
                :employee="employee"
                :employees="employees"
                :trainees="trainees" /> -->

            <!-- <AreaBlock
                :addedWorkers="addedWorkers"
                :employee="employee"
                :employees="employees"
                :production="production"
                :timesheet="timesheet" /> -->

            <!-- <NotPresenceBlock
                :employee="employee"
                :employees="employees" 
                :production="production"
                :timesheet="timesheet" /> -->


            <button v-if="countAreaError == 0 && countSheetError == 0" class="btn btn-danger float-end" data-bs-dismiss="modal">Сохранить</button>
        
        </form>
    </div>
</template>

<style scoped>

</style>