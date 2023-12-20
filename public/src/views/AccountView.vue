<script>
import Header from '../components/Header.vue';
import MasterPage from '../components/MasterPage.vue';
import Footer from '../components/Footer.vue';

export default {
    name: 'AccountView',
    components: { 
        Header, 
        MasterPage, 
        Footer 
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
    <div class="wrapper">

        <Header :employee="employee" />

        <MasterPage 
            :addedTrainees="addedTrainees"
            :addWorkers="addWorkers"
            :employee="employee"
            :employees="employees"
            :production="production"
            :reportBtn="reportBtn"
            :shift="shift"
            :timesheet="timesheet"
            :trainees="trainees"
            v-if="this.employee[0].slug == 'master'" />

        <Footer />

    </div>
</template>

<style scoped>

</style>