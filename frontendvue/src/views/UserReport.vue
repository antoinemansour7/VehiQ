<template>
    <div>
      <h1>Report Issue</h1>
      <form @submit.prevent="submitForm" class="form">
        <div class="form-group">
          <label for="title" class="label-left">Title:</label>
          <input type="text" id="title" v-model="form.title" required>
        </div>
        <div class="form-group">
          <label for="severity" class="label-left">Severity:</label>
          <select id="severity" v-model="form.severity">
            <option value="critical">Critical</option>
            <option value="non-critical">Non-critical</option>
          </select>
        </div>
        <div class="form-group">
          <label for="text" class="label-left">Description:</label>
          <textarea id="text" v-model="form.text" rows="5" required></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          title: '',
          text: '',
          severity: 'critical'
        }
      };
    },
    methods: {
      submitForm() {
        console.log('Form submitted with data:', this.form);
        this.resetForm();
      },
      resetForm() {
        // Reset form fields after submission
        this.form.title = '';
        this.form.text = '';
        this.form.severity = 'critical';
      }
    }
  };
  </script>
  
  <style scoped>
  .form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 5px;
    background-color: #f1eff3;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .label-left {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  textarea,
  select,
  button {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
  }
  
  button {
    background-color: #ada3b8;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #90839c;
  }
  </style>
  