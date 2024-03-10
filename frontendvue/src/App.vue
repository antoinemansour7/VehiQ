<template>
  <div id="wrapper">
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">Home</router-link>
      <router-link to="/about" class="navbar-item">About</router-link>
    </div>
    
  </nav>
  <router-view/>
</div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
