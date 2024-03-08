<template>
    <h1>Profile</h1>
  </template>
  
  <script>
  import { collapsed, toggleSidebar } from '@/components/sidebar/state'
  
  export default {
    setup() {
      return { collapsed, toggleSidebar }
    }
  }
  </script>