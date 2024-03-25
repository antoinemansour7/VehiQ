<template>
    <div>
        <form @submit.prevent="handleSubmit">
            <label for="confirmationCode">Confirmation Code:</label>
            <input type="text" id="confirmationCode" v-model="confirmationCode" required>

            <label for="creditCardNumber">Credit Card Number:</label>
            <input type="text" id="creditCardNumber" v-model="creditCardNumber" maxlength="16" required>

            <button type="submit">Submited</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            confirmationCode: '',
            creditCardNumber: ''
        };
    },
    methods: {
    async handleSubmit() {
        try {
            

            const response = await axios.get('http://127.0.0.1:8000/accounts/reservations/');
            

            const reservations = response.data;

            const filteredReservations = reservations.filter(reservation => {
    const cardNumber = reservation.card_number.toString().trim();
    const confirmationCode = reservation.confirmation_number.toString().trim();

    return confirmationCode === this.confirmationCode.trim() &&
           cardNumber === this.creditCardNumber.trim();
});


            console.log('Filtered Reservations:', filteredReservations); // Add this line

            if (filteredReservations.length > 0) {
                alert('Reservation found');
                console.log('Reservation found:', filteredReservations[0]);
            } else {
                alert('No matching reservation found');
                console.log('No matching reservation found');
            }
        } catch (error) {
            console.error('Error retrieving reservations:', error);
        }
    }
}

};
</script>
