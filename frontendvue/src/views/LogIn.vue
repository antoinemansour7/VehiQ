<template>
    <div class="logIn-container">
    <h1>Log In</h1>
    <div class="tabs">
      <button class="tab" :class="{ 'active': activeTab === 'logInAdmin' }" @click="activeTab = 'logInAdmin'">Log In as an Admin</button>
      <button class="tab" :class="{ 'active': activeTab === 'logInUser' }" @click="activeTab = 'logInUser'">Log In as an User</button>
    </div>
    <div v-if="activeTab === 'logInAdmin'">
      <form class="login-form">
        <div class="form-row">
          <label for="username">Username:</label>
          <input type="text" id="username" required>
        </div>
        <div class="form-row">
          <label for="password">Password:</label>
          <input type="password" id="password" required>
        </div>
      </form>
      <button type="button" @click="logInAsAdmin">Log In</button>
    </div>
    <div v-else-if="activeTab === 'logInUser'">
        <form class="login-form">
        <div class="form-row">
          <label for="username">Username:</label>
          <input type="text" id="username" required>
        </div>
        <div class="form-row">
          <label for="password">Password:</label>
          <input type="password" id="password" required>
        </div>
      </form>
      <button type="button" @click="logInAsUser">Log In</button>
    </div>
  </div>
     
</template>

<script>
    //import axios from 'axios';

export default {
  data() {
    return {
        activeTab: 'logInAdmin',
        formData: {
            username: '',
            password: ''
        }
    };
  },
  methods: {
    // These methods have to be fixed once backend is done
    logInAsAdmin() {
      // Logic to handle signing up as admin
      console.log('Signing up as admin with data:', this.formData);
      // Reset form data after submission
      this.formData = {
        username: '',
        password: ''
      };
      // Redirect to login page
      window.location.href = 'http://127.0.0.1:8000/admin/';
    },
    logInAsUser() {
      // Logic to handle signing up as admin
      console.log('Signing up as admin with data:', this.formData);
      // Reset form data after submission
      this.formData = {
        username: '',
        password: ''
      };
      // Redirect to login page
      //window.location.href = 'http://127.0.0.1:8000/admin/';
    }
  }
}
</script>

<style scoped>
h1, p{
  color: #544e63;
}

.logIn-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
}

.tabs {
  margin-bottom: 20px;
  font-size: 20px;
}

.tab {
  background-color: #d8d2de;
  color: white;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 15px 30px;
  margin: 0 10px;
  border-radius: 5px 5px 0 0;
  transition: background-color 0.3s;
}

.tab:hover {
  background-color: #8c7aa7;
}

.tab.active {
  background-color: #ada3b8;
}

.login-form {
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
input[type="password"],
button {
  padding: 6px 12px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
}

.save-button{
  width: 340px;
}

button {
  background-color: #ada3b8;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #90839c;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-row {
  display: flex;
  align-items: center;
  margin-left: 80px;
  margin-bottom: 15px; /* Adjust as needed */
}

.form-row label {
  width: 120px; /* Set a fixed width for labels to ensure consistent alignment */
  margin-right: 10px; /* Adjust as needed */
}

</style>