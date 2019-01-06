import Vue from 'vue'
import App from './App.vue'


const MuseUI = require('muse-ui')
Vue.config.productionTip = false
Vue.use(MuseUI)

new Vue({
  render: h => h(App),
}).$mount('#app')