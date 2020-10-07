<template>
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
  </div>
</template>

<script>
import TheHeader from '@/components/home/TheHeader'
export default {
  name: 'Home',

  components: {
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
}

</style>
