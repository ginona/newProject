<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
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
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-row justify="center" align="center"
        ><img src="~/assets/img/sauron-ico.png" width="50px"
      /></v-row>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light> mdi-repeat </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
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
          El sistema de interpretación de imágenes para la detección de armas
          SAURON es un sistema basado en una inteligencia artificial que permite
          la detección de armas en fuego de pequeño calibre (pistolas y
          revólveres) en imágenes tomadas en tiempo real por cámaras de
          seguridad. Si se detecta la presencia de algún arma anteriormente
          mencionada, el sistema emitirá una alarma visual y sonora.
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
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Sauron',
    }
  },
}
</script>
