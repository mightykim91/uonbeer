<template>
  <div id="app">
    <the-nav-bar></the-nav-bar>
    <the-side-bar></the-side-bar>
    <router-view/>
  </div>
</template>

<script>
import TheNavbar from '@/components/common/TheNavbar'
import TheSidebar from '@/components/common/TheSidebar'

export default {
  components: {
    'the-nav-bar': TheNavbar,
    'the-side-bar': TheSidebar
  },
  
  data() {
    return {
      showSide: false,
    }
  },
}
</script>

<style lang="scss">
@import '@/assets/style/base';

@font-face {
  font-family: "NanumSquareR";
  src: url("./assets/fonts/NanumSquareR.ttf") format("truetype");
}

body {
  margin: 0;
}

#app {
  font-family: "NanumSquareR";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
