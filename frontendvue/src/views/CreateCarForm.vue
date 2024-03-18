<template>
  <div class="signup-container">
    <h2>Add a New Car</h2>
    <form @submit.prevent="submitForm" class="signup-form">
      <div class="form-group">
        <label for="make">Make:</label>
        <input type="text" id="make" v-model="car.make" required>
      </div>
      <div class="form-group">
        <label for="model">Model:</label>
        <input type="text" id="model" v-model="car.model" required>
      </div>
      <div class="form-group">
        <label for="year">Year:</label>
        <input type="number" id="year" v-model="car.year" required>
      </div>
      <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" id="price" v-model="car.price" required>
      </div>
      <div class="form-group">
        <label for="image">Image:</label>
        <input type="file" id="image" accept="image/*" @change="handleImageChange">
      </div>
      <div class="form-group">
        <label>Options:</label>
        <div class="checkbox-group">
          <input type="checkbox" id="electric" v-model="car.electric">
          <label for="electric">Electric</label>
          <input type="checkbox" id="allWheelDrive" v-model="car.allWheelDrive">
          <label for="allWheelDrive">All Wheel Drive</label>
        </div>
      </div>
      <div id="submit-botton">
        <button type="submit" >Submit</button>
      </div>
      
    </form>
  </div>
</template>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
  background-color: #eae7ed;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  color: #544e63;
}

input[type="text"],
input[type="number"],
input[type="file"],
button {
  padding: 8px;
  border: 1px solid #ada3b8;
  border-radius: 5px;
}

button {
  background-color: #ada3b8;
  color: #fff;
  cursor: pointer;
  margin-top: 10px; /* Added margin to separate the buttons */
}

button:hover {
  background-color: #90839c;
}

.checkbox-group {
  display: flex;
  align-items: center;
}

.checkbox-group input[type="checkbox"] {
  margin-right: 5px;
}

.checkbox-group label {
  margin-right: 15px;
}
</style>

<style>
.container {
  width: 50%;
  margin: 0 auto;
}

.car-form {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: inline-block;
  width: 100px;
  text-align: left;
  font-weight: bold;
}

input[type="text"],
input[type="number"],
input[type="file"],
button {
  width: calc(100% - 110px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  margin-top: 5px;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.checkbox-group {
  white-space: nowrap;
}

.checkbox-group input[type="checkbox"] {
  display: inline-block;
  margin-right: 5px;
}

.checkbox-group label {
  display: inline-block;
  margin-right: 15px;
}

.all-wheel-drive-label {
  white-space: nowrap;
}

.submit-button {
  align-items: center;
}
</style>




<script>
export default {
  data() {
    return {
      car: {
        make: '',
        model: '',
        year: null,
        price: null,
        electric: false,
        allWheelDrive: false,
        image: null
      }
    };
  },
  methods: {
    handleImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.car.image = file;
      }
    },
    submitForm() {
      // You can handle form submission logic here
      console.log(this.car);
    }
  }
};
</script>
