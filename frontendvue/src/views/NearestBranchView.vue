<template>
  <div class="nearest-branch-view">
    <h1>Find a Branch Near You</h1>
    <div class="branch-search-form">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Enter address or postal code"
      />
      <button @click="searchNearestBranch">Search</button>
    </div>
    <BranchMap :singleBranch="nearestBranch" />
    <div v-if="nearestBranch" class="branch-details">
      <h2>Nearest Branch:</h2>
      <p>{{ nearestBranch.name }}</p>
      <p>{{ nearestBranch.address }}</p>
      <!-- Add other details here -->
    </div>
    <div v-else>
      <p>Enter an address or postal code to find the nearest branch.</p>
    </div>
  </div>
</template>

<script>
import BranchMap from "@/components/map/BranchMap.vue";
import axios from "axios";

export default {
  components: { BranchMap },
  data() {
    return {
      searchQuery: "",
      nearestBranch: null,
    };
  },
  methods: {
    searchNearestBranch() {
      const address = this.searchQuery;
      // Make sure to replace `YOUR_API_KEY` with your actual Google Maps Geocoding API key
      axios
        .get(
          `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(
            address
          )}&key=AIzaSyC0reBBmM59hL07OU_NNWYY1DB1fWrujdI`
        )
        .then((response) => {
          if (
            response.data &&
            response.data.results &&
            response.data.results.length > 0
          ) {
            const location = response.data.results[0].geometry.location;
            console.log("Geocode success:", location); // Debugging
            return axios.get(
              `http://localhost:8000/branches/nearest/?lat=${location.lat}&lng=${location.lng}`
            );
          } else {
            throw new Error("Geocoding failed");
          }
        })
        .then((response) => {
          console.log("Nearest branch response:", response.data); // Debugging
          this.nearestBranch = response.data;
        })
        .catch((error) => {
          console.error("Error while fetching nearest branch:", error);
        });
    },
  },
};
</script>

<style scoped>
.nearest-branch-view {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.branch-search-form {
  margin-bottom: 20px;
}

.branch-details {
  margin-top: 20px;
}

/* Additional styles if needed */
</style>
