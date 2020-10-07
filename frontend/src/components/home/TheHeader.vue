<template>
  <div id="header-img" class="flex-center">
    <div class="header-msg">
      U WANT BEER. <br>
      NOW. <br>
      <p class="header-msg-sm">
        지금 원하는 맥주를 검색해보세요!
      </p>
    </div>

    <div class="search-bar-wrap">
      <search-bar></search-bar>
    </div>

    <vue-particles
        color="#ffffff"
        :particleOpacity="0.8"
        :particlesNumber="150"
        shapeType="circle"
        :particleSize="13"
        linesColor="#dedede"
        :linesWidth="1"
        :lineLinked="false"
        :lineOpacity="0"
        :linesDistance="150"
        :moveSpeed="3"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
        style="height: 100%; width: 100%;"
      >
      </vue-particles>
  </div>
</template>

<script>
import SearchBar from '@/components/common/SearchBar'

export default {
  components: {
    'search-bar': SearchBar
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

#header-img {
  position: relative;
  flex-direction: column;
  height: 80vh;
  background: #333333;
  background-image: $gradient-yellow;
  background-size: cover;
}

.header-msg {
  position: absolute;
  top: 20vh;
  margin-bottom: 20px;
  width: 50vw;
  font-size: 3rem;
  font-weight: bolder;
  text-align: left;
  color: white;
  text-shadow: 3px 3px 5px #333333;

  &-sm {
    font-size: 1rem;
    text-shadow: none;
    color: black;
  }
}

.search-bar-wrap {
  position: absolute;
  top: 40vh;
}


@media screen and (max-width: 768px) {
  .header-msg {
    font-size: 2rem;
  }
}
</style>
