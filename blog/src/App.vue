<template>
  <img alt="VehiQ logo" src="./assets/VEHIQ_logo.png">
  <HelloWorld msg="Welcome to My Vue.js App"/>
  <CarListing/>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import CarListing from './components/CarListing.vue'


export default {
  name: 'App',
  components: {
    HelloWorld,
    CarListing

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
