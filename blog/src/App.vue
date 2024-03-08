<template>
  <SideBar/>
  <div :style="{'margin-left': sidebarWidth}">
    <router-view/>
  </div>
  <CarListing/>

</template>

<script>
import SideBar from '@/components/sidebar/SideBar'
import { sidebarWidth } from '@/components/sidebar/state'
import CarListing from './components/CarListing.vue'


export default {
  name: 'App',
  components: {
    SideBar,
    CarListing

  },
  setup(){
    return {sidebarWidth}
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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
