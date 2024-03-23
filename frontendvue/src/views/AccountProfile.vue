<template>
  <div class="signup-container">
    <h1>Account Profile</h1>
    <div class="tabs">
      <button class="tab" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'">My Profile</button>
      <button class="tab" :class="{ 'active': activeTab === 'reservations' }" @click="activeTab = 'reservations'">My Reservations</button>
    </div>
    <div v-if="activeTab === 'profile'">
      <form @submit.prevent="saveProfile" class="signup-form">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="formData.username" :disabled="!isEditMode" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="formData.email" :disabled="!isEditMode" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="formData.password" :disabled="!isEditMode" required>
        </div>
      </form>
      <div class="button-container">
        <button v-if="!isEditMode" type="button" class="save-button" @click="toggleEditMode" style="width: 340px;">Edit</button>
        <button v-else type="submit" class="save-button" @click="saveProfile">Save Profile</button>
      </div>
    </div>
    <div v-else-if="activeTab === 'reservations'">
      <button class="report-button" @click="redirectToUserReport">
        Report Something <span class="icon"><i class="fas fa-flag"></i></span>
      </button>
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
      this.isEditMode = !this.isEditMode;
    },
    toggleEditMode() {
      this.isEditMode = !this.isEditMode;
    },
    redirectToUserReport() {
      this.$router.push('/userReport');
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
  background-color: #f1eff3;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.tabs {
  display: flex;
  margin-bottom: 20px;
}

.tab {
  flex: 1;
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
  padding: 10px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
}

button.save-button {
  background-color: #ada3b8;
  color: #fff;
  cursor: pointer;
}

button.save-button.edit-mode {
  width: auto;
}

button.save-button:hover {
  background-color: #90839c;
}

.form-group {
  display: flex;
  align-items: center;
}

.form-group label {
  min-width: 120px;
  margin-right: 10px;
}

.button-container {
  display: flex;
  justify-content: center;
}

.button-container button {
  margin: 10px;
}

.report-button {
  background-color: #ada3b8;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
}

.report-button:hover {
  background-color: #90839c;
}
</style>
