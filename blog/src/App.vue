<template>
  <HeaderSection msg="VehiQ"/>
  <CarListing/>

</template>

<script>
import HeaderSection from './components/HeaderSection.vue'
import CarListing from './components/CarListing.vue'


export default {
  name: 'App',
  components: {
    HeaderSection,
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
