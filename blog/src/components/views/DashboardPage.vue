<template>
    <h1>Dashboard</h1>
  </template>
  
  <script>
  import { collapsed, toggleSidebar } from '@/components/sidebar/state'
  
  export default {
    setup() {
      return { collapsed, toggleSidebar }
    }
  }
  </script>