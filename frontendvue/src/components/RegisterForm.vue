<!-- RegisterForm.vue -->

<template>
  <form @submit.prevent="registerUser">
    <input type="text" v-model="username" placeholder="Username" required>
    <input type="email" v-model="email" placeholder="Email" required>
    <input type="password" v-model="password" placeholder="Password" required>
    <button type="submit">Register</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    async registerUser() {
      try {
        const response = await fetch('http://127.0.0.1:8000/accounts/register/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password
          })
        })
        const data = await response.json()
        if (response.ok) {
          // Registration successful, redirect or show success message
        } else {
          // Registration failed, handle errors
        }
      } catch (error) {
        console.error('Error registering user:', error)
      }
    }
  }
}
</script>
