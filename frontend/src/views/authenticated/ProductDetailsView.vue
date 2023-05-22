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
            <div class="bundle">
                <Transition>
                    <div v-if="product" class="generated">
                        <h5>{{ product.name }}</h5>
                        <div class="scroll-bundle">
                            <p>{{ product.spec }}</p>
                            <h5>{{"Price: ₱" + product.price + ".0"}}</h5>
                        </div>
                        <button @click="getReview(allSentiments)">All {{ allSentiments.length }}</button>
                        <button @click="getReview(positiveSentiments)">Positive {{ positiveSentiments.length }}</button>
                        <button @click="getReview(negativeSentiments)">Negative {{ negativeSentiments.length }}</button>
                        <button @click="getReview(neutralSentiments)">Neutral {{ neutralSentiments.length }}</button>
                    </div>
                    <div v-else>
                        <p class="generated-else">Loading product details...</p>
                    </div>
                </Transition>
                <div class="divider"></div>
                <div class="suggestions1">
                    <h5>Reviews</h5>
                    <Transition>
                        <div class="suggested">
                            <div v-for="review in reviews" :key="review.id" class="items">
                                <div>
                                    <h4>{{ review['customerName'] }}</h4>
                                    <p>{{ review['textContent'] }}</p>
                                    <p>{{ review['reviewDate'] }}</p>
                                </div>
                            </div>
                        </div>
                    </Transition>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductDetails',
    props: ['id'],
    data() {
        return {
            reviews: [],
            product: [],
            allSentiments: [],
            positiveSentiments: [],
            negativeSentiments: [],
            neutralSentiments: []
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/products/' + this.id + '/')
            .then(res => res.json())
            .then(data => this.product = data)
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
        getReview(sentiment) {
            this.reviews = []
            for(var value in sentiment){
                fetch('http://localhost:8000/api/reviews/' + sentiment[value]['reviewID'] + '/')
                    .then(res => res.json())
                    .then(data => {
                        this.reviews.unshift(data)
                    })
                    .catch(err => console.log(err.message))
            }
        }
    }
}
</script>

<style>
</style>