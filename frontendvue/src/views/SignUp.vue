<template>
    <div class="signup-container">
      <h1>Sign Up</h1>
      <form @submit.prevent="submitForm" class="signup-form">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="formData.username" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="formData.password" required>
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          username: '',
          email: '',
          password: ''
        }
      };
    },
    methods: {
      submitForm() {
        console.log('Form submitted with data:', this.formData);
        this.formData = {
          username: '',
          email: '',
          password: ''
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .signup-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ada3b8; 
    border-radius: 5px;
    background-color: #eae7ed;
  }
  
  .signup-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    font-weight: bold;
    color: #544e63;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"],
  button {
    padding: 8px;
    border: 1px solid #ada3b8;
    border-radius: 5px;
  }
  
  button {
    background-color: #ada3b8; 
    color: #fff;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #90839c;
  }
  
  </style>
  