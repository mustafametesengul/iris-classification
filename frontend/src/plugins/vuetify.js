import Vue from 'vue'
import Vuetify from 'vuetify/lib'

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      dark: {
        primary: colors.blue.base,
        secondary: colors.green.base,
        accent: colors.grey.base,
      },
    },
  },
})