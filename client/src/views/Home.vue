<template>
<div class="container text-center setup">
    <h1 class="mt-5 intro">
        Welcome to ExamineAI
    </h1>
    <div>
        <p class="fs-4">
            The power of artificial intelligence meets your well-being. 
            By analyzing your symptoms against a vast database of medical knowledge, ExamineAI generates 
            personalized recommendations and suggestions. Using ExamineAI is simple and user-friendly. 
            All you need to do is provide accurate information about your symptoms and answer a series 
            of questions. Our intelligent system will then process the data and generate a comprehensive 
            report, highlighting potential ailments that may be associated with your symptoms. Join us on 
            this transformative journey toward better health. Explore ExamineAI today and take the first 
            step in unlocking a deeper understanding of your physical well-being. Click the button below 
            to begin your examination.
        </p>
        <button class="btn btn-primary btn-lg">
            <RouterLink to="/signin" class="text-white text-decoration-none">Join Us Today</RouterLink>
        </button>
    </div>
</div>
</template>

<script>
import { RouterLink } from 'vue-router';
</script>

<style>
.setup {
    margin-top: 175px;
    animation: fadeInAnimation ease 2s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
}

@keyframes fadeInAnimation {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
     }
}

h1 {
    font-size: 48px;
}

.intro {
    margin-bottom: 50px;
}

button.btn.btn-primary.btn-lg {
    margin-top: 200px;
    height: 100px;
    width: 200px;
}

</style>