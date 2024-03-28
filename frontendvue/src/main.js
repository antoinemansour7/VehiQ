import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueGoogleMaps from "@fawmi/vue-google-maps";

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
