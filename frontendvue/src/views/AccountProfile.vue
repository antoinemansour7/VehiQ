<template>
  <div class="profile-container">
    <h1>Account Profile</h1>
    <div class="tabs">
      <button class="tab" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'">My Profile</button>
      <button class="tab" :class="{ 'active': activeTab === 'reservations' }" @click="activeTab = 'reservations'">My Reservations</button>
    </div>
    <div v-if="activeTab === 'profile'">
      <form @submit.prevent="saveProfile" class="profile-form">
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
        <div class="button-container">
          <button v-if="!isEditMode" type="button" class="save-button" @click="toggleEditMode" style="width: 340px;">Edit</button>
          <button v-else type="submit" class="save-button" @click="saveProfile" style="width: 340px;">Save Profile</button>
        </div>
      </form>
      
    </div>
    <div v-else-if="activeTab === 'reservations'">
      
      <div class="rental-car-list">
        <div v-for="(reservation, index) in reservations" :key="index" class="rental-car">
          <div class="button-container">
            <!-- Delete button -->
            <button class="button-looking small-button" @click="deleteReservation(reservation.id)">
              <span class="icon"><i class="fas fa-trash"></i></span>
            </button>
            <!-- Edit button -->
            <button class="button-looking small-button">
              <span class="icon"><i class="fas fa-edit"></i></span>
            </button>
            <!-- Report button -->
            <button class="button-looking small-button" @click="redirectToUserReport">
              <span class="icon"><i class="fas fa-flag"></i></span>
            </button>
          </div>
          <div class="details">
            <h3>{{ reservation.car_name }}</h3>
            <p><strong>Start Date:</strong> {{ reservation.start_date }}</p>
            <p><strong>End Date:</strong> {{ reservation.end_date }}</p>
            <p><strong>Reserved By:</strong> {{ reservation.user_name }}</p>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      formData: {
        username: 'JohnDoe',
        email: 'johndoe@example.com',
        password: '******'
      },
      isEditMode: false,
      activeTab: 'profile',
      cars: []
    }
  },
  mounted() {
    this.getReservations()
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
    },
    getReservations() {
      axios.get('http://127.0.0.1:8000/accounts/reservations/')
        .then(response => {
          this.reservations = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteReservation(id) {
      axios.delete(`http://127.0.0.1:8000/accounts/reservations/${id}/`)
        .then(() => {
          this.reservations = this.reservations.filter(reservation => reservation.id !== id);
        })
        .catch(error => {
          console.error("Error deleting reservation:", error);
        });
    }
  }
};
</script>

<style scoped>
.profile-container {
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

.profile-form {
  display: flex;
  flex-direction: column;
  justify-content: space-between; 
  height: 100%; 
}

.form-group {
  margin-bottom: 20px;
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
  box-sizing: border-box;
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
  align-items: center; 
  margin-top: 20px;
  margin: 0 auto;
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


.rental-car-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.rental-car {
    margin: 10px;
    padding: 10px;
    border: 1px solid black;
    border-radius: 5px;
    width: 300px;
    position: relative;
}
.rental-car img{
    width:100%;
    height: auto;
    border-radius: 5px;
}
.details p:last-child {
    position: absolute;
    margin-top: 10px;
    margin-bottom: 10px;
    bottom: 5px;
    right: 20px;
    font: bold 20px Arial, sans-serif;
}
.features {
    display: flex;
    align-items: flex-end;
    
}
.features img {
    height: 50px;
    width: 50px;
    margin-right: 10px;
}
.button-looking {
  background-color: #ada3b8; 
  color: #fff; 
  cursor: pointer;
  padding: 15px 32px;
  border: none;
  font-size: 16px;
  border-radius: 5px;
  margin: 4px 2px;
  transition: background-color 0.3s;
}

/* Hover effect */
.button-looking:hover {
  background-color: #90839c; 
}

.button-container {
  align-self: flex-end;
  margin-top: 20px;
}

.small-button {
  margin: 2px;
  font-size: 10px;
}

/* Additional styles for Bulma icons */
.icon {
  vertical-align: middle; /* Align the icon vertically with button text */
}
</style>
