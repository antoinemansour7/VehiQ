<template>
  <div>
    <h1>Reservation Details</h1>
    <div v-if="reservation">
      <p><strong>Reservation ID:</strong> {{ reservation.id }}</p>
      <p><strong>Car:</strong> {{ reservation.car }}</p>
      <p><strong>User:</strong> {{ reservation.user }}</p>
      <p><strong>Start Date:</strong> {{ reservation.start_date }}</p>
      <p><strong>End Date:</strong> {{ reservation.end_date }}</p>
      <p><strong>Reservation Date:</strong> {{ reservation.reservation_date }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reservation: null
    };
  },
  mounted() {
    this.fetchReservation();
  },
  methods: {
    fetchReservation() {
      const reservationId = this.$route.params.reservationId;
      axios.get(`http://127.0.0.1:8000/accounts/reservations/${reservationId}`)
        .then(response => {
          this.reservation = response.data;
        })
        .catch(error => {
          console.error('Error fetching reservation:', error);
        });
    }
  }
};
</script>
