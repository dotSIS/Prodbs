<template>
    <h1>Generate Bundle</h1>
    <div class="box">
        <div class="user-options">
            <router-link :to="{ name: 'Products' }">View Products</router-link>
            <router-link :to="{ name: 'GenerateBundle' }">Generate Bundle</router-link>
            <router-link :to="{ name: 'ViewBundles' }">View Bundles</router-link>
            <router-link :to="{ name: 'ViewAnalytics' }">View Analytics</router-link>
        </div>
        <router-view/>
        <Transition>
            <h2>Generate bundle area...</h2>
        </Transition>
    </div>
</template>
  
<script>
</script>

<style>
    .box {
        display: inline-flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .user-options {
        margin: 10px;
        display: inline-flex;
        flex-direction: column;
        gap: 5px;
    }
    .user-options a {
        font-size: 15px;
        background: white;
        border: 1px solid #42b983;
        border-radius: 25px;
        text-decoration: none;
    }
    .user-options a:hover {
        color: white;
        background: #42b983;
        border: 1px solid black;
    }
</style>