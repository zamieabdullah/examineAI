<template>
    <header class="navbar navbar-expand-lg bg-light">
        <h1>ExamineAI</h1>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <RouterLink to='/' class="nav-link">Home</RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to='/about' class="nav-link">About</RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to='/resources' class="nav-link">Resources</RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to='/signin' class="nav-link">Sign In</RouterLink>
                </li>
            </ul>
        </div>
    </header>
</template>

<script>
import { RouterLink } from 'vue-router';
</script>

<style>
header {
    padding: 100px;
}

header h1 {
    font-size: 48px;
    margin-left: 1%;
}

header ul {
    list-style: none;
    display: flex;
    justify-content: space-between;
    margin-right: 1%;
}

button.navbar-toggler {
    margin-right: 10px;
}

div#navbarNav.navbar-collapse {
    margin-left: 10px;
}

.navbar-collapse.collapse .nav-link {
    transition: transform 0.1s ease;
}

.navbar-collapse.collapse .nav-link:hover{
    color: rgb(98, 164, 226);
    transform: translate(1%, 0%);
}

@media (min-width: 992px) {
    .navbar-collapse.collapse .nav-link:hover {
        background-color: rgba(50, 240, 224, 0.377);
        color: rgb(98, 164, 226);
        transform: scale(1.1);
    }
}
</style>