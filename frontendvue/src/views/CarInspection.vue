<template>
    <div class="car-inspection-form">
        <h2>Car Inspection Form</h2>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="carMake">Car Make:</label>
                <input type="text" id="carMake" v-model="carMake" required>
            </div>
            <div class="form-group">
                <label for="carModel">Car Model:</label>
                <input type="text" id="carModel" v-model="carModel" required>
            </div>
            <div class="form-group">
                <label>Damage Description:</label>
                <div class="checkbox-group">
                    <label>
                        <input type="checkbox" v-model="damageDescriptions.wheelsPressure">
                        Wheels Pressure Okay
                    </label>
                    <label>
                        <input type="checkbox" v-model="damageDescriptions.ACWorking">
                        AC Working
                    </label>
                    <label>
                        <input type="checkbox" v-model="damageDescriptions.wheelWorking">
                        Wheel Working
                    </label>
                    <!-- Add more checkboxes for other damages -->
                </div>
            </div>
            <div class="form-group">
                <label for="damagePhotos">Damage Photos:</label>
                <input type="file" id="damagePhotos" accept="image/*">
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            carMake: '',
            carModel: '',
            damageDescriptions: {
                wheelsPressure: false,
                ACWorking: false,
                wheelWorking: false,
                // Add more damage descriptions here
            },
            damagePhotos: []
        };
    },
    methods: {
        submitForm() {
            // Handle form submission logic here
            // You can access the form data using this.carMake, this.carModel, this.damageDescriptions, and this.damagePhotos
            console.log("Form submitted with data:", this.carMake, this.carModel, this.damageDescriptions, this.damagePhotos);
        }
    }
};
</script>

<style scoped>
.car-inspection-form {
    max-width: 400px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    font-weight: bold;
}

input[type="text"],
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.checkbox-group label {
    display: block;
    margin-bottom: 10px;
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
</style>
