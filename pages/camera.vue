<template>
  <div>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <div id="app">
          <vue-frame
            text=""
            url="http://localhost:5000/video_feed"
            frame="myframe"
            type="button"
            class="form-control"
            :default="true"
          ></vue-frame>
          <v-row justify="center" align="center">
            <iframe id="myframe" height="365" width="645"></iframe>
          </v-row>
        </div>
      </v-col>
    </v-row>
    <br />
    <br />
    <v-row justify="center" align="center">
      <v-btn color="black" dark @click="playSound()">
        <img src="~/assets/img/sauron-gif.gif" width="50px"
      /></v-btn>
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="600px" clas="border-alert">
      <v-card>
        <v-card-title class="justify-center text-center">
          <h1>!ALERTA!</h1>
        </v-card-title>
        <v-card-text class="justify-center text-center">
          <br />
          <h3>ARMA DETECTADA</h3>
          <br />
          <h3>CÁMARA 001</h3>
          <br />
          <h3>AVISANDO A LAS AUTORIDADES</h3>
          <br />
          <img src="~/assets/img/sauron-gif.gif" width="200px" />
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn color="red darken-1" text @click="closeDialog()">
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import VueFrame from 'vue-frame'
const { Howl } = require('howler')
// import { WebCam } from 'vue-web-cam'

export default {
  components: {
    VueFrame,
    // 'vue-web-cam': WebCam,
  },
  // middleware: ['auth'],
  data() {
    return {
      myIframe: null,
      dialog: false,
      audio: false,
      sound: null,
    }
  },
  methods: {
    playSound() {
      this.dialog = true
      this.sound = new Howl({
        src: '/alarm.mp3',
        autoplay: true,
        duration: 10,
        loop: true,
        volume: 1,
      })
      // eslint-disable-next-line no-console
      // eslint-disable-next-line no-console
      this.sound.play()
    },
    closeDialog() {
      this.dialog = false
      this.sound.stop()
      this.sound.unload()
      this.sound = null
    },
  },
}
</script>
