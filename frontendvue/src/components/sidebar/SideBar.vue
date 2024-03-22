<script>
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'

export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div><img class="VehiQLogo1" src="@/assets/VEHIQ_logo.png" alt="VehiQLogo" /></div>
      </span>
      <span v-else>
        <img class="VehiQLogo2" src="@/assets/VEHIQ_logo.png" alt="VehiQLogo" />
        <div>VehiQ</div>
      </span>
    </h1>

    <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>
    <SidebarLink to="/profile" icon="fas fa-user">Profile</SidebarLink>
    <SidebarLink to="/carListing" icon="fas fa-columns">Car Listing</SidebarLink>
    <SidebarLink to="/signUp" icon="fas fa-arrow-right">Sign Up</SidebarLink>
    <SidebarLink to="/reservations" icon="fas fa-calendar">Reservations</SidebarLink>
    <SidebarLink to="/blankPage" icon="fas fa-calendar">Blank Page</SidebarLink>
    <SidebarLink to="/viewUsers" icon="fas fa-calendar">View Users</SidebarLink>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #ada3b8;
  --sidebar-item-hover: #d6cde0;
  --sidebar-item-active: #91859e;
}
</style>

<style scoped>
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
</style>