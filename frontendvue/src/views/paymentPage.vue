<template>
    <div class="payment-container">
      <h1>Payment Information</h1>
      <p>this is price : {{ this.$route.query.price }}</p>
      <form @submit.prevent="submitPayment" class="payment-form">
        <div class="form-group">
          <label for="cardNumber" class="left-label">Card Number (16 digits):</label>
          <input type="text" id="cardNumber" v-model="cardNumber" required maxlength="16" pattern="[0-9]{16}">
        </div>
        <div class="form-group">
          <label for="expirationDate" class="left-label">Expiration Date:</label>
          <input type="text" id="expirationDate" v-model="expirationDate" placeholder="MM/YY" required>
        </div>
        <div class="form-group">
          <label for="cvv" class="left-label">CVV:</label>
          <input type="text" id="cvv" v-model="cvv" placeholder="Enter CVV" required>
        </div>
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
        expirationDate: '',
        cvv: '',
        confirmationNumber: '',
        pickupLocation: '',
        reservation: {}
      };
    },
    methods: {
      async submitPayment() {
        try {
          alert(this.$route.query.price);
          // Fetch reservation details
          const reservationId = this.$route.query.id;
          const reservationResponse = await axios.get(`http://127.0.0.1:8000/accounts/reservations/${reservationId}/`);
          const reservationData = reservationResponse.data;
  
          // Extract necessary data
          const { car, user, end_date, price, pickup_location, dropoff_location } = reservationData;
  
          // Construct the payload for the PUT request
          const payload = {
            card_number: this.cardNumber,
            confirmation_number: (Math.floor(Math.random() * 9000000000) + 1000000000).toString(),
            car,
            user,
            end_date,
            price,
            pickup_location,
            dropoff_location,
            deposit : 500
          };
  
          // Perform the PUT request to update the reservation
          const response = await axios.put(`http://127.0.0.1:8000/accounts/reservations/${reservationId}/`, payload);
          console.log('Reservation updated successfully:', response.data);
  
          // Update confirmation number after successful submission
          this.confirmationNumber = payload.confirmation_number;
  
          setTimeout(() => {
        this.$router.push({ name: 'ReservationPage', params: { reservationId: response.data.id } });
      }, 30000); // 30 seconds delay (30,000 milliseconds)
        } catch (error) {
          console.error('Error updating reservation:', error);
        }
      }
    }
  };
  </script>


  <style scoped>
  .payment-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 5px;
    background-color: #f1eff3;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .payment-form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .form-group {
    margin-bottom: 15px;
    display: flex;
    align-items: center;
  }
  
  .left-label {
    width: 120px;
    margin-right: 10px;
    font-weight: bold;
    color: #544e63;
  }
  
  input[type="text"],
  button {
    padding: 8px;
    border: 1px solid #ada3b8;
    border-radius: 5px;
  }
  
  button {
    background-color: #ada3b8;
    color: #fff;
    cursor: pointer;
    margin-top: 10px;
  }
  
  button:hover {
    background-color: #90839c;
  }
  
  </style>
  