<script>

export default {
    name: 'Header',
    props: [
        'employee',
    ],
}
</script>

<template>
    <div class="wrapper">
        <div class="navbar navbar-expand-md bg-dark navbar-dark fixed-top">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand" href="#">MagMetalPack</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="collapsibleNavbar">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <router-link to="/home/" class="nav-link" v-if="employee[0].team != '5'">Главная</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link v-bind:to="`/${employee[0].slug}/${employee[0].id}/`" class="nav-link" v-if="employee[0].team != '5'">Личный кабинет</router-link>
                        </li>
                        <li class="nav-item">
                            <a href="/" class="nav-link">Выйти</a>
                        </li> 
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.alert {margin-top: 75px;}
</style>