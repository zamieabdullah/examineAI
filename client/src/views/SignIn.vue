<template>
<div class="container" style="margin-top: 10%;">
    <div class="d-flex justify-content-center">
        <form class="card p-5">
            <div class="form-outline mb-4">
                <input type="email" class="form-control" placeholder="Email Address" v-model="email"/>
            </div>
            <div class="form-outline mb-4">
                <input :type="hide" id="password" class="form-control" placeholder="Password" v-model="password"/>
            </div>
            <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" :value="remember_me" @click="handleRemember" :checked="remember_me"/>
                        <label class="form-check-label">Remember me</label>
                    </div>
                </div>
    
                <div class="col">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="checked" @click="handleHide" checked/>
                        <label class="form-check-label">Hide Password</label>
                    </div>
                </div>
            </div>
            <button type="button" class="btn btn-primary btn-block mb-4" @click.prevent="handleSubmit">Sign in</button>
            <div class="text-center">
                <p>Not a member? <a href="#!">Register</a></p>
            </div>
        </form>
    </div>
</div>
</template>

<script>
import Cookies from 'js-cookie';
export default {
    data() {
        return {
            email: '',
            password: '',
            remember: false,
            hidden: 'password'
        }
    },
    methods: {
        handleHide(event) {
            if (event.target.value === "checked") {
                event.target.value = "unchecked";
                this.hidden = "text";
            } else {
                event.target.value = "checked";
                this.hidden = "password";
            }
        },
        handleRemember(event) {
            if (JSON.parse(event.target.value) === true) {
                this.remember = false;
            } else {
                this.remember = true;
            }
        },
        handleSubmit() {
            console.log(this.email);
            console.log(this.password);
            console.log(this.remember);
            if (this.remember) {
                Cookies.set('email_address', this.email, {expires: 1});
            } else {
                Cookies.remove('email_address');
            }
        }
    },
    computed: {
        hide: function() {
            return this.hidden;
        },
        remember_me: function() {
            return this.remember;
        }
    },
    mounted() {
        const email = Cookies.get('email_address');
        if (email) {
            this.email = email;
            this.remember = true;
        }
    }
}
</script>

<style>
</style>