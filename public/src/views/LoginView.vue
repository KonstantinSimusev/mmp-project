<script>
import Header from '../components/Header.vue';
import LoginForm from '../components/forms/LoginForm.vue';

export default {
    name: 'LoginView',
    components: { 
        Header, 
        LoginForm, 
    },
    props: [
        'employee', 
        'employees',
    ],
}
</script>

<template>
    <div class="wrapper">

        <Header :employee="employee" 
                v-if="employee.length > 0" />

        <LoginForm  :employee="employee" 
                    :employees="employees"  />           
    </div>
</template>

<style scoped>

</style>