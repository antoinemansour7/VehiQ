<template>
  <form @submit.prevent="loginUser">
    <input type="email" v-model="email" placeholder="Email" required>
    <input type="password" v-model="password" placeholder="Password" required>
    <button type="submit">Log In</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async loginUser() {
      try {
        const response = await fetch('http://127.0.0.1:8000/accounts/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        });
        const data = await response.json();
        if (response.ok && data.success) {
          // Dispatch the login action to update the login state in Vuex
          this.$store.dispatch('login', data.user);
        } else {
          // Login failed, handle errors
        }
      } catch (error) {
        console.error('Error logging in user:', error.message);
      }
    }
  }
}
</script>
