<template>
  <p>Available Cars</p>
    <div class="rental-car-list">
        <div v-for="car in cars" :key="car.id" class="rental-car">
            <img :src="car.get_image" alt="Car Image">
            <div class="details">
                <h3>{{ car.make }} {{ car.model }}</h3>
                <p>{{ car.year }}</p>
                <p>{{ car.price }}</p>
            </div>
            <div class="features">
                <img v-if="car.isElectric" src='../assets/lightning.png' class="icon">
                <img v-if="car.isAllWheelDrive" src='../assets/wheels.png' class="icon">
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
  components: {
  },
  mounted(){
    this.getCars()
  },
  methods:
  {
    getCars(){
      axios
        .get('http://127.0.0.1:8000/api/v1/browse/')
        .then(response => {
          this.cars = response.data
      })
      .catch(error => {
          console.log(error)
      })
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
    position: absolute  ;
    margin-top: 10px;
    bottom: 5px;
    right: 20px;
    font: bold 20px Arial, sans-serif;

    
}
.features{
    display: flex;
    align-items: flex-end;
}
.features img{
    height: 50px;
    width:50px ;
    margin-right: 10px;
}
</style>
