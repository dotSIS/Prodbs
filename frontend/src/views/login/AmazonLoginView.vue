<template>
    <h1>Amazon Login</h1>
    <div class="submit">
        <button>Login</button>
    </div>
</template>

<script>
export default {
    name: 'AmazonLogin',
    data() {
        return {
            authenticated: false
        }
    },
    methods: {
        handleAuthentication() {
            this.authenticated = !this.authenticated
        }
    }
}
</script>

<style>
</style>