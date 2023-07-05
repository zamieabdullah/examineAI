<template>
<div class="container" style="margin-top: 10%;">
    <div class="d-flex justify-content-center">
        <form class="card p-5">
            <div class="form-outline mb-4">
                <input type="email" class="form-control" placeholder="Email Address"/>
            </div>
            <div class="form-outline mb-4">
                <input :type="hide" id="password" class="form-control" placeholder="Password"/>
            </div>
            <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" checked />
                        <label class="form-check-label"> Remember me </label>
                    </div>
                </div>
    
                <div class="col">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="hide" value="checked" @click="handleHide" checked />
                        <label class="form-check-label"> Hide Password </label>
                    </div>
                </div>
            </div>
            <button type="button" class="btn btn-primary btn-block mb-4">Sign in</button>
            <div class="text-center">
                <p>Not a member? <a href="#!">Register</a></p>
            </div>
        </form>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
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
        }
    },
    computed: {
        hide: function() {
            return this.hidden;
        }
    }
}
</script>

<style>
</style>