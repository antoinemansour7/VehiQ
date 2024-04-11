<template>
  <SideBar/>
  <div :style="{'margin-left': sidebarWidth}">
    <router-view/>
    <router-view name="login-form"/>
    <router-view name="register-form"/>
  </div>
  <button class="chatbot-toggle-button" @click="toggleChatbot"><i class="fas fa-robot"></i></button>
  <Chatbot :isOpen="isChatbotOpen" />

</template>

<script>
import SideBar from '@/components/sidebar/SideBar'
import { sidebarWidth } from '@/components/sidebar/state'
import Chatbot from '@/views/Chatbot'


export default {
  name: 'App',
  components: {
    SideBar,
    Chatbot

  },
  data() {
    return {
      isChatbotOpen: false
    };
  },
  methods: {
    toggleChatbot() {
      this.isChatbotOpen = !this.isChatbotOpen;
    }
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

.chatbot-toggle-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 40px;
  height: 40px;
  border-radius: 50%; /* Make it circular */
  background-color: #ada3b8;
  color: #fff;
  font-size: 24px;
  border: none;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.chatbot-toggle-button:hover {
  background-color: #90839c; 
}
</style>
