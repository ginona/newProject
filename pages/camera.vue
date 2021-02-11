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
      <v-btn color="black" dark disabled>
        <img src="~/assets/img/sauron-gif.gif" width="50px"
      /></v-btn>
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="600px" clas="border-alert">
      <v-card>
        <v-card-title class="justify-center text-center">
          <h1>!WARNING!</h1>
        </v-card-title>
        <v-card-text class="justify-center text-center">
          <br />
          <h3>GUN DETECTED</h3>
          <br />
          <h3>CAMERA 001</h3>
          <br />
          <h3>NOTIFYING THE AUTHORITIES</h3>
          <br />
          <img src="~/assets/img/sauron-gif.gif" width="200px" />
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn color="red darken-1" text @click="closeDialog()">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import VueFrame from 'vue-frame'
import socket from '~/plugins/socket.io.js'

export default {
  components: {
    VueFrame
  },
  data() {
    return {
      myIframe: null,
      dialog: false,
      audio: null,
    }
  },
  watch: {
    dialog(val) {
      if (val) {
        this.audio.play()
      } else {
        this.audio.pause()
      }
    },
  },
  created() {
    const self = this
    self.audio = new Audio('/alarm.mp3')
    socket.on('connect', function () {
      socket.emit('first-connect', 'A user has connected')
      console.log('Connected with socket')
    })

    socket.on('gun-detected', function (data) {
      self.playSound()
    })
  },
  methods: {
    playSound() {
      this.dialog = true
    },
    closeDialog() {
      this.dialog = false
    },
  },
}
</script>
