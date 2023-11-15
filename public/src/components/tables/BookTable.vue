<script>
import axios from 'axios';

class Profession {
    constructor(id, title, count) {
        this.id = id;
        this.title = title;
        this.count = count;
    }
}

export default {
    name: 'BookTable',
    data() {
        return {
            employees: [],
            professions: [],
        }
    },
    async mounted() {
        try {
            const dataBaseEmployees = await axios
                .get('http://127.0.0.1:8000/api/employee/?format=json');

            const dataBaseProfessions = await axios
                .get('http://127.0.0.1:8000/api/profession/?format=json');
            
            this.employees = dataBaseEmployees.data;
            this.professions = dataBaseProfessions.data;
        }
        catch (error) {
            console.log(error);
        }
        
        this.professions = this.professions.map(profession =>
            new Profession(
                profession.id,
                profession.name,
                this.employees.filter(employee => 
                    employee.slug == profession.slug).length
            )
        );

    }, 
}
</script>

<template>
    <div class="wrapper mt-5 shadow p-4 rounded-4">
        <div class="text-center fw-bold mb-2 text-uppercase small">Книга личного состава</div>

        <table class="table table-bordered table-hover table-sm align-middle small">
            <thead class="table-success">
                <tr>
                    <th class="text-center">#</th>
                    <th class="text-center">Профессия</th>
                    <th class="text-center">Чел</th>
                </tr>
            </thead>
            <tbody class="table-light">
                <tr v-for="(profession, number) in this.professions.sort((a,b) => a.id - b.id)" :key="profession">
                    <th class="text-center">{{ number + 1 }}</th>    
                    <td class="ps-2">{{ profession.title }}</td>
                    <td class="text-center">{{ profession.count }}</td>
                </tr>
            </tbody>
            <tfoot class="table-secondary">
                <tr>
                    <th colspan="3" class="text-end pe-2">Итого: {{ employees.length }}</th>
                </tr>
            </tfoot>
        </table>

    </div>
</template>

<style scoped>
.bg__color {
    background: rgba(237, 237, 237, 0.8);
}
</style>