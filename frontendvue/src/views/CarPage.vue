<template>
    <div>
      <h1>Car Details</h1>
      <div v-if="car">
        <img id="car-image" :src="car.get_image" alt="Car Image">
        <h2>{{ car.make }} {{ car.model }}</h2>
        <p>Year: {{ car.year }}</p>
        <p>Price: {{ car.price }}</p>
      </div>
      <h2>Create Reservation</h2>
      <form @submit.prevent="createReservation">
        <label for="startDate">Start Date:</label>
        <input type="datetime-local" id="startDate" v-model="startDate" required>
        <label for="endDate">End Date:</label>
        <input type="datetime-local" id="endDate" v-model="endDate" required>
        <label for="reservationDate">Reservation Date:</label>
        <input type="datetime-local" id="reservationDate" v-model="reservationDate" required>
        <label for="pickupLocation">Pickup Location:</label>
        <select id="pickupLocation" v-model="pickupLocation" required>
          <option value="option1">Option 1</option>
          <option value="option2">Option 2</option>
          <option value="option3">Option 3</option>
          <option value="option4">Option 4</option>
        </select>
        <label for="dropoffLocation">Drop-off Location:</label>
        <select id="dropoffLocation" v-model="dropoffLocation" required>
          <option value="option1">Option 1</option>
          <option value="option2">Option 2</option>
          <option value="option3">Option 3</option>
          <option value="option4">Option 4</option>
        </select>

        <p>According to the chosen dates, the rental will cost you: {{ calculateRentalCost() }} </p>
        
        <button type="submit">Continue to payement</button>
      </form>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        car: null,
        startDate: '',
        endDate: '',
        reservationDate: '',
        pickuplocation: '',
        dropofflocation: ''
      };
    },
    mounted() {
      this.fetchCarDetails();
    },
    methods: {
      fetchCarDetails() {
        const carId = this.$route.params.id;
  
        axios.get(`http://127.0.0.1:8000/vehicles/cars/${carId}`)
          .then(response => {
            this.car = response.data;
          })
          .catch(error => {
            console.error('Error fetching car details:', error);
          });
      },
      calculateRentalCost() {
      if (!this.car || !this.startDate || !this.endDate) return '';

      const start = new Date(this.startDate);
      const end = new Date(this.endDate);
      const days = Math.ceil((end - start) / (1000 * 60 * 60 * 24)); // Calculate number of days
      
      return (this.car.price * days).toFixed(2); // Multiply price by number of days
    },
      createReservation() {
        const reservation = {
          car: this.$route.params.id,
          user: 1, // Hardcoded user ID for now
          start_date: new Date(this.startDate).toISOString(),
          end_date: new Date(this.endDate).toISOString(),
          reservation_date: new Date(this.reservationDate).toISOString(),
          pickup_location: this.pickupLocation,
          dropoff_location: this.dropoffLocation,
          price: this.calculateRentalCost()
        };
  
        axios.post('http://127.0.0.1:8000/accounts/reservations/', reservation)
          .then(response => {
            alert('Reservation created successfully');
            this.$router.push({ name: 'ReservationPage', params: { reservationId: response.data.id } });
          })
          .catch(error => {
            alert('Error creating reservation');
          });
      }
    }
  };
  </script>

  <style>

  #car-image {
    width: 200px;

  }
  </style>
  
  
  
  