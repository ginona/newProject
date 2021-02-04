<template>
  <div>
    <br />
    <br />
    <br />
    <br />
    <br />
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <vue-web-cam
          ref="webcam"
          :device-id="deviceId"
          width="100%"
          @started="onStarted"
          @stopped="onStopped"
          @error="onError"
          @cameras="onCameras"
          @camera-change="onCameraChange"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { WebCam } from 'vue-web-cam'

export default {
  components: {
    'vue-web-cam': WebCam,
  },
  // middleware: ['auth'],
  data() {
    return {
      greeting: 'Hello World',
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
    }
  },
  computed: {
    ...mapGetters({
      tests: 'tests/list',
    }),
    device() {
      return this.devices.find((n) => n.deviceId === this.deviceId)
    },
  },
  watch: {
    camera(id) {
      this.deviceId = id
    },
    devices() {
      const [first] = this.devices
      if (first) {
        this.camera = first.deviceId
        this.deviceId = first.deviceId
      }
    },
  },
  mounted() {
    this.$store.dispatch('tests/list')
  },
  methods: {
    onCapture() {
      this.img = this.$refs.webcam.capture()
    },
    onStarted(stream) {
      // eslint-disable-next-line no-console
      console.log('On Started Event', stream)
    },
    onStopped(stream) {
      // eslint-disable-next-line no-console
      console.log('On Stopped Event', stream)
    },
    onStop() {
      this.$refs.webcam.stop()
    },
    onStart() {
      this.$refs.webcam.start()
    },
    onError(error) {
      // eslint-disable-next-line no-console
      console.log('On Error Event', error)
    },
    onCameras(cameras) {
      this.devices = cameras
      // eslint-disable-next-line no-console
      console.log('On Cameras Event', cameras)
    },
    onCameraChange(deviceId) {
      this.deviceId = deviceId
      this.camera = deviceId
      // eslint-disable-next-line no-console
      console.log('On Camera Change Event', deviceId)
    },
  },
}
</script>
