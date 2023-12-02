<script>

export default {
    name: 'DateForm',
    props: [
        'employee', 
        'shift'
    ],
    data() {
        return {
            // Input Properties
            shiftDate: '',

            // Select Properties
            shiftNumber: 'Выберите смену',
            shiftOptions: [
                { value: 'Выберите смену' },
                { value: '1' },
                { value: '2' },
            ],

            // Invalid properties
            emptyDate: '',
            emptyShift: '',
        }
    },
    methods: {
        createDate() {
            if (this.shiftDate.length > 0 && this.shiftNumber != 'Выберите смену') {
                
                const shiftInfo = {
                    day: this.shiftDate.split('-').reverse().join('-'),
                    number: this.shiftNumber,
                    team: this.employee[0].team
                }

                this.shift.push(shiftInfo);
            } else {
                this.emptyDate = 'is-invalid';
                this.emptyShift = 'is-invalid';
            }
        },
    }
}
</script>

<template>
    <div class="container">    
        <form class="mx-auto" @submit.prevent="createDate()">

            <input type="date" v-bind:class="`form-control mb-3 ${ emptyDate } ps-4 shadow-sm`" v-model="shiftDate">

            <select v-bind:class="`form-control form-select mb-5 ${ emptyShift } ps-4 shadow-sm`" v-model="shiftNumber">
                <option v-for="option in shiftOptions" v-bind:value="option.value" :key="option">{{ option.value }}</option>
            </select>
            
            <button class="btn btn-danger">Создать смену</button>

        </form>
    </div>
</template>

<style scoped>
form, .btn { width: 280px; }
</style>