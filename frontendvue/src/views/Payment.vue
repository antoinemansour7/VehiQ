<template>
    <div class="payment-container">
      <h1>Payment Details</h1>
      <form @submit.prevent="processPayment" class="payment-form">
        <div class="form-group">
          <label for="cardNumber" class="left-label">Card Number:</label>
          <input type="text" id="cardNumber" v-model="cardNumber" placeholder="Enter card number" required>
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
      <div v-if="paymentStatus">
        <p>{{ paymentStatus }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cardNumber: '',
        expirationDate: '',
        cvv: '',
        paymentStatus: ''
      };
    },
    methods: {
      processPayment() {
        // Simulate payment processing
        this.paymentStatus = 'Processing payment...';
        setTimeout(() => {
          // After 2 seconds, simulate successful payment
          this.paymentStatus = 'Payment successful!';
          // You can add further logic here like submitting the form data to a backend server
        }, 2000);
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
  