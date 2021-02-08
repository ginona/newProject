<template>
  <v-app dark>
    <v-main>
        <v-hover v-slot="{ hover }">
          <v-navigation-drawer
            app
            permanent
            dark
            expand-on-hover
            mini-variant-width="100px"
            color="nav"
          >
            <v-avatar tile width="200px" class="mx-4 my-8" v-if="hover">
              <v-img
                  :src="require('@/assets/img/logo.png')"
                  alt="AMD"
                  max-height="90"
                  class="cursor-pointer"
                  contain
                ></v-img>
            </v-avatar>
            <v-avatar width="70px" class="mx-4 my-8" v-else >
              <v-img
                :src="require('@/assets/img/sauron-ico.png')"
                alt="AMD"
                max-height="90"
                class="cursor-pointer"
                contain
              ></v-img>
            </v-avatar>



            <v-list>
              <v-list-item
                v-for="(item, i) in items"
                :key="i"
                :to="item.to"
                router
                exact
              >
                <v-list-item-action>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title v-text="item.title" />
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-hover>
      <v-container class="px-12" fluid>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer dark padless>
      <v-card flat tile class="dark lighten-1 white--text text-center">
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 white--text"
            icon
          >
            <v-icon size="24px">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          <p style="padding-left: 10%; padding-right: 10%">
            El sistema de interpretación de imágenes para la detección de armas
            SAURON es un sistema basado en una inteligencia artificial que
            permite la detección de armas en fuego de pequeño calibre (pistolas
            y revólveres) en imágenes tomadas en tiempo real por cámaras de
            seguridad. Si se detecta la presencia de algún arma anteriormente
            mencionada, el sistema emitirá una alarma visual y sonora.
          </p>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Sauron</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      value: true,
      image: '/assets/img/sauron-ico.png',
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
      items: [
        {
          icon: 'mdi-home',
          title: 'Landing',
          to: '/',
        },
        {
          icon: 'mdi-camera',
          title: 'Camera',
          to: '/camera',
        },
        {
          icon: 'mdi-history',
          title: 'History',
          to: '/history',
        },
        {
          icon: 'mdi-account-multiple',
          title: 'Contacts',
          to: '/contacts',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Sauron',
    }
  },
  watch: {
    value(val) {
      console.log(val)
    },
  },
}
</script>
