<template>
    <div class="payment-container">
      <h1>Payment Information</h1>
      <form @submit.prevent="submitPayment">
        <label for="cardNumber">Card Number (16 digits):</label>
        <input type="text" id="cardNumber" v-model="cardNumber" required maxlength="16" pattern="[0-9]{16}">
        <button type="submit">Submit Payment</button>
      </form>
  
      <div v-if="confirmationNumber" class="confirmation">
        <h2>Booking Confirmation</h2>
        <p>Your booking has been confirmed. Confirmation Number: {{ confirmationNumber }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        cardNumber: '',
        confirmationNumber: '',
        pickupLocation: ''
      };

    },
    methods: {
      async submitPayment() {
        try {
          // Fetch reservation details
          const reservationId = this.$route.query.id;
          const reservationResponse = await axios.get(`http://127.0.0.1:8000/accounts/reservations/${reservationId}/`);
          const reservationData = reservationResponse.data;
  
          // Extract necessary data
          const { car, user, end_date } = reservationData;
  
          // Construct the payload for the PUT request
          const payload = {
            card_number: this.cardNumber,
            confirmation_number: (Math.floor(Math.random() * 9000000000) + 1000000000).toString(),
            car,
            user,
            end_date
          };
  
          // Perform the PUT request to update the reservation
          const response = await axios.put(`http://127.0.0.1:8000/accounts/reservations/${reservationId}/`, payload);
          console.log('Reservation updated successfully:', response.data);
  
          // Update confirmation number after successful submission
          this.confirmationNumber = payload.confirmation_number;
        } catch (error) {
          console.error('Error updating reservation:', error);
        }
      }
    }
  };
  </script>
  