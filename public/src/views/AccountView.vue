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
            slug: 'master'
        }
    }
}
</script>

<template>
    <div class="wrapper">

        <Header :employee="employee" />

        <MasterPage 
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
            :teamWorkers="teamWorkers"
            v-if="this.employee[0].slug == this.slug" />

        <Footer />

    </div>
</template>

<style scoped>

</style>