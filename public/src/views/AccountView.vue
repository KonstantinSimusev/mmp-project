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
        'employee', 
        'employees', 
        'notTeamWorkers', 
        'production', 
        'reportBtn', 
        'sheetBtn', 
        'shift', 
        'timesheet',
    ],
}
</script>

<template>
    <div class="wrapper">

        <Header :employee="employee" />

        <MasterPage :employee="employee"
                    :employees="employees"
                    :notTeamWorkers="notTeamWorkers"
                    :production="production"
                    :reportBtn="reportBtn"
                    :sheetBtn="sheetBtn"
                    :shift="shift"
                    :timesheet="timesheet"
                    v-if="this.employee[0].slug == 'master'" />

        <Footer />

    </div>
</template>

<style scoped>

</style>