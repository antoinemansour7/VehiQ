<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div>
          <img
            class="VehiQLogo1"
            src="@/assets/VEHIQ_logo.png"
            alt="VehiQLogo"
          />
        </div>
      </span>
      <span v-else>
        <img class="VehiQLogo2" src="@/assets/VEHIQ_logo.png" alt="VehiQLogo" />
        <div>VehiQ</div>
      </span>
    </h1>

    <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>
    <SidebarLink to="/profile" icon="fas fa-user">Profile</SidebarLink>
    <SidebarLink to="/carListing" icon="fas fa-car">Car Listing</SidebarLink>
    <SidebarLink to="/reservations" icon="fas fa-calendar"
      >Reservations</SidebarLink
    >
    <SidebarLink to="/viewReservations" icon="fas fa-list-alt"
      >View Reservations</SidebarLink
    >
    <!-- Branch link-->
    <SidebarLink to="/nearest-branch" icon="fas fa-map-marker-alt"
      >Find Branch</SidebarLink
    >

    <SidebarLink to="/CSRViewReservations" icon="fas fa-list-alt"
      >View Reservations as a CSR</SidebarLink
    >
    <!--can change name to "View Reservations"-->
    <SidebarLink to="/viewUsers" icon="fas fa-users">View Users</SidebarLink>
    <SidebarLink to="/carInspection" icon="fas fa-car-crash"
      >Check Out</SidebarLink
    >
    <!-- Show Sign Up link only if not logged in -->
    <SidebarLink v-if="!isLoggedIn" to="/register" icon="fas fa-user-plus"
      >Sign Up</SidebarLink
    >

    <!-- Show Log In link only if not logged in -->
    <SidebarLink v-if="!isLoggedIn" to="/logIn" icon="fas fa-sign-in-alt"
      >Log In</SidebarLink
    >

    <!-- Show Log Out link only if logged in -->
    <SidebarLink
      v-if="isLoggedIn"
      to="/logOut"
      icon="fas fa-sign-out-alt"
      @click="handleLogout"
      >Log Out</SidebarLink
    >

    <!-- Notification -->
    <div v-if="notification" class="notification">
      {{ notification }}
      <button @click="clearNotification">Close</button>
      <!-- Close button to clear notification -->
    </div>

    <SidebarLink to="/PickUp" icon="fas fa-car-side">Pick Up</SidebarLink>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<script>
import SidebarLink from "./SidebarLink";
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  components: { SidebarLink },
  setup() {
    const store = useStore();

    const isLoggedIn = computed(() => store.state.isLoggedIn);
    const collapsed = computed(() => store.state.collapsed);
    const sidebarWidth = computed(() => "11%");

    const toggleSidebar = () => store.commit("toggleSidebar");
    const handleLogout = () => store.dispatch("logout");
    const notification = computed(() => store.state.notification);

    const clearNotification = () => {
      store.dispatch("clearNotification");
    };

    return {
      isLoggedIn,
      collapsed,
      sidebarWidth,
      toggleSidebar,
      handleLogout,
      notification,
      clearNotification,
    };
  },
};
</script>

<style>
:root {
  --sidebar-bg-color: #ada3b8;
  --sidebar-item-hover: #d6cde0;
  --sidebar-item-active: #91859e;
}

.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.VehiQLogo1 {
  padding-right: 10px;
  width: 40px;
  height: auto;
}

.VehiQLogo2 {
  width: 60px;
  height: auto;
}

.notification {
  position: fixed;
  top: 10px;
  right: 10px;
  background-color: #333;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
}
</style>
