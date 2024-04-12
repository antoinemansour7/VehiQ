// Import Vue Router
import router from "@/router"; // Adjust the path based on your project setup

// Vuex store file
import { createStore } from "vuex";

export default createStore({
  state: {
    isLoggedIn: false,
    user: null,
    notification: null, // Add a field for notification message
    isChatbotOpen: false, // Trach chatbot visibility
  },
  mutations: {
    SET_LOGIN_STATE(state, { isLoggedIn, notification }) {
      // Modify mutation to accept notification
      state.isLoggedIn = isLoggedIn;
      state.notification = notification; // Set the notification message
    },
    SET_USER(state, user) {
      state.user = user;
    },
    CLEAR_NOTIFICATION(state) {
      state.notification = null; // Clear the notification message
    },
    TOGGLE_CHATBOT(state) {
      state.isChatbotOpen = !state.isChatbotOpen;
    },
  },
  actions: {
    login({ commit }, user) {
      const notification = "You have logged in successfully."; // Set notification message
      commit("SET_LOGIN_STATE", { isLoggedIn: true, notification });
      commit("SET_USER", user);

      // Redirect to a certain page after login
      router.push("/carListing"); // Adjust the path as needed
    },
    logout({ commit }) {
      const notification = "You have logged out successfully."; // Set notification message
      commit("SET_LOGIN_STATE", { isLoggedIn: false, notification });
      commit("SET_USER", null);

      // Redirect to a certain page after logout
      router.push("/"); // Adjust the path as needed
    },
    clearNotification({ commit }) {
      commit("CLEAR_NOTIFICATION"); // Clear the notification message
    },
  },
});
