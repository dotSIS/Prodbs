<template>
    <div class="login">
        <h1>Admin Login</h1>
        <form>
            <label>Username:</label>
            <input type="text" required v-model="username">
            <label>Password:</label>
            <input type="password" required v-model="password">
            <div class="submit">
                <button @click="handleAuthentication">Login</button>
            </div>
        </form>
    </div>
</template>

<script>
</script>

<style>
</style>