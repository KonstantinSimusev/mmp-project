<script>
import axios from 'axios';

class Option {
    constructor(value) {
        this.value = value;
    }
}

export default {
    name: 'TimeSheetModal',
    props: [
        'sheetBtn', 
        'shift', 
        'timesheet'
    ],
    data() {
        return {
            workers: [],
            sheet: [],
            visible: true,
            professionOptions: [
                new Option('УКЛАДЧИК - УПАКОВЩИК'),
                new Option('ШТАБЕЛИРОВЩИК МЕТАЛЛА'),
                new Option('ШТАМПОВЩИК'),
            ],
            presenceOptions: [
                new Option('ЯВКА'),
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
            areaOptions: [
                new Option('ЛПЦ-5'),
                new Option('АПР-2'),
                new Option('АПР-3'),
                new Option('АПР-4'),
                new Option('АПР-5'),
                new Option('АПР-8'),
                new Option('АПР-9'),
                new Option('НТА'),
                new Option('НТА (к)'),
                new Option('ЛПЦ-4'),
                new Option('Туп 10/1'),
                new Option('Туп 10/2'),
                new Option('Туп 12 (тов)'),
                new Option('Туп 12 (ммк)'),
            ],
            probationOptions: [
                new Option('ПРОЙДЕНА'),
                new Option('СТАЖЕР'),
            ],
        }
    },
    mounted() {
        if (this.sheetBtn.length > 0)
            this.visible = this.sheetBtn[0];
    },
    methods: {
        saveTimeSheet() {
            const data = {
                team: this.shift[0].team,
                timesheet: JSON.stringify(this.timesheet[0])
            }

            axios.put(`http://127.0.0.1:8000/api/timesheet/${ this.shift[0].team }/`, data);

            if (this.sheetBtn.length == 0) {
                this.visible = false;
                this.sheetBtn.push(this.visible);
            }
        },
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="mt-3 text-center">
            <button style="width: 245px;" v-if="visible" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#timesheet">Создать табель</button>

            <button style="width: 245px;" v-if="!visible" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#timesheet">Изменить табель</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="timesheet" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <div class="modal-header bg-secondary">
                        <h4 class="modal-title text-light fw-bold">Табель</h4>
                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">
                        <form class="p-2"  @submit.prevent="saveTimeSheet()">
                            
                            <div class="timesheet rounded p-3 mb-5 shadow" v-for="(worker, number) in this.timesheet[0].sort((a, b) => (a.slug + a.fullname) > (b.slug + b.fullname) ? 1 : -1)" :key="worker.id">


                                <div class="mb-2 fw-bold small p-2"><b>#{{ number + 1 }} {{ worker.fullname }}</b></div>

                                <div class="mb-1 text-secondary small">Профессия :</div>
                                <select class="form-control form-select text-center mb-2" v-model="worker.profession">
                                    <option v-for="option in professionOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                </select>
             
                                <div class="mb-1 text-secondary small">Участок :</div>
                                <select class="form-control form-select text-center mb-2" v-model="worker.area">
                                    <option v-for="option in areaOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                </select>

                                <div class="mb-1 text-secondary small">Нахождение на рабочем месте :</div>
                                <select class="form-control form-select text-center mb-2" v-model="worker.presence">
                                    <option v-for="option in presenceOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                </select>

                                <div class="mb-1 text-secondary small">Стажировка на рабочем месте :</div>
                                <select class="form-control form-select text-center mb-2" v-model="worker.probation">
                                    <option v-for="option in probationOptions" :key="option" v-bind:value="option.value">{{ option.value }}</option>
                                </select>

                                <!-- <div><b>Отработано часов :</b></div>
                                <input class="form-control text-center mb-5" type="number" placeholder="Планируемое произвоство" v-model="worker.time"> -->
                        
                            
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
.timesheet {
    background: rgba(220, 220, 220, 0.6);
}

input:focus,
select:focus,
button:focus { box-shadow: none }
</style>