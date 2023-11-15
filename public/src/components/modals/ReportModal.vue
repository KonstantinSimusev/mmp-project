<script>
import axios from 'axios';

export default {
    name: 'ReportModal',
    props: [
        'production', 
        'reportBtn', 
        'shift'
    ],
    data() {
        return {
            areas: [],
            visible: true,
            disabled: 'disabled',
        }
    },
    mounted() {
        if (this.reportBtn.length > 0)
            this.visible = this.reportBtn[0];
    },
    methods: {
        saveReport() {
            const data = {
                date: this.shift[0].day,
                shift: this.shift[0].number,
                team: this.shift[0].team,
                report: JSON.stringify(this.production[0])
            }

            axios.put(`http://127.0.0.1:8000/api/report/1/`, data);

            if (this.reportBtn.length == 0) {
                this.visible = false;
                this.reportBtn.push(this.visible);
            }
        },
    }
}
</script>

<template>
    <div class="wrapper">

        <div class="mt-5 text-center">
            <button style="width: 245px;" v-if="visible" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#report">Создать рапорт</button>

            <button style="width: 245px;" v-if="!visible" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#report">Изменить рапорт</button>
        </div>

        <!-- The Modal -->
        <div class="modal fade" id="report" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">

                    <!-- Modal Header -->
                    <div class="modal-header bg-secondary">
                        <h4 class="modal-title text-light fw-bold">Производство</h4>
                    </div>

                    <!-- Modal body -->
                    <div class="modal-body">
                        <form class="p-2" @submit.prevent="saveReport()">
            
                            <div class="area rounded p-3 mb-5 shadow" v-for="area in this.production[0].sort((a, b) => a.id - b.id)" :key="area.id">
                                <div class="mb-1 small">{{ area.title }}, {{ area.unit }} :</div>

                                <div class="d-flex">
                                    <input class="form-control text-center me-2" type="number" placeholder="План" v-model="area.plan">

                                    <input class="form-control text-center ms-2" type="number" placeholder="Остаток" v-model="area.residue"> 
                                </div>
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
.area {
    background: rgba(220, 220, 220, 0.6);
}

input::placeholder {
    color: #333;
}

input:focus,
button:focus { box-shadow: none }
</style>