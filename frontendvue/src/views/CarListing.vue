<template>
  <div class="reservations-container">
    <input type="text" v-model="username" placeholder="Enter username" class="input-field">
    <button @click="getAllReservations" class="btn-get-reservations">Get Reservations</button>
    <div v-if="reservations.length > 0" class="reservation-list">
      <h2 class="reservation-title">Reservations for {{ username }}</h2>
      <ul>
        <li v-for="reservation in reservations" :key="reservation.id" class="reservation-item">
          <span class="reservation-info">
            <span class="reservation-label">Car:</span> {{ reservation.car_name }},
            <span class="reservation-label">Profile:</span> {{ reservation.profile_name }},
            <span class="reservation-label">Start Date:</span> {{ reservation.start_date }},
            <span class="reservation-label">End Date:</span> {{ reservation.end_date }},
            <span class="reservation-label">Reservation Date:</span> {{ reservation.reservation_date }}
          </span>
        </li>
      </ul>
    </div>
    <div v-else class="no-reservations">
      <p>No reservations found for {{ username }}.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Reservations',
  data() {
    return {
      username: '',
      reservations: []
    };
  },
  methods: {
    getAllReservations() {
      axios.get('http://127.0.0.1:8000/accounts/reservations/', {
        params: { username: this.username }
      })
        .then(response => {
          this.reservations = response.data.filter(reservation => reservation.profile_name === this.username);
        })
        .catch(error => {
          console.error('Error fetching reservations:', error);
        });
    }
  }
}
</script>

<style>
.reservations-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #ada3b8;
  border-radius: 8px;
}

.input-field {
  width: 200px;
  padding: 8px;
  margin-bottom: 10px;
}

.btn-get-reservations {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.reservation-title {
  color: #333;
}

.reservation-list {
  margin-top: 20px;
}

.reservation-item {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #fff;
  border-radius: 4px;
}

.reservation-info {
  font-size: 14px;
}

.reservation-label {
  font-weight: bold;
  margin-right: 5px;
}

.no-reservations {
  margin-top: 20px;
  text-align: center;
  font-size: 16px;
}
</style>
