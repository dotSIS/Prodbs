<template>
  <div v-if="product">
    <h1>{{ product.title }}</h1>
    <p>{{ product.details }}</p>
  </div>
  <div v-else>
    <p>Loading product details...</p>
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