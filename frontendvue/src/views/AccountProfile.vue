<template>
  <div>
    <h1>Profile</h1>
    <div class="tabs">
      <button class="tab" :class="{ 'active': activeTab === 'information' }" @click="activeTab = 'information'">My Information</button>
      <button class="tab" :class="{ 'active': activeTab === 'reservations' }" @click="activeTab = 'reservations'">My Reservations</button>
    </div>
    <div v-if="activeTab === 'information'">
      <!-- Content for My Information tab -->
      <form v-if="!isEditMode" @submit.prevent="saveInformation">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="userInfo.username" disabled>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="userInfo.email" disabled>
        <br>
        <button class="edit-button" @click="toggleEditMode">Edit</button>
      </form>
      <form v-else @submit.prevent="saveInformation">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="userInfo.username">
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="userInfo.email">
        <br>
        <button class="save-button">Save</button>
      </form>
    </div>
    <div v-else-if="activeTab === 'reservations'">
      <!-- Content for My Reservations tab -->
      <p>Your reservation details go here.</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'; // Importing ref from Vue

export default {
  setup() {
    const activeTab = ref('information'); // Using ref to create reactive variable
    const isEditMode = ref(false); // Indicates whether the form is in edit mode

    const userInfo = ref({
      username: 'JohnDoe', // Sample username
      email: 'johndoe@example.com' // Sample email
    });

    // Function to toggle between edit mode and read-only mode
    const toggleEditMode = () => {
      isEditMode.value = !isEditMode.value;
    };

    // Function to save user information
    const saveInformation = () => {
      // Logic to save user information
      toggleEditMode(); // Toggle back to read-only mode after saving
    };

    return {
      activeTab,
      isEditMode,
      userInfo,
      toggleEditMode,
      saveInformation
    };
  }
};
</script>

<style scoped>
/* CSS for tabs */
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
  transition: background-color 0.3s; /* Add transition for smooth color change */
}

.tab:hover {
  background-color: #8c7aa7; /* Change color on hover */
}

.tab.active {
  background-color: #ada3b8; /* Change color for active tab */
}

/* Other styles remain the same */
.save-button {
  background-color: #ada3b8; /* Match with the color scheme */
  color: white;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s; /* Add transition for smooth color change */
}

.save-button:hover {
  background-color: #91859e; /* Change color on hover */
}
</style>
