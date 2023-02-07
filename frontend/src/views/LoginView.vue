<template>
    <div class="login-options">
        <h1>Login Page</h1>
        <div class="options">
            <router-link :to="{ name: 'AmazonLogin' }">Login with Amazon</router-link>
            <router-link :to="{ name: 'AdminLogin' }">Login as Administrator</router-link>
        </div>
        <router-view/>
    </div>
</template>
  
<script>
import AdminLoginView from './login/AdminLoginView.vue';

export default {
    name: 'Login'
}
</script>

<style>
</style>