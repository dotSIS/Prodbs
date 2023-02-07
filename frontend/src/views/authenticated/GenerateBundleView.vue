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
        <div class="container">
            <Transition>
                <h2>Generate bundle area...</h2>
            </Transition>
        </div>
    </div>
</template>
  
<script>
</script>

<style>
</style>