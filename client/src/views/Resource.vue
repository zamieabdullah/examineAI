<template>
    <div class="container mt-5 setup">
        <h1 class="text-decoration-underline text-center intro">Resources</h1>
        <div class="box">
            <img src="../assets/ChatGPT.png" class="d-inline-block" style="width: 10%;">
            <div class="ms-3 d-inline-block">
                <h2>ChatGPT</h2>
                <p class="fs-5">
                    ChatGPT, the powerful language model developed by OpenAI, plays a significant 
                    role in the functionality of ExamineAI. As an advanced AI technology, ChatGPT 
                    enables seamless and intelligent conversations between users and the web 
                    application.<br><br>
                    With ChatGPT as a core component, ExamineAI provides a user-friendly interface 
                    for users to describe their symptoms, ask questions, and receive personalized 
                    recommendations. The model's ability to comprehend complex medical terminology 
                    and provide informative responses enhances the user experience and aids in 
                    assessing potential ailments.<br><br>
                    It's important to note that while ChatGPT is a sophisticated AI language model, 
                    it functions as an assistant and does not replace professional medical 
                    expertise. Its purpose is to assist users in gathering information and generating 
                    insights, but it should not be considered a substitute for medical advice or diagnosis. 
                    Users are encouraged to consult qualified healthcare professionals for accurate 
                    assessments and treatment plans.
                </p>
            </div>
        </div>
        <div class="box">
            <img src="../assets/HIPAA.png" class="d-inline-block" style="width: 10%;">
            <div class="ms-3 d-inline-block">
                <h2>HIPAA</h2>
                <p class="fs-5">
                    The protection of user data and privacy is of paramount importance to 
                    ExamineAI, and we adhere to strict security measures and regulations, 
                    including compliance with the Health Insurance Portability and 
                    Accountability Act (HIPAA). <br><br>
                    To meet HIPAA requirements, we implement robust technical and administrative 
                    safeguards to protect PHI from unauthorized access, use, or disclosure. This 
                    includes encryption of data in transit and at rest, strict access controls, 
                    regular security assessments, and comprehensive staff training on privacy 
                    practices. <br><br>
                    By complying with HIPAA, ExamineAI demonstrates its commitment to ensuring 
                    the privacy and security of user data. We understand the sensitivity of 
                    health-related information and take all necessary precautions to maintain 
                    the confidentiality and trust of our users.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style>
.setup {
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

.intro {
    margin-bottom: 50px;
}

.box {
    margin-top: 25px;
    margin-bottom: 125px;
    position: relative;
    text-align: left;
}

.box img {
    position: absolute;
    top: 0;
    left: 0;
}

.box div {
    padding-left: 12%;
}
</style>