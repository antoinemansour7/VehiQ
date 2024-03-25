<template>
    <div class="form-container">
        <form @submit.prevent="handleSubmit">
            <label for="confirmationCode">Confirmation Code:</label>
            <input type="text" id="confirmationCode" v-model="confirmationCode" required>

            <label for="creditCardNumber">Credit Card Number:</label>
            <input type="text" id="creditCardNumber" v-model="creditCardNumber" maxlength="16" required>

            <button type="submit" class="button-looking">Submit</button>
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

                console.log('Filtered Reservations:', filteredReservations);

                if (filteredReservations.length > 0) {
                    alert('Reservation found');
                    console.log('Reservation found:', filteredReservations[0]);
                    this.$router.push({ name: 'UserReport' });
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

<style scoped>
.form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Center vertically */
}

form {
    width: 300px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"] {
    width: calc(100% - 20px); /* Make the input fields shorter */
    padding: 5px;
    margin-bottom: 10px;
}

.button-looking {
    background-color: #ada3b8;
    color: #fff;
    cursor: pointer;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
}

/* Hover effect */
.button-looking:hover {
    background-color: #90839c;
}
</style>
