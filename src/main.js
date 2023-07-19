import { createApp } from 'vue'
import App from './App.vue'
import Vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const app = createApp(App)

app.use(Vuetify)
app.mount('#app')