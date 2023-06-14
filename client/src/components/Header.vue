<template>
    <header class="navbar navbar-expand-lg">
        <h1>ExamineAI</h1>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Resources</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Sign In</a>
                </li>
            </ul>
        </div>
    </header>
</template>

<script>
import { RouterLink } from 'vue-router';
</script>

<style>

header h1 {
    font-size: 48px;
    margin-right: 24px;
}

header ul {
    list-style: none;
    display: flex;
    justify-content: space-between;
    padding: 0%;
}

li {
    transition: transform 0.1s ease;
}

li:hover{
    background-color: rgba(50, 240, 224, 0.377);
    color: rgb(98, 164, 226);
    transform: scale(1.1);
}
</style>