<template>
    <div class="login">
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
    .options a{
        background: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
        margin: 10px auto;
        max-width: 600px;
        cursor: pointer;
        color: #444;
        text-decoration: none;
    }
    .options a:hover {
        background: #ddd;
    }
</style>