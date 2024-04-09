<template>
  <div ref="mapContainer" class="map-container">
    <GMapMap
      :center="mapCenter"
      :zoom="10"
      map-type-id="roadmap"
      style="width: 100%; height: 500px"
    >
      <GMapMarker
        v-for="branch in branches"
        :key="branch.id"
        :position="getLatLng(branch)"
        @click="selectBranch(branch)"
      />
      <GMapMarker
        v-if="singleBranch"
        :position="getLatLng(singleBranch)"
        :clickable="false"
        icon="http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
      />
    </GMapMap>
  </div>
</template>

<script>
import axios from "axios";
import { ref, watch, onMounted } from "vue";
import { GMapMap, GMapMarker } from "@fawmi/vue-google-maps";

export default {
  name: "BranchMap",
  props: {
    branches: Array,
    singleBranch: Object,
  },
  setup(props) {
    const gmap = ref(null);
    const mapCenter = ref({ lat: 45.5017, lng: -73.5673 });

    const getLatLng = (branch) => {
      console.log(branch); // Debugging to inspect the structure of branch object
      if (branch.location && branch.location.coordinates) {
        return {
          lat: branch.location.coordinates[1],
          lng: branch.location.coordinates[0],
        };
      } else {
        console.error("Unexpected branch structure:", branch);
        return { lat: 0, lng: 0 }; // Return a default or handle the error appropriately
      }
    };

    watch(
      () => props.singleBranch,
      (newBranch, oldBranch) => {
        if (newBranch && gmap.value) {
          mapCenter.value = getLatLng(newBranch);
          gmap.value.panTo(mapCenter.value);
        }
      }
    );

    onMounted(() => {
      if (props.singleBranch) {
        mapCenter.value = getLatLng(props.singleBranch);
      }
    });

    return { gmap, mapCenter, getLatLng };
  },

  methods: {
    selectBranch(branch) {
      this.$emit("branch-selected", branch);
    },
  },
};
</script>

<style scoped>
.map-container {
  height: 500px;
}
</style>
