<template>
  <h1>Available Cars</h1>
  <button class="button-looking" @click="openCreateCarForm">Create</button>
  <div class="rental-car-list">
    <div v-for="car in cars" :key="car.id" class="rental-car">
      <div class="button-container">
        <!-- Delete button -->
        <button class="button-looking small-button" @click="deleteCar(car.id)">
          <span class="icon"><i class="fas fa-trash"></i></span>
        </button>
        <!-- Edit button -->
        <button class="button-looking small-button">
          <span class="icon"><i class="fas fa-edit"></i></span>
        </button>
      </div>
      <img :src="car.get_image" alt="Car Image">
      <div class="details">
        <h3>{{ car.make }} {{ car.model }}</h3>
        <p>{{ car.year }}</p>
        <p>{{ car.price }}</p>
      </div>
      <div class="features">
        <img v-if="car.is_electric" src="../assets/lightning.png" class="icon">
        <img v-if="car.is_all_wheel_drive" src="../assets/wheels.png" class="icon">
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
      cars: []
    }
  },
  mounted() {
    this.getCars()
  },
  methods: {
    getCars() {
      axios.get('http://127.0.0.1:8000/vehicles/cars/')
        .then(response => {
          this.cars = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteCar(id) {
      axios.delete(`http://127.0.0.1:8000/vehicles/cars/${id}/`)
        .then(() => {
          // Remove the deleted car from the local list
          this.cars = this.cars.filter(car => car.id !== id)
          alert('Car deleted successfully')
        })
        .catch(error => {
          console.log(error)
        })
    },
    openCreateCarForm() {
      this.$router.push('/createCar')
    }
  }
}
</script>

<style scoped>
.rental-car-list {
    display: flex;
    flex-wrap: wrap;
}
.rental-car {
    margin: 10px;
    padding: 10px;
    border: 1px solid black;
    border-radius: 5px;
    width: 300px;
    position: relative;
}
.rental-car img{
    width:100%;
    height: auto;
    border-radius: 5px;
}
.details p:last-child {
    position: absolute;
    margin-top: 10px;
    margin-bottom: 10px;
    bottom: 5px;
    right: 20px;
    font: bold 20px Arial, sans-serif;
}
.features {
    display: flex;
    align-items: flex-end;
    
}
.features img {
    height: 50px;
    width: 50px;
    margin-right: 10px;
}
.button-looking {
  background-color: #ada3b8; 
  color: #fff; 
  cursor: pointer;
  padding: 15px 32px;
  border: none;
  font-size: 16px;
  border-radius: 5px;
  margin: 4px 2px;
  transition: background-color 0.3s;
}

/* Hover effect */
.button-looking:hover {
  background-color: #90839c; 
}

.button-container {
  display: flex;
  position: absolute;
  top: 10px; /* Adjust as needed */
  right: 10px; /* Adjust as needed */
}

.small-button {
  margin: 2px;
  font-size: 10px;
}

/* Additional styles for Bulma icons */
.icon {
  vertical-align: middle; /* Align the icon vertically with button text */
}
</style>
