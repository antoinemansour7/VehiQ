<template>
  <h1>Available Cars</h1>
  <div class="rental-car-list">
    <div v-for="car in cars" :key="car.id" class="rental-car">
      <img :src="car.get_image" alt="Car Image">
      <div class="details">
        <h3>{{ car.make }} {{ car.model }}</h3>
        <p>{{ car.year }}</p>
        <p>{{ car.price }}</p>
      </div>
      <div class="features">
        <img v-if="car.is_electric" src="../assets/lightning.png" class="icon">
        <img v-if="car.is_all_wheel_drive" src="../assets/wheels.png" class="icon">
        <button @click="deleteCar(car.id)">Delete</button>
        <button>Modify</button><!--Create form Modify and link it onclick and Create form Create and link it onclick -->
        <button>Create</button>
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
    }
  }
}
</script>

<style scoped>
h1, h3, p{
  color: #544e63;
}
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
</style>
