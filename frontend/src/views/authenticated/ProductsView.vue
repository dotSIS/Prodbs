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
          <Transition>
              <div v-if="products.length">
                  <div v-for="product in products" :key="product.id" class="product">
                      <router-link :to="{name: 'ProductDetails', params: { id: product.id }}">
                          <h2>
                              <img src="../../assets/dis1.png" alt="product image">
                              {{ product.title }}
                          </h2>
                      </router-link>
                  </div>
              </div>
              <div v-else>
                  <p>Loading products...</p>  
              </div>
          </Transition>
        </div>
    </div>
</template>

<script>
export default {
      data() {
          return {
              products: [],
        }
    },
    mounted() {
        fetch('http://localhost:3000/products')
            .then(res => res.json())
            .then(data => this.products = data)
            .catch(err => console.log(err.message))
    }
}
</script>

<style>
</style>