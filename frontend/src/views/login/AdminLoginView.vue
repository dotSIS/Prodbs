<template>
    <div class="login">
        <h1>Admin Login</h1>
        <form>
            <label>Username:</label>
            <input type="text" required v-model="username">
            <label>Password:</label>
            <input type="password" required v-model="password">
            <div class="submit">
                <button>Login</button>
            </div>
        </form>
    </div>
</template>
  
<script>
export default {
    name: 'AdminLogin'
}
</script>

<style>
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
</style>