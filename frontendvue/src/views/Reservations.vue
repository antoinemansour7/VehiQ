<template>
    <div class="reservations-container">
      <input type="text" v-model="username" placeholder="Enter username" class="input-field">
      <button @click="getAllReservations" class="btn-get-reservations">Get Reservations</button>
      <div v-if="reservations.length > 0" class="reservation-list">
        <h2 class="reservation-title">Reservations for {{ username }}</h2>
        <ul>
          <li v-for="reservation in reservations" :key="reservation.id" class="reservation-item">
            <div class="reservation-info">
              <div class="info-row">
                <span class="label">Car:</span>
                <span class="value">{{ reservation.car_name }}</span>
              </div>
              <div class="info-row">
                <span class="label">Profile:</span>
                <span class="value">{{ reservation.profile_name }}</span>
              </div>
              <div class="info-row">
                <span class="label">Start Date:</span>
                <span class="value">{{ reservation.start_date }}</span>
              </div>
              <div class="info-row">
                <span class="label">End Date:</span>
                <span class="value">{{ reservation.end_date }}</span>
              </div>
              <div class="info-row">
                <span class="label">Reservation Date:</span>
                <span class="value">{{ reservation.reservation_date }}</span>
              </div>
            </div>
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
        axios.get('http://127.0.0.1:8000/accounts/user/', {
          params: { user: this.username }
        })
          .then(userResponse => {
            const userId = userResponse.data.id;
            axios.get(`http://127.0.0.1:8000/accounts/reservations/`)
            
            .then(reservationResponse => {
              this.reservations = reservationResponse.data.filter(reservation => reservation.profile_name === userId);
            })
            .catch(error => {
              console.error('Error fetching reservations:', error);
            });
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
    background-color: #6a0dad; /* Dark purple */
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
  
  .info-row {
    display: flex;
    margin-bottom: 5px;
  }
  
  .label {
    font-weight: bold;
    margin-right: 5px;
  }
  
  .value {
    flex-grow: 1;
  }
  </style>
  