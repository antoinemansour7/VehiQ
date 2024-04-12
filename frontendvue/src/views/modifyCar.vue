<template>
    <div>
      <h1>Edit Car</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="make">Make :</label>
          <input type="text" id="make" v-model="form.make" class="short-input" >
        </div>
        <div class="form-group">
          <label for="model">Model:</label>
          <input type="text" id="model" v-model="form.model" class="short-input">
        </div>
        <div class="form-group">
          <label for="year">Year:</label>
          <input type="number" id="year" v-model.number="form.year" class="short-input">
        </div>
        <div class="form-group">
          <label for="price">Price:</label>
          <input type="number" id="price" v-model.number="form.price" class="short-input">
        </div>
        <div class="form-group">
          <label for="image">Image:</label>
          <input type="file" id="image" accept="image/*" @change="handleImageChange" class="short-input">
        </div>
        <div class="form-group">
          <label for="isElectric">Electric?</label>
          <input type="checkbox" id="isElectric" v-model="form.is_electric">
        </div>
        <div class="form-group">
          <label for="isAllWheelDrive">All-Wheel Drive?</label>
          <input type="checkbox" id="isAllWheelDrive" v-model="form.is_all_wheel_drive">
        </div>
        <button type="submit" class="button-looking">Save</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        form: {
          id: null,
          make: '',
          model: '',
          year: null,
          price: null,
          get_image: '',
          is_electric: false,
          is_all_wheel_drive: false
        }
      };
    },
    mounted() {
      const carId = this.$route.query.id;
      const car = this.$route.query.car;
    },
    methods: {
      async submitForm() {
        const carId = this.$route.params.id;
        try {
          await axios.patch(`http://127.0.0.1:8000/vehicles/cars/${carId}/`, this.form);
          alert('Car updated successfully');
        } catch (error) {
          console.error('Error updating car:', error);
          alert('Error updating car. Please try again.');
        }
      },
      handleImageChange(event) {
        const file = event.target.files[0];

      }
    }
  };
  </script>
  
  <style>
  .short-input {
    width: 150px; 
  }
  
  </style>
  