<script>
import axios from 'axios';
import Trainee from '../Trainee.vue';
import Area from '../Area.vue';
import TimeSheet from '../TimeSheet.vue';


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


class AreaWorker {
    constructor(
        area,
        initials,
        presence,
        trainee,
    ) {
        this.area = area;
        this.initials = initials;
        this.presence = presence;
        this.trainee = trainee;
    }
}


export default {
    name: 'ReportForm',
    components: {
        Trainee,
        Area,
        TimeSheet,
    },
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
            console.log(this.getSheetWorkers());

            this.createDataBaseWorkers();

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

        createSheetWorkers() {
            let worker = {};
            let workers = [];

            this.getSheetWorkers.map()
        },

        getSheetWorkers() {
            const workers = this.timesheet.filter(worker =>
                worker.presence != 'Выберите причину');
            return workers
        },

        createDataBaseWorkers() {
            let trainee = {};
            let workers = [];
            const addTrainees = this.trainees.join();

            this.createAreaWorkers().forEach(function(worker) {
                if (addTrainees.includes(worker.initials)) {
                    trainee = new AreaWorker(
                        worker.area,
                        worker.initials,
                        'ЯВКА',
                        'СТАЖЕР',
                    );
                    workers.push(trainee);
                } else 
                    workers.push(worker);
            });

            const dataBaseWorkers = this.makeDataBaseWorkers(workers);
            return dataBaseWorkers;
        },

        makeDataBaseWorkers(array) {
            let workers = [];
            if (array.length > 0)
                workers = array.map(worker =>
                    new Worker(
                        this.getProperty(worker.initials).id,
                        this.getProperty(worker.initials).slug,
                        this.getProperty(worker.initials).fullname, 
                        this.getProperty(worker.initials).profession, 
                        this.getProperty(worker.initials).schedule, 
                        this.getProperty(worker.initials).team,
                        worker.area,
                        worker.initials,
                        worker.presence,
                        worker.trainee,
                    )                
                );

            return workers;
        },

        getProperty(initials) {
            const employee = this.getWorkers().filter(worker =>
                worker.initials == initials)[0];
            return employee;
        },

        createAreaWorkers() {
            let workers = [];
            workers = this.production.map(area =>
                area.addWorkers.map(worker =>
                    new AreaWorker(
                        area.title,
                        worker,
                        'ЯВКА',
                        'ПРОЙДЕНА',
                    )
                )
            ).flat();

            return workers;
        },

        //     if (this.trainees.length > 0)
        //         workers = this.trainees.map(trainee =>
        //             this.getWorkers().filter(worker =>
        //                 worker.initials == trainee)).flat();

        getWorkers() {
            let workers = [];
            workers.push(...this.notTeamWorkers);
            workers.push(...this.teamWorkers);
            return workers;
        },
    }
}
</script>

<template>
    <div class="wrapper">
        <form class="p-2 mb-5" @submit.prevent="this.saveReport()">

            <Trainee 
                :nameOptions="nameOptions"
                :notTeamWorkers="notTeamWorkers" 
                :teamWorkers="teamWorkers"
                :trainees="trainees" />

            <Area
                :nameOptions="nameOptions"
                :notTeamWorkers="notTeamWorkers" 
                :production="production"
                :teamWorkers="teamWorkers" />

            <TimeSheet 
                :timesheet="timesheet"
                :teamWorkers="teamWorkers" />


            <button v-if="countAreaError == 0 && countSheetError == 0" class="btn btn-danger float-end" data-bs-dismiss="modal">Сохранить</button>
        
        </form>
    </div>
</template>

<style scoped>

</style>