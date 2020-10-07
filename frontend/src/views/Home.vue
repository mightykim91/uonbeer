<template>
  <div id="header-img" class="flex-center">
    <div class="header-msg">
      U WANT BEER. <br>
      NOW. <br>
      <p class="header-msg-sm">
        지금 원하는 맥주를 검색해보세요!
      </p>
  <div>
    <the-header></the-header>
    
    <div v-if="isAuthed" class="home-section">
    </div>

    <div v-else class="home-section home-intro-section">
      <div class="home-intro-card">
        <!-- <div class="home-intro-card-img">
        </div> -->
        <div class="home-intro-card-msg">
          검색하십시오.
        </div>
      </div>
      <div class="home-intro-card">
        <div class="home-intro-card-msg">
          리뷰하고 캘린더에 기록하십시오.
        </div>
      </div>
      <div class="home-intro-card">
        <div class="home-intro-card-msg">
          추천받으십시오.
        </div>
      </div>

      <div class="home-intro-card">
        <div class="home-intro-card-msg">
          다른 사용자들과 소통하십시오.
        </div>
      </div>


      <div class="signup-btn">
        회원가입하고 이 모든 혜택 누리기
      </div>
    </div>
    <div class="search-bar-wrap">
      <search-bar></search-bar>
    </div>
    <vue-particles
        color="#ffffff"
        :particleOpacity="1"
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
    'the-header': TheHeader,
  },
  
  computed: {
    isAuthed() {
      return this.$store.getters['common/isAuthed']
    }
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-section {
  padding: 100px auto;
}

.home-intro-section {
  display: flex;
  flex-direction: column;
  padding-top: 100px;
  // background-image: $gradient-green;
  height: 1800px;
}

.home-intro-card {
  display: flex;
  align-items: center;

  margin: 70px auto;
  width: 40vw;
  min-width: 500px;
  height: 300px;
  padding: 10px 15px;

  background: white;
  border-radius: 5px;
  border: none;
  box-shadow: 5px 5px 10px grey;

  &-img {
    border: 1px solid salmon;
    width: 200px;
    height: 280px;
  }

  &-msg {
    margin-left: 30px;
    overflow-wrap: normal;
    font-size: 2rem;
    text-align: left;
  }
}

.signup-btn {
  @extend .base-btn;
  margin: 0 auto 150px;
  width: 300px;
  height: 100px;
  background: white;
}

@media screen and (max-width: 768px) {
  .home-intro-card {
    min-width: 0;
    width: 80vw;
    left: 10vw;
  }
  
  .header-msg {
    font-size: 2rem;
  }
}
</style>
