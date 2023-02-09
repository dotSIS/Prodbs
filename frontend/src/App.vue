<template>
    <img id="logo" src="./assets/logo.svg" alt="Prodbs Analytics logo">
    <div id="nav">
        <router-link :to="{ name: 'Home' }">Home</router-link>
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <router-link :to="{ name: 'Help' }">Help</router-link>
        <router-link :to="{ name: 'About' }">About</router-link>
        <router-link :to="{ name: 'Profile' }">Profile</router-link>
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
        width: 70px;
        height: 43px;
        font-weight: bold;
        color: #2c3e50;
        text-decoration: none;
        padding: 10px;
        border-radius: 4px;
    }
    #nav a:hover {
        background: #ddd;
    }
    #nav a.router-link-exact-active {
        color: white;
        background: #42b983;
    }
    .login-options a{
        background: #f4f4f4;
        padding: 20px;
        border-radius: 25px;
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
        gap: 15px;
    }
    .user-options a {
        font-size: 15px;
        background: white;
        padding: 10px;
        border: 1px solid #42b983;
        border-radius: 25px;
        text-decoration: none;
    }
    .user-options a:hover {
        color: #2c3e50;
        border: 1px solid #ddd;
        /* background: #42b983; */
        background: #ddd;
    }
    .user-options a.router-link-exact-active {
        color: white;
        background: #42b983;
    }
    .container {
        width: 640px;
        height: 320px;
        padding: 10px;
        border: 1px solid #444;
        border-radius: 5px;
        overflow-y: auto;
    }
    .container p {
        font-size: 0.8em;
    }
    .bundle {
        height: 320px;
        display: flex;
        flex-direction: row;
    }
    .bundle .generated {
        width: 50%;
        border-radius: 10px;
        overflow-y: auto;
    }
    .bundle .generated-else {
        width: 319px;
        height: 320px;
    }
    .bundle .generate h2 {
        background: #f4f4f4;
        font-size: 0.7em;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 10px;
        width: 260px;
        height: 10px;
        cursor: pointer;
        color: #444;
    }
    .bundle .generate h2:hover {
        background: #ddd;
    }
    .bundle .generate a {
        text-decoration: none;
    }
    .divider {
        border: 1px solid #444;
    }
    .suggestions {
        width: 50%;
        overflow-y: hidden;
        overflow-x: hidden;
    }
    .suggestions1 {
        width: 50%;
        overflow-y: auto;
        overflow-x: hidden;
    }
    .suggestions .suggested {
        width: 319px;
        height: 320px;
        padding: 0px 10px 10px 10px;
    }
    .suggested-else {
        width: 319px;
        height: 320px;
    }
    .suggestions .suggested h2 {
        background: #f4f4f4;
        font-size: 0.7em;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 10px;
        width: 260px;
        height: 10px;
        cursor: pointer;
        color: #444;
    }
    .suggestions .suggested h2:hover {
        background: #ddd;
    }
    .suggestions .suggested .item-div {
        display: flex;
        flex-direction: row;
    }
    .suggestions .suggested .submit:hover {
        background: #ddd;
        color: black;
    }
    .suggestions .suggested .selected-items {
        background: transparent;
        color: #444;
        padding: 5px 5px 5px 5px;
        margin: 5px 5px 5px 5px;
        border-radius: 10px;
    }
    .suggestions .suggested span {
        font-size: 0.6em;
        border-radius: 10px;
    }
    .suggestions .items a {
        text-decoration: none;
    }
    div.sort button {
        width: 75px;
        height: 39px;
        color: #42b983;
        background: white;
        padding: 10px;
        border: 1px solid #42b983;
    }
    div.sort button:hover {
        color: #2c3e50;
        background: #42b983;
        padding: 10px;
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
    .bundle h2 {
        background: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
        margin: 10px auto;
        max-width: 600px;
        cursor: pointer;
        color: #444;
    }
    .bundle h2:hover {
        background: #ddd;
    }
    .bundle a {
        text-decoration: none;
    }
    .bundles-view {
        height: 320px;
        display: flex;
        flex-direction: row;
    }
    .bundles-view .generated {
        width: 50%;
        border-radius: 10px;
        overflow-y: auto;
    }
    .bundles-view .generated-else {
        width: 319px;
        height: 320px;
    }
    .bundles-view .generate h2 {
        background: #f4f4f4;
        font-size: 0.7em;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 10px;
        width: 260px;
        height: 10px;
        cursor: pointer;
        color: #444;
    }
    .bundles-view .generate h2:hover {
        background: #ddd;
    }
    .bundles-view .generate a {
        text-decoration: none;
    }
    .divider {
        border: 1px solid #444;
    }
</style>
