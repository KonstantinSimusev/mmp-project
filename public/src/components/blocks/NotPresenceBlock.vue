<script>
import axios from 'axios';


class Option {
    constructor(value) {
        this.value = value;
    }
}


export default {
    name: 'NotPresenceBlock',
    props: [
        'employee',
        'employees',
        'production',
        'timesheet',
    ],
    data() {
        return {
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
    mounted() {
        this.createTimesheet();
    },
    methods: {
        createTimesheet() {
            let workers = [];

            if (this.timesheet.length == 0) {
                this.getTeamWorkers().forEach(worker => {
                    worker.presence = 'Выберите причину';
                    worker.error = true;
                    worker.visible = true;
                    worker.info = 'Измените поле'
                    workers.push(worker);
                });

                this.timesheet.push(...workers);
            }
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
    <div class="wrapper">

        <div v-for="(worker, number) in this.timesheet" :key="worker.id">

            <div v-if="worker.visible" class="block__color rounded-4 p-3 mb-5 shadow-sm">

                <div class="d-flex justify-content-between mb-4">
                    <div class="px-3 rounded-4 text-light fw-bold bg-secondary">{{ number + 1 }}</div>
                    <div v-if="worker.error" class="small fw-bold text-danger pe-2">{{ worker.info }}</div>
                </div>

                <div class="mb-2 fw-bold small fw-bold">{{ worker.fullname }}</div>

                <div class="mb-1 text-secondary small">Профессия :</div>
                <div class="small mb-2">{{ worker.profession }}</div>

                <div class="mb-1 text-secondary small">Причина отсутствия :</div>

                <select class="form-control form-select mb-2 ps-3" v-model="worker.presence">
                    <option v-for="option in this.presenceOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                </select>                

            </div>

        </div>

    </div>
</template>

<style scoped>
.block__color { background: #d2cea8; }

input:focus,
button:focus,
select:focus { box-shadow: none }
</style>