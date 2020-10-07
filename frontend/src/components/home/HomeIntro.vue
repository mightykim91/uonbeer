<template>
  <div class="home-intro-section">

      <div class="home-line"></div> 

      <div class="home-intro-title">
        U WANT BEER.는 <br> 맥주를 즐기는 사람들을 위한 <br> 커뮤니티입니다.
      </div>

      <div class="home-line"></div> 

      <!-- cards -->
      <div class="home-intro-card-wrap">

        <div class="home-intro-card">
          <div class="home-intro-card-img"></div>
          <div class="home-intro-card-msg">
            검색하고 <br class="hide-on-mobile"> 리뷰를 <br> 남겨보세요.
          </div>
        </div>

        <div class="home-intro-card">
          <div class="home-intro-card-img"></div>
          <div class="home-intro-card-msg">
            캘린더로 <br class="hide-on-mobile"> 기록을 <br> 관리해보세요.
          </div>
        </div>
        <div class="home-intro-card">
          <div class="home-intro-card-img"></div>
          <div class="home-intro-card-msg">
            빅데이터 분석으로 <br> 취향의 맥주를 <br> 추천해드립니다.
          </div>
        </div>

        <div class="home-intro-card">
          <div class="home-intro-card-img"></div>
          <div class="home-intro-card-msg">
            다른 사용자들과 <br> 실시간으로 <br> 소통해보세요
          </div>
        </div>
      </div>

      <!-- signup -->
      <div class="signup-btn">
        회원가입하고 이 모든 혜택 누리기
      </div>
    </div>
</template>

<script>
export default {
  name: 'HomeIntro'
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-line {
  width: 50vw; height: 0;
  margin: 50px auto;
  border-bottom: 1px solid lightgrey;
}


.home-intro-section {
  margin: 0 10vw;
}

.home-intro-title {
  margin: 50px auto;
  font-weight: bolder;
  font-size: 1.5rem;
  line-height: 150%;
}

.home-intro-card {
  @extend .flex-center;
  flex-direction: column;
  margin: 30px auto;
  width: 210px;
  height: 250px;
  padding: 10px 15px;

  background: white;
  border-radius: 5px;
  border: 1px solid lightgrey;
  box-shadow: 5px 5px 5px lightgrey;

  &-wrap {
    display: flex;
  }

  &-img {
    margin-bottom: 10px;
    width: 210px;
    height: 120px;
    border: 1px dashed lightgrey;
    background: $highlight-color;
  }

  &-msg {
    margin-left: 15px;
    font-size: 1.3rem;
    font-weight: 500;
    text-align: left;
    line-height: 150%;
  }
}

.signup-btn {
  @extend .base-btn;
  margin: 50px auto;
  width: 250px;
  height: 100px;
  background: white;
}

@media screen and (max-width: 768px) {

  .home-intro {
    &-section {
      margin: 0;
    }

    &-card {
      min-width: 0;
      width: 80vw;
      left: 10vw;

      &-msg {
        margin: 0;
      }
    }

    &-card-wrap {
      flex-direction: column;
    }
}
}
</style>