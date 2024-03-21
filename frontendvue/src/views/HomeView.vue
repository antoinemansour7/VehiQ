<template>
  <div class="home-container">
    <h1 class="animate__animated animate__bounceIn">Welcome to VehiQ</h1>
    <h3>Your Ultimate Destination for Car Rentals</h3>
    <div class="firework left"></div>
    <img class="VehiQLogo animate__animated animate__fadeIn" src="@/assets/VEHIQ_logo.png" alt="VehiQLogo" />
    <div class="firework right"></div>
    <p class="welcome-text">
      At VehiQ, we're dedicated to providing you with an unparalleled car rental experience that combines convenience, reliability, and affordability. Whether you're planning a weekend getaway, a business trip, or an adventurous road trip, we've got the perfect vehicle to suit your needs.
      <br><br>
      With our extensive fleet of well-maintained cars, ranging from sleek sedans to spacious SUVs and everything in between, finding the ideal ride for your journey has never been easier. Plus, our user-friendly booking platform allows you to reserve your vehicle with just a few clicks, ensuring a hassle-free rental process from start to finish.
      <br><br>
      At VehiQ, we prioritize customer satisfaction above all else. Our team of friendly and knowledgeable staff is here to assist you every step of the way, helping you select the right car for your trip and addressing any questions or concerns you may have along the way.
      <br><br>
      Whether you're exploring the open road, navigating city streets, or embarking on a family vacation, VehiQ is your trusted partner in transportation. Experience the freedom of the open road with VehiQ - where every journey begins with convenience, comfort, and confidence.
      <br><br>
      Start your adventure today and discover why VehiQ is the preferred choice for car rentals nationwide. Welcome aboard!
    </p>
  </div>
</template>

<script>
export default {
  setup() {
    // No need to return anything from setup
  }
}
</script>

<style scoped>
.home-container {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.VehiQLogo {
  width: 200px; 
  height: auto;
}

h1, h3, p{
  color: #544e63;
}

.welcome-text {
  font-size: 18px;
  line-height: 1.6;
}

.firework {
  position: absolute;
  width: 300px;
  height: 300px;
  background-image: url('@/assets/fireworks.gif');
  background-size: contain;
  background-repeat: no-repeat;
}

.left {
  top: 100px;
  left: 50px; /* Half of the container width minus half of the fireworks width minus 100px */
}

.right {
  top: 100px;
  right: 50px; /* Half of the container width minus half of the fireworks width minus 100px */
}
</style>
