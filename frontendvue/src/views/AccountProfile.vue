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
        <div class="details">
          
          <p><strong>Car Make:</strong> {{ reservation.car_details.make }}</p>
          <p><strong>Car Model:</strong> {{ reservation.car_details.model }}</p>
          <p><strong>Start Date:</strong> {{ reservation.start_date }}</p>
          <p><strong>End Date:</strong> {{ reservation.end_date }}</p>
          <p><strong>Reservation Date:</strong> {{ reservation.reservation_date }}</p>
          <p><strong>Picking Up at:</strong> {{ reservation.pickup_location}}</p>
          <p><strong>Dropping Off at:</strong> {{ reservation.dropoff_location}}</p>
         
          <p><strong>Reserved By:</strong> {{ reservation.user_details.user }}</p>
        </div>
        <div class="features">
          <button @click="deleteReservation(reservation.id)">Delete</button>
          <button>Modify</button>
          <button @click="confirmReservation(reservation.id,reservation.pickup_location)">Confirm</button>
          <!--Report button-->
          <button @click="redirectToUserReport">
              <span class="icon"><i class="fas fa-flag"></i></span>
          </button>
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
      reservations: []
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
          const reservationsWithDetails = response.data.map(async reservation => {
 
      const carResponse = await axios.get(`http://127.0.0.1:8000/vehicles/cars/${reservation.car}`);
      const carDetails = carResponse.data;

      const userResponse = await axios.get(`http://127.0.0.1:8000/accounts/user/${reservation.user}`);
      const userDetails = userResponse.data;

 
      return {
        ...reservation,
        car_details: carDetails,
        user_details: userDetails
    
        };
      });
        
          Promise.all(reservationsWithDetails)
            .then(reservations => {
              this.reservations = reservations;
            })
            .catch(error => {
              console.error('Error fetching reservation details:', error);
            });
        })
        .catch(error => {
          console.error('Error fetching reservations:', error);
        });
    },
    deleteReservation(id) {
      axios.delete(`http://127.0.0.1:8000/accounts/reservations/${id}/`)
        .then(() => {
          this.reservations = this.reservations.filter(reservation => reservation.id !== id);
        })
        .catch(error => {
          console.error("Error deleting reservation:", error);
        });
    },
    confirmReservation(id,pickup_location) {
      alert(`Reservation ID: ${id}`); 
      this.$router.push({ name: 'paymentPage', query: { id: id, pickup_location:pickup_location } });

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

.rental-car-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

button {
  background-color: #ada3b8;
  color: #fff;
  cursor: pointer;
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
}

button:hover {
  background-color: #90839c;
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
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
.rental-car {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.details {
  margin-bottom: 20px;
}
.features {
    display: flex;
    align-items: flex-end;
    
}

/* Additional styles for Bulma icons */
.icon {
  vertical-align: middle; /* Align the icon vertically with button text */
}
</style>
