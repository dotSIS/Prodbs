<template>
  <h1>Products</h1>
  <Transition>
    <div v-if="products.length">
      <div v-for="product in products" :key="product.id" class="product">
        <router-link :to="{name: 'ProductDetails', params: { id: product.id }}">
          <h2>{{ product.title }}</h2>
        </router-link>
      </div>
    </div>
    <div v-else>
      <p>Loading products...</p>
    </div>
  </Transition>
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
  .product h2{
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
  .product a{
    text-decoration: none;
  }
</style>