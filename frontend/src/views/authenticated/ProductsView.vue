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
                <div v-if="products.length" class="generated">
                    <div v-for="product in products" :key="product.id" class="product">
                        <router-link :to="{name: 'ProductDetails', params: { id: product.id }}">
                            <h2>
                                {{ product.name }}
                            </h2>
                        </router-link>
                        </div>
                </div>
                <div v-else>
                    <p class="generated-else">Loading products...</p>  
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
            reviews: [],
            allSentiments: [],
            positiveSentiments: [],
            negativeSentiments: [],
            neutralSentiments: []
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/products/')
            .then(res => res.json())
            .then(data => this.products = data)
            .catch(err => console.log(err.message))

        fetch('http://localhost:8000/api/analizeproductreviews/?product=' + this.id)
            .then(res => res.json())
            .then(data => {
                data.forEach(element => {
                    this.allSentiments.unshift(element)
                    switch (element['overallSentiment']) {
                        case "Positive":
                            this.positiveSentiments.unshift(element)
                            break;
                        case "Negative":
                            this.negativeSentiments.unshift(element)
                            break;
                        case "Neutral":
                            this.neutralSentiments.unshift(element)
                            break;
                        default:
                            break;
                    }
                    
                });
            })
            .catch(err => console.log(err.message))
    },
    methods: {
    }
}
</script>

<style>
</style>