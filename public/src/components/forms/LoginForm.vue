<script>
import axios from 'axios';

export default {
    name: 'LoginForm',
    props: [
        'employee', 
        'employees',
    ],
    data() {
        return {
            // Database Properties
            baseEmployees: [],

            // Spinner Properties
            loaded: false,

            // Input Properties
            login: '',
            password: '',

            // Invalid properties
            loginError: '',
            passwordError: '',
            
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            this.baseEmployees = dataBaseEmployees.data;

        } catch(error) {
            console.log(error);
        }

        this.loaded = true;
    },
    methods: {
        signIn() {
            if (this.checkIn().length > 0) {
            
                this.employee.push(this.checkIn()[0]);
                this.employees.push(...this.baseEmployees);

                if (this.employee[0].slug != 'boss')
                    this.$router.push(`/${ this.employee[0].slug }/${ this.employee[0].id }/`);
                else 
                    this.$router.push('/home/');

            } else {
                this.loginError = 'is-invalid';
                this.passwordError = 'is-invalid';

                this.login = '',
                this.password = ''
            }
        },

        checkIn() {
            const manager = this.getManagers().filter(manager => 
                manager.login == this.login &&
                manager.password == this.password);
            return manager;
        },

        getManagers() {
            const managers = this.baseEmployees.filter(employee =>
                employee.slug == 'master' && 
                employee.schedule == '2-А' ||
                employee.slug == 'boss')
                    .sort((a, b) => a.slug < b.slug ? -1 : 1);
            
            return this.createManagers(managers);
        },

        createManagers(array) {
            let manager = {};
            const managers = array.map((employee, index) =>
                manager = {
                    id: employee.id,
                    slug: employee.slug,
                    fullname: employee.fullname,
                    team: employee.team,
                    login: index + 1,
                    password: index + 1
                }
            )
            return managers;
        },
    },
}
</script>

<template>
    <div class="container">

        <!-- Spinner -->
        <div v-if="!loaded" class="loading__spinner d-flex align-items-center text-secondary px-5">
            <strong role="status">Идет загрузка...</strong>
            <div class="spinner-border ms-auto" aria-hidden="true"></div>
        </div>
 
        <form v-if="loaded" class="login__block mx-auto" @submit.prevent="signIn()">

            <input type="text" v-bind:class="`form-control ${ loginError } ps-4 mb-3 shadow-sm`" placeholder="Введите логин" v-model="login">

            <input type="password" v-bind:class="`form-control ${ passwordError } ps-4 mb-5 shadow-sm`" placeholder="Введите пароль" v-model="password">
                    
            <button class="btn btn-danger">Войти в личный кабинет</button>

        </form> 
    </div>
</template>

<style scoped>
form, .loading__spinner { margin-top: 130px; }

form, .btn { width: 280px; }

input::placeholder { color: #333; }
</style>