<template>
    <div class="reservation-container">
      <h1>Available Reservations</h1>
      <div class="rental-car-list">
        <div v-for="(reservation, index) in reservations" :key="index" class="rental-car">
          <div class="details">
            <h3>{{ reservation.car_name }}</h3>
            <p><strong>Start Date:</strong> {{ reservation.start_date }}</p>
            <p><strong>End Date:</strong> {{ reservation.end_date }}</p>
            <p><strong>Reserved By:</strong> {{ reservation.user_name }}</p>
          </div>
          <div class="features">
            <button @click="deleteReservation(reservation.id)">Delete</button>
            <button>Modify</button>
            <!--Report button-->
            <button @click="redirectToCSRReport">
              <span class="icon"><i class="fas fa-flag"></i></span>
            </button>
          </div>
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
        },
        redirectToCSRReport() {
            this.$router.push('/CSRReport');
        }
    }
  }
  </script>
  
  <style scoped>
  .reservation-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
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
    justify-content: space-between;
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
  
  </style>
  