<template>
    <h1>Available Reservations</h1>
    <div class="rental-car-list">
      <div v-for="(reservation, index) in reservations" :key="index" class="rental-car">
        <div class="details">
          <h3>{{ reservation.car_name }}</h3>
          <p>Start Date: {{ reservation.start_date }}</p>
          <p>End Date: {{ reservation.end_date }}</p>
          <p>Reserved By: {{ reservation.user_name }}</p>
        </div>
        <div class="features">
          <button @click="deleteReservation(reservation.id)">Delete</button>
          <button>Modify</button><!--Create form Modify and link it onclick and Create form Create and link it onclick -->
          <button>Create</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'HomeView',
    data() {
      return {
        reservations: []
      }
    },
    mounted() {
      this.getReservations()
    },
    methods: {
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
    }
  
  </script>
  
  <style scoped>
  .rental-car-list {
      display: flex;
      flex-wrap: wrap;
  }
  .rental-car {
      margin: 10px;
      padding: 10px;
      border: 1px solid black;
      border-radius: 5px;
      width: 300px;
      position: relative;
  }
  .details p:last-child {
      position: absolute;
      margin-top: 10px;
      bottom: 5px;
      right: 20px;
      font: bold 20px Arial, sans-serif;
  }
  .features {
      display: flex;
      align-items: flex-end;
  }
  </style>
  