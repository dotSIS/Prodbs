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
            <div class="bundle">
                <Transition>
                    <div v-if="products.length" class="generated">
                        <h5>Products</h5>
                        <div class="scroll-bundle">
                            <div v-for="product in products" :key="product.id" class="generate">
                                <router-link :to="{}" @click="generateBundle(product.id)">
                                    <h2>
                                        {{ product.name }}
                                    </h2>
                                </router-link>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        <p class="generated-else">Loading products...</p>
                    </div>
                </Transition>
                <div class="divider"></div>
                <div class="suggestions">
                    <h5>Suggested Bundle Items</h5>
                    <Transition>
                        <div v-if="bundles.length" class="suggested">
                            <div v-for="bundle in bundles" :key="bundles.id" class="items">
                                <router-link :to="{}" @click.native="addToBundle(bundle)">
                                    <h2>{{ bundle.name }}</h2>
                                </router-link>
                            </div>
                            <button class="submit" @click="saveBundle()">Save</button>
                            Selected:
                            <div class="item-div">
                                <div v-for="item in bundle" :key="item" class="selected-items">
                                    <span class="selected-span">
                                        {{ item.name }}
                                    </span>
                                </div>
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
            products: [],
            product: [],
            bundles: [],
            bundle: [],
            tempBundle: [],
            item: '',
            seletedProductID: ''
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/products/')
            .then(res => res.json())
            .then((data) => {
                this.products = data;
            })
            .catch(err => console.log(err.message))
    },
    methods: {
        generateBundle(productID) {
           this.seletedProductID = productID
            this.bundle = []
            fetch('http://localhost:8000/api/generatebundle/?product=' + productID)
                .then(res => res.json())
                .then(bundle_data => {
                    this.bundles = [];
                    bundle_data['consequents'].forEach(element => {
                        fetch("http://localhost:8000/api/products/"+element+'/')
                        .then(res => res.json())
                        .then(prodRe => {
                            this.bundles.unshift(prodRe);
                        });
                    })
                })
                .catch(err => console.log(err.message))
        },
        addToBundle(item) {
            if (!this.bundle.includes(item)) {
                this.bundle.push(item)
            }
            else {
                this.tempBundle = []
                this.bundle.forEach((bb) => {
                    if(item.id != bb.id) this.tempBundle.unshift(bb)
                })
                this.bundle =  this.tempBundle;
            }
        },
        saveBundle() {
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ 'sellerID': "3324",})
            };
            fetch('http://localhost:8000/api/bundleproducts/',requestOptions)
            .then(resj => resj.json())
            .then((res)=>{
                    var id = res.id
                    let productBundle =[]
                    // seletedProductID
                    const data = {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(
                            {
                                'bundleProductID':id,
                                'productID':this.seletedProductID
                            }
                        )
                    };
                    fetch('http://localhost:8000/api/productbundle/',data).then((r)=>{
                        
                    })
                    this.bundle.forEach(
                        (bun)=>{
                            const data = {
                                method: "POST",
                                headers: { "Content-Type": "application/json" },
                                body: JSON.stringify(
                                    {
                                        'bundleProductID':id,
                                        'productID':bun.id
                                    }
                                )
                            };
                            fetch('http://localhost:8000/api/productbundle/',data).then((r)=>{
                                this.bundles = [],
                                this.bundle = []
                            })
                        }
                    )
                }
                    
            )
            
            // this.bundle.forEach((value)=>{
            //     productBundles.unshift(
            //         {
            //             ''
            //         }
            //     )
            // })
        }
    }
}
</script>

<style>
</style>