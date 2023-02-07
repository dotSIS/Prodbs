<template>
    <img id="logo" src="./assets/logo.svg" alt="Prodbs Analytics logo">
    <div id="nav">
        <router-link :to="{ name: 'Home' }">Home</router-link>
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <router-link :to="{ name: 'Help' }">Help</router-link>
        <router-link :to="{ name: 'About' }">About</router-link>
        <router-link :to="{ name: 'Profile' }">Profile</router-link>
        <!-- <span v-if="authenticated">
          <router-link :to="{ name: 'Profile' }">Profile</router-link>
        </span> -->
    </div>
    <router-view/>
</template>

<script>
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        max-width: 960px;
        margin: 0 auto;
    }
    #logo {
        width: 20%;
        height: 20%;
    }
    #nav {
        padding: 30px;
    }
    #nav a {
        font-weight: bold;
        color: #2c3e50;
        text-decoration: none;
        padding: 10px;
        border-radius: 4px;
    }
    #nav a.router-link-exact-active {
        color: white;
        background: #42b983;
    }
    .login-options a{
        background: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
        margin: 10px auto;
        max-width: 600px;
        cursor: pointer;
        color: #444;
        text-decoration: none;
    }
    .login-options a:hover {
        background: #ddd;
    }
    form {
        max-width: 420px;
        margin: 30px auto;
        background: #ddd;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    button {
        background: #42b983;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 20px;
        cursor: pointer;
    }
    .submit {
        text-align: center;
    }
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
    .container {
        width: 640px;
        height: 276px;
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
