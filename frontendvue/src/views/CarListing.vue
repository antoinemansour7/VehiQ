<template>
  <div>
    <h1 class="title">Available Cars</h1>

    <!-- Dropdowns for filtering -->
    <div class="filter-dropdowns">
      <!-- Make -->
      <select v-model="selectedMake" @change="filterCars" class="select-box">
        <option value="">Select Make</option>
        <option v-for="make in uniqueMakes" :key="make" :value="make">{{ make }}</option>
      </select>

      <!-- Price Range -->
      <select v-model="selectedPriceRange" @change="filterCars" class="select-box">
        <option value="">Select Price Range</option>
        <option value="0-10000">$0 - $10,000</option>
        <option value="10001-20000">$10,001 - $20,000</option>
        <!-- Add more options as needed -->
      </select>

      <!-- Mileage -->
      <select v-model="selectedMileage" @change="filterCars" class="select-box">
        <option value="">Select Mileage</option>
        <option value="0-5000">0 - 5,000 miles</option>
        <option value="5001-10000">5,001 - 10,000 miles</option>
        <!-- Add more options as needed -->
      </select>

      <!-- Fuel Type -->
      <select v-model="selectedFuelType" @change="filterCars" class="select-box">
        <option value="">Select Fuel Type</option>
        <option value="hybrid">Hybrid</option>
        <option value="electric">Electric</option>
        <option value="gas">Gas</option>
      </select>
    </div>

    <!-- Car list -->
    <div class="rental-car-list">
      <div v-for="car in filteredCars" :key="car.id" class="rental-car">
        <img :src="car.get_image" alt="Car Image">
        <div class="details">
          <h3>{{ car.make }} {{ car.model }}</h3>
          <p>{{ car.year }}</p>
          <p>{{ car.price }}</p>
        </div>
        <div class="features">
          <img v-if="car.is_electric" src='../assets/lightning.png' class="icon">
          <img v-if="car.is_all_wheel_drive" src='../assets/wheels.png' class="icon">
        </div>
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
      selectedMake: '',
      selectedPriceRange: '',
      selectedMileage: '',
      selectedFuelType: ''
    }
  },
  computed: {
    uniqueMakes() {
      return [...new Set(this.cars.map(car => car.make))];
    },
    filteredCars() {
      let filtered = this.cars;

      // Filter by selected make
      if (this.selectedMake) {
        filtered = filtered.filter(car => car.make === this.selectedMake);
      }

      // Filter by selected price range
      if (this.selectedPriceRange) {
        const [min, max] = this.selectedPriceRange.split('-').map(Number);
        filtered = filtered.filter(car => car.price >= min && car.price <= max);
      }

      // Filter by selected mileage
      if (this.selectedMileage) {
        const [minMileage, maxMileage] = this.selectedMileage.split('-').map(Number);
        // Assuming mileage is a property of the car object
        filtered = filtered.filter(car => car.mileage >= minMileage && car.mileage <= maxMileage);
      }

      // Filter by selected fuel type
      if (this.selectedFuelType) {
        filtered = filtered.filter(car => car.fuelType === this.selectedFuelType);
      }

      return filtered;
    }
  },
  mounted() {
    this.getCars();
  },
  methods: {
    getCars() {
      axios
        .get('http://127.0.0.1:8000/api/v1/browse/')
        .then(response => {
          this.cars = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterCars() {
      // Triggered when any filter changes
      // No need to do anything here as computed property 'filteredCars' handles the filtering
    }
  }
}
</script>

<style scoped>
.title {
  color: #ada3b8;
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}

.filter-dropdowns {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.select-box {
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
  background-color: white;
  color: #ada3b8;
}

.rental-car-list {
  display: flex;
  flex-wrap: wrap;
}

.rental-car {
  margin: 10px;
  padding: 10px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
  width: 300px;
  position: relative;
}
.rental-car img{
    width:100%;
    height: auto;
    border-radius: 5px;
}

.details h3 {
  color: #ada3b8;
}

.features {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.feature {
  padding: 5px 10px;
  border: 1px solid #ada3b8;
  border-radius: 20px;
  margin-right: 5px;
  color: #ada3b8;
  font-size: 14px;
}
.features img{
    height: 50px;
    width:50px ;
    margin-right: 10px;
}
</style>

