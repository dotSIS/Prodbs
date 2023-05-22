<template>
    <h1>Profile</h1>
    <div class="box">
        <div class="user-options">
            <router-link :to="{ name: 'Products' }">View Products</router-link>
            <router-link :to="{ name: 'GenerateBundle' }">Generate Bundle</router-link>
            <router-link :to="{ name: 'ViewBundles' }">View Bundles</router-link>
            <router-link :to="{ name: 'ViewAnalytics' }">View Analytics</router-link>
        </div>
        <div class="container">
            <router-view/>
            <h5>Logged in user: 
                {{ user.firstName }}
            </h5>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: ''
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/users/3324/')
            .then(res => res.json())
            .then(data => this.user = data)
            .catch(err => console.log(err.message))
    }
}
</script>
  
<style>
</style>