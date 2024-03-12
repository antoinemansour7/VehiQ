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
      <button type="button" @click="signUpAsAdmin">Sign Up as Admin</button>
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
      axios.post('http://127.0.0.1:8000/accounts/create_user/', this.formData)
        .then(response => {
          console.log('User signed up:', response.data);
          alert('User signed up successfully!'); 
          
        })
        .catch(error => {
          console.error('There was an error!', error);
          alert('User signed up successfully!'); 
        });
      }
    },
    signUpAsAdmin() {
      // Logic to handle signing up as admin
      console.log('Signing up as admin with data:', this.formData);
      // Reset form data after submission
      this.formData = {
        username: '',
        email: '',
        password: ''
      };
      // Redirect to login page
      window.location.href = 'http://127.0.0.1:8000/admin/login/?next=/admin//';
    }
  }

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
  margin-top: 10px; /* Added margin to separate the buttons */
}

button:hover {
  background-color: #90839c;
}
</style>
