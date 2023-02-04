<template>
    <h1>Products</h1>
    <div class="box">
      <div class="user-options">
        <a href="">View Products</a>
        <a href="">Generate Bundle</a>
        <a href="">View Bundles</a>
        <a href="">View Analytics</a>
      </div>
    </div>
  </template>
  
  <script>
  export default {
  }
  </script>
  
  <style>
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
  </style>