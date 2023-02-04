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
  .product h2 {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
    margin: 10px auto;
    max-width: 600px;
    cursor: pointer;
    color: #444;
  }
  .product h2:hover {
    background: #ddd;
  }
  .product a {
    text-decoration: none;
  }
  .product img {
    width: 5%;
    height: 5%;
  }
</style>