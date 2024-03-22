<template>
  <div class="signup-container">
    <h1>Account Profile</h1>
    <div class="tabs">
      <button class="tab" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'">My Profile</button>
      <button class="tab" :class="{ 'active': activeTab === 'reservations' }" @click="activeTab = 'reservations'">My Reservations</button>
    </div>
    <div v-if="activeTab === 'profile'">
      <form @submit.prevent="saveProfile" class="signup-form">
        <div class="form-row">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="formData.username" :disabled="!isEditMode" required>
        </div>
        <div class="form-row">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="formData.email" :disabled="!isEditMode" required>
        </div>
        <div class="form-row">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="formData.password" :disabled="!isEditMode" required>
        </div>
        <div class="form-row">
          <button v-if="!isEditMode" type="button" class="save-button" @click="toggleEditMode">Edit</button>
          <button v-else type="submit" class="save-button">Save Profile</button>
        </div>
      </form>
    </div>
    <div v-else-if="activeTab === 'reservations'">
      <p>Your reservation details go here.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        username: 'JohnDoe',
        email: 'johndoe@example.com',
        password: '******'
      },
      isEditMode: false,
      activeTab: 'profile'
    };
  },
  methods: {
    saveProfile() {
      console.log('Profile saved with data:', this.formData);
      this.isEditMode = false;
    },
    toggleEditMode() {
      this.isEditMode = !this.isEditMode;
    }
  }
};
</script>

<style scoped>

.signup-container {
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
