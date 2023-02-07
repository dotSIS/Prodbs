<template>
    <h1>Products</h1>
    <div class="box">
        <div class="user-options">
            <router-link :to="{ name: 'Products' }">View Products</router-link>
            <router-link :to="{ name: 'GenerateBundle' }">Generate Bundle</router-link>
            <router-link :to="{ name: 'ViewBundles' }">View Bundles</router-link>
            <router-link :to="{ name: 'ViewAnalytics' }">View Analytics</router-link>
        </div>
        <router-view/>
        <div class="container">
            <div v-if="product">
                <h1>{{ product.title }}</h1>
                <p>{{ product.details }}</p>
            </div>
            <div v-else>
                <p>Loading product details...</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['id'],
    data() {
        return {
            product: null
        }
    },
    mounted() {
        fetch('http://localhost:3000/products/' + this.id)
            .then(res => res.json())
            .then(data => this.product = data)
            .catch(err => console.log(err.message))
    }
}
</script>

<style>
</style>