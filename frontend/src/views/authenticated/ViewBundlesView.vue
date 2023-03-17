<template>
    <h1>View Bundles</h1>
    <div class="box">
        <div class="user-options">
            <router-link :to="{ name: 'Products' }">View Products</router-link>
            <router-link :to="{ name: 'GenerateBundle' }">Generate Bundle</router-link>
            <router-link :to="{ name: 'ViewBundles' }">View Bundles</router-link>
            <router-link :to="{ name: 'ViewAnalytics' }">View Analytics</router-link>
        </div>
        <router-view/>
        <div class="container">
            <div class="bundles-view">
                <Transition>
                    <div v-if="bundles.length" class="generated">
                        <h5>Bundles</h5>
                        <div class="scroll-bundle">
                            <div v-for="bundle in bundles" :key="bundle.id" class="generate">
                                <router-link :to="{}" @click="viewBundle(bundle.id)">
                                    <h2>
                                        {{ "Bundle ID: " + bundle.id }}
                                    </h2>
                                </router-link>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        <p class="generated-else">Loading bundles...</p>
                    </div>
                </Transition>
                <div class="divider"></div>
                <div class="suggestions">
                    <h5>Bundled Items</h5>
                    <Transition>
                        <div v-if="products.length" class="suggested">
                            <div v-for="product in products" :key="product.id" class="items">
                                <router-link :to="{name: 'ProductDetails', params: { id: product.id }}">
                                    <h2>{{ product.name }}</h2>
                                </router-link>
                            </div>
                        </div>
                        <div v-else>
                            <p class="suggested-else">Select product...</p>  
                        </div>
                    </Transition>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            bundle: [],
            bundles: [],
            products:[]
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/bundleproducts/')
            .then(res => res.json())
            .then((data) => {
                this.bundles = data
            })
            .catch(err => console.log(err.message))
    },
    methods: {
        viewBundle(bundle){
            fetch('http://localhost:8000/api/productbundle/?bundleproduct=' + bundle)
                .then(res => res.json())
                .then(data => {
                    this.products = []
                    data.forEach(element => {
                        fetch("http://localhost:8000/api/products/" + element.productID+'/')
                        .then(res => res.json())
                        .then(prodRe => {
                            this.products.unshift(prodRe);
                        });
                    })
                })
                .catch(err => console.log(err.message))
        }
    }
}
</script>

<style>
</style>