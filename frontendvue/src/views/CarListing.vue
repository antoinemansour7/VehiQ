<template>
  <h1>Available Cars</h1>

  <!--Create new car-->
  <button class="button-looking" @click="openCreateCarForm">Create</button>
  
  <!-- Filter dropdowns -->
  <div class="filter-container">
    <select class="filter-select" v-model="search.make">
      <option value="">Select Make</option>
      <option v-for="make in uniqueMakes" :key="make" :value="make">{{ make }}</option>
    </select>
    <select class="filter-select" v-model="search.model">
      <option value="">Select Model</option>
      <option v-for="model in uniqueModels" :key="model" :value="model">{{ model }}</option>
    </select>
    <select class="filter-select" v-model="search.year">
      <option value="">Select Year</option>
      <option v-for="year in uniqueYears" :key="year" :value="year">{{ year }}</option>
    </select>
    <select class="filter-select" v-model="search.price">
      <option value="">Select Price</option>
      <option value="0-10000">$0 - $10,000</option>
      <option value="10001-20000">$10,001 - $20,000</option>
      <!-- Add more options as needed -->
    </select>
    <select class="filter-select" v-model="search.isElectric">
      <option value="">Electric?</option>
      <option value="true">Yes</option>
      <option value="false">No</option>
    </select>
    <select class="filter-select" v-model="search.isAllWheelDrive">
      <option value="">All-Wheel Drive?</option>
      <option value="true">Yes</option>
      <option value="false">No</option>
    </select>
  </div>


  <div class="rental-car-list">
    <div v-for="car in filteredCars" :key="car.id" class="rental-car">
      <div class="button-container">
        
        <button class="button-looking small-button" @click="deleteCar(car.id)">
          <span class="icon"><i class="fas fa-trash"></i></span>
        </button>
        
        <button class="button-looking small-button">
          <span class="icon"><i class="fas fa-edit"></i></span>
        </button>
        <button class="button-looking small-button" @click="openCreateCarPage(car.id)">
          <span class="icon"><i class="fas fa-calendar"></i></span>
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
      cars: [],
      search: {
        make: '',
        model: '',
        year: '',
        price: '',
        isElectric: '',
        isAllWheelDrive: ''
      }
    };
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
    ,
    openCreateCarPage(id) {
    this.$router.push({ name: 'carPage', params: { id: id} })
    }

  },
  computed: {
    uniqueMakes() {
      return [...new Set(this.cars.map(car => car.make))];
    },
    uniqueModels() {
      return [...new Set(this.cars.map(car => car.model))];
    },
    uniqueYears() {
      return [...new Set(this.cars.map(car => car.year))];
    },
    filteredCars() {
  return this.cars.filter(car => {
    // Check if car make, model, and year match the search criteria
    const makeMatch = car.make.toLowerCase().includes(this.search.make.toLowerCase());
    const modelMatch = car.model.toLowerCase().includes(this.search.model.toLowerCase());
    const yearMatch = car.year.toString().includes(this.search.year);

    // Check if car price falls within the selected price range
    let priceMatch = true;
    if (this.search.price) {
      const [minPrice, maxPrice] = this.search.price.split('-').map(Number);
      priceMatch = car.price >= minPrice && car.price <= maxPrice;
    }

    // Check if car is electric matches the selected filter
    const isElectricMatch = this.search.isElectric === '' || car.is_electric.toString() === this.search.isElectric;

    // Check if car is all-wheel drive matches the selected filter
    const isAllWheelDriveMatch = this.search.isAllWheelDrive === '' || car.is_all_wheel_drive.toString() === this.search.isAllWheelDrive;

    // Return true if all criteria match
    return makeMatch && modelMatch && yearMatch && priceMatch && isElectricMatch && isAllWheelDriveMatch;
  });
}


  }
};
</script>

<style scoped>
.rental-car-list {
    display: flex;
    flex-wrap: wrap;
    padding: 0 20px;
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
  padding: 15px 15px;
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
  bottom: 10px; /* Adjust as needed */
  left: 110px; /* Adjust as needed */
}

.small-button {
  margin: 2px;
  font-size: 10px;
}

/* Additional styles for Bulma icons */
.icon {
  vertical-align: middle; /* Align the icon vertically with button text */
}

.filter-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 5px 30px;
}

.filter-select {
  width: calc(14% - 10px);
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc1d7;
  color: #ada3b8;
}
</style>
