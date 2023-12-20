<script>
import Header from '../components/Header.vue';
import HomePage from '../components/HomePage.vue';
import Footer from '../components/Footer.vue';

export default {
    name: 'HomeView',
    components: { 
        Header, 
        HomePage, 
        Footer 
    },
    props: [
        'employee',
        'employees',
    ],
}
</script>

<template>
    <div class="wrapper">

        <Header :employee="employee" />

        <!-- <HomePage /> -->

        <Footer />

    </div>
</template>

<style scoped>

</style>