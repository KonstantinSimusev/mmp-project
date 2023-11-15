<script>
import axios from 'axios';

class Employee {
    constructor(
        id,
        slug,
        fullname, 
        profession, 
        schedule, 
        team,
        area,
        presence,
        probation,
        login,
        password
        ) {
        this.id = id;
        this.slug = slug;
        this.fullname = fullname;
        this.profession = profession;
        this.schedule = schedule;
        this.team = team;
        this.area = area;
        this.presence = presence;
        this.probation = probation;
        this.login = login;
        this.password = password;
    }
}

export default {
    name: 'LoginForm',
    props: [
        'employee', 
        'employees'
    ],
    data() {
        return {
            baseEmployees: [],
            newEmployees: [],
            login: '',
            password: '',
            loginError: '',
            passwordError: '',
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            this.baseEmployees = dataBaseEmployees.data;
        }
        catch (error) {
            console.log(error);
        }

        this.baseEmployees.sort((a, b) => a.fullname > b.fullname ? 1 : -1);

        this.newEmployees = this.baseEmployees.map((employee, index) =>
            new Employee(
                employee.id,
                employee.slug,
                employee.fullname, 
                employee.profession, 
                employee.schedule, 
                employee.team,
                'ЛПЦ-5',
                'ЯВКА',
                'ПРОЙДЕНА',
                index,
                index
            )
        );
        // console.log(this.newEmployees);
    },
    methods: {
        signIn() {
            const person = this.newEmployees.filter(employee => 
                this.login == employee.login &&
                this.password == employee.password);

            if (person.length > 0) {
                this.employee.push(person[0]);
                this.employees.push(...this.newEmployees);

                if (person[0].slug != 'boss')
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
    },
}
</script>

<template>
    <div class="container">
        <form class="login__block mx-auto" @submit.prevent="signIn()">

            <input type="text" v-bind:class="`form-control ${ loginError } ps-4 mb-3 shadow`" placeholder="Введите логин" v-model="login">

            <input type="password" v-bind:class="`form-control ${ passwordError } ps-4 mb-5 shadow`" placeholder="Введите пароль" v-model="password">
                    
            <button class="btn btn-danger">Войти в личный кабинет</button>

        </form> 
    </div>
</template>

<style scoped>
form { margin-top: 130px; }

form, .btn { width: 280px; }

input::placeholder { color: #333; }
</style>