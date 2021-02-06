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
  </div>
</template>

<script src="/dist/vue-frame.js"></script>
<script>
import { mapGetters } from 'vuex'
import VueFrame from 'vue-frame'
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
    }
  },
}
</script>
