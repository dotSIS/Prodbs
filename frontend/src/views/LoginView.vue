<template>
    <div class="login-options">
        <h1>Login Page</h1>
        <div class="options">
            <router-link :to="{ name: 'AmazonLogin' }">Login with Amazon</router-link>
            <!-- <router-link :to="{ name: 'AdminLogin' }">Login as Administrator</router-link> -->
            <a href="http://localhost:8000/admin">Login as Administrator</a>
        </div>
        <router-view/>
    </div>
</template>
  
<script>
</script>

<style>
</style>