<template>
  <GMapMap
    :center="{ lat: 45.5017, lng: -73.5673 }" // Center the map around Montreal
    :zoom="12"
    map-type-id="roadmap"
    style="width: 100%; height: 500px"
  >
    <GMapMarker
      v-for="branch in branches"
      :key="branch.id"
      :position="{ lat: branch.location.coordinates[1], lng: branch.location.coordinates[0] }"
      @click="selectBranch(branch)"
    />
  </GMapMap>
</template>

<script>
import axios from 'axios';
export default {
  name: "BranchMap",
  data() {
    return {
      branches: [],
    };
  },
  mounted() {
    this.getBranches();
  },
  methods: {
    getBranches() {
      axios.get('http://localhost:8000/branches/')
        .then(response => {
          console.log('Branches fetched:', response.data);
          this.branches = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the branches:', error);
        });
    },
    selectBranch(branch) {
      // Implement your logic for when a branch is selected
       this.$emit('branch-selected', branch);
  // Or store it in Vuex store
  // this.$store.commit('setSelectedBranch', branch);
  // Or navigate to a branch detail page
  // this.$router.push({ name: 'BranchDetail', params: { id: branch.id } });
      console.log('Branch selected:', branch);
    },
  },
};
</script>
