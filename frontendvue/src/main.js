import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueGoogleMaps from "@fawmi/vue-google-maps";

createApp(App)
  .use(store)
  .use(router)
  .use(VueGoogleMaps, {
    load: {
      key: process.env.VUE_APP_GMAPS_API_KEY,
    },
  })
  .mount("#app");
