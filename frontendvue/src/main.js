import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueCookies from "vue-cookies";
import store from "./store";

// log the API key to the console
console.log("Google Maps API Key:", process.env.VUE_APP_GMAPS_API_KEY);

createApp(App)
  .use(store)
  .use(router)
  .use(VueGoogleMaps, {
    load: {
      key: process.env.VUE_APP_GMAPS_API_KEY,
    },
  })
  .mount("#app");
