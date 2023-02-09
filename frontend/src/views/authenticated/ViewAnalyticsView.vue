<template>
    <h1>View Analytics</h1>
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
                    <div v-if="analytics.length" class="generated">
                        <h5>Months</h5>
                        <div class="scroll-bundle">
                            <div v-for="xdata in analytics.reverse()" :key="xdata" class="generate">
                                <router-link :to="{}">
                                    <h2>
                                        {{ xdata['number'] + " = ₱" + xdata['value'] + ".0" }}
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
                <div class="suggestions" style="overflow-y: auto;">
                    <h5>Years</h5>
                    <Transition>
                        <div v-if="analytics1.length" class="suggested">
                            <div v-for="xdata in analytics1.reverse()" :key="xdata" class="items">
                                <h2>
                                    {{ xdata['number'] + " = $" + xdata['value'] + ".0" }}
                                </h2>
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
    data() {
        return {
            analytics: [],
            analytics1: [],
            months: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            years: []
        }
    },
    mounted() {
        fetch('http://localhost:8000/api/getanalytics/')
            .then(res => res.json())
            .then((data) => {
                var count =1
                for(var x in data[0]){
                    this.analytics.unshift(
                        {
                            'number':this.months[count-1],
                            'value':data[0][x]
                        }
                    )
                    count+=1
                }
                var count =1
                for(var x in data[1]){
                    this.analytics1.unshift(
                        {
                            'number':x,
                            'value':data[1][x]
                        }
                    )
                    count+=1
                }
            })
            .catch(err => console.log(err.message))
    }
}
</script>

<style>
</style>