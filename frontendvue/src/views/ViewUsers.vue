<template>
    <div>
      <h1>Available Users</h1>
      <div class="rental-car-list">
        <div v-for="(user, index) in users" :key="index" class="rental-car">
          <div class="details">
            <h3>{{ user.user }}</h3>
            <p>{{ user.email }}</p>
            <p>{{ user.first_name }}</p>
            <p v-if="user.is_staff">Admin</p>
          </div>
          <div class="features">
            <button @click="deleteUser(user.id)">Delete</button>
            <button>Modify</button><!--Create form Modify and link it onclick and Create form Create and link it onclick -->
            <button>Create</button>
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
        users: []
      }
    },
    mounted() {
      this.getUsers()
    },
    methods: {
      getUsers() {
        axios.get('http://127.0.0.1:8000/accounts/user/')
          .then(response => {
            this.users = response.data
          })
          .catch(error => {
            console.error('Error in getUsers:', error)
          })
      },
      deleteUser(id) {
        console.log('Deleting user with ID:', id)
        axios.delete(`http://127.0.0.1:8000/accounts/user/${id}/`)
          .then(() => {
            this.users = this.users.filter(user => user.id !== id)
          })
          .catch(error => {
            console.error('Error deleting user:', error)
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
  </style>
  