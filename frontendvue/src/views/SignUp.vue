<template>
  <div class="signup-container">
    <h1>Sign Up</h1>
    <form @submit.prevent="submitForm" class="signup-form">
      <div class="form-group">
        <label for="username" class="left-label">Username:</label>
        <input type="text" id="username" v-model="formData.username" required>
      </div>
      <div class="form-group">
        <label for="email" class="left-label">Email:</label>
        <input type="email" id="email" v-model="formData.email" required>
      </div>
      <div class="form-group">
        <label for="password" class="left-label">Password:</label>
        <input type="password" id="password" v-model="formData.password" required>
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

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
      axios.post('http://127.0.0.1:8000/accounts/user/', this.formData)
        .then(response => {
          console.log('User signed up:', response.data);
          alert('User signed up successfully!'); 
        })
        .catch(error => {
          console.error('There was an error!', error);
          alert('User signed up successfully!'); 
        });
    }
  }
}
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  background-color: #f1eff3;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center align the form items */
}

.form-group {
  margin-bottom: 15px;
  display: flex;
  align-items: center; /* Align items vertically */
}

.left-label {
  width: 100px; /* Set a fixed width for the labels */
  margin-right: 10px;
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
  margin-top: 10px; /* Added margin to separate the buttons */
}

button:hover {
  background-color: #90839c;
}
</style>
