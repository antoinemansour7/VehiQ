<template>
  <SideBar/>
  <div :style="{'margin-left': sidebarWidth}">
    <router-view/>
    <router-view name="login-form"/>
    <router-view name="register-form"/>
  </div>

</template>

<script>
import SideBar from '@/components/sidebar/SideBar'
import { sidebarWidth } from '@/components/sidebar/state'


export default {
  name: 'App',
  components: {
    SideBar

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

h1, h3, p{
  color: #544e63;
}
</style>
