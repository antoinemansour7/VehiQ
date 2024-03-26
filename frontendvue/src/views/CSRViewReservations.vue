<template>
  <div class="reservation-container">
    <h1>Available Reservations</h1>
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
          <button>Create</button>
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
    redirectToCSRReport() {
      this.$router.push('/CSRReport');
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
