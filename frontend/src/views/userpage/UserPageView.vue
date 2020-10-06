<template>
  <div>
    <!-- header -->
    <div class="user-header">
      <!-- user info section -->
      <div class="user-info-wrap">
        <div class="user-info-box">
          <!-- user photo -->
          <div class="user-photo">
            <div @click="onClickWIP" class="user-photo-btn">
              <i class="fas fa-camera"></i>
            </div>
          </div>

          <!-- user info -->
          <div class="user-info-content">
            <h1>{{ userData.username }}</h1>
            <h4>안녕하세요, 맥주를 좋아하는 {{ userData.username }}입니다</h4>
          </div>

          <!-- setting button -->
            <i
              v-if="isMyPage"
              @click="onClickWIP"
              class="fas fa-cog user-info-btn"></i>
        </div>
      </div>


      <!-- tabs -->
      <div class="user-content-tab-box">
        <div
          v-for="index in tabName.length" :key="index"
          @click="onSelectTab(index)"
          v-text="tabName[index-1]"
          :class="[selectedTab === index ? 
          'user-content-tab-selected' : '',
          'user-content-tab']">
        </div>
      </div>
    </div>

    <!-- content -->
    <div class="user-content-wrap">

      <!-- reviews -->
      <beer-review-list v-if="selectedTab === 1"></beer-review-list>
      <!-- wish list -->
      <beer-list v-if="selectedTab === 2"></beer-list>
      <!-- calendar -->
      <user-calendar v-show="selectedTab === 3"></user-calendar>
    </div>

  </div>
</template>

<script>
// components
import BeerList from '@/components/beer/BeerList'
import BeerReviewList from '../../components/beer/BeerReviewList'
import UserCalendar from '@/components/userpage/UserCalendar'

export default {
  name: 'UserPageView',

  components: {
    'beer-list': BeerList,
    'beer-review-list': BeerReviewList,
    'user-calendar': UserCalendar
  },

  data() {
    return {
      selectedTab: 1,
      tabName: ['리뷰', '위시리스트', '다이어리']
    }
  },

  computed: {
    isMyPage() {
      return this.$cookies.get('username') === this.userData.username
    }
  },

  methods: {
    onSelectTab(index) {
      this.selectedTab = index
    },
    onClickWIP() {
      alert('곧 업데이트될 예정입니다.')
    }
  },


  created() {
    const username = this.$route.params.username
    // getUserData 구현필요

    // data에 userData 설정
    this.userData = {
      username,
      reviewCount: 13,
    }

    // getUserReviewArray
    // store에 저장
    // reviewList, calendar에서 사용
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.user-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f2f2f2;
  // background-image: url('../../assets/img/header.jpg');
  background-image: $gradient-green;
  // background-size: 100%;
}

.user-info {
  &-wrap {
    margin: 70px 0 30px;  
  }

  &-box {
    position: relative;
    display: flex;
    align-items: center;
    background-color: white;
    width: 60vw;
    height: 180px;
    border: 1px solid lightgrey;
  }

  &-content {
    text-align: left;
    margin-right: 20px;
  }

  &-btn {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 1.3rem;
    transition: 400ms;
    &:hover {
      color: $highlight-color;
      transform: rotate(180deg);
    }
  }
}

.user-photo {
  position: relative;
  margin: 0 50px 0 100px;
  min-width: 100px; 
  min-height: 100px;
  border-radius: 100%;
  border: 3px solid grey;
  background: #f2f2f2;
}

.user-photo-btn {
  @extend .flex-center;
  position: absolute;
  top: 73px;
  left: 73px;
  width: 25px;
  height: 25px;
  border-radius: 100%;
  border: 2px solid $font-main;
  background: grey;
  color: white;
  font-size: 12px;

  &:hover {
    cursor: pointer;
    background: $highlight-color;
  }
}

.user-content-wrap {
  @extend .flex-center;
  margin-top: 50px;
  padding: 50px 10vw 100px;
  border-top: 1px solid lightgrey;
  background-color: #f2f2f2;
}

.user-content-tab {
  @extend .flex-center;
  // border: 1px solid lightgrey;
  color: white;

  width: 20vw;
  // min-width: 180px;
  height: 50px;
  font-size: 14px;

  &-box {
    @extend .flex-center;
    background-color: rgba(51, 51, 51, 0.8);
    width: 100vw;
  }

  &-selected {
    background-color: white !important;
    border-top: 3px solid $color-2;
    color: $font-main;
  }

  &:hover {
    cursor: pointer;
    background-color: rgba(51, 51, 51, 0.9);
  }
}


@media screen and (max-width: 768px) {
  .user-header {
    background: white;
  }

  .user-info {
    &-wrap {
      margin: 40px 0 0;
      background: white;
    }

    &-box {
      width: 100vw;
      border: none;
    }
  }
  
  .user-photo {
    margin: 20px;
  }

  .user-content-wrap {
    margin: 50px 0 100px;
  }

  .user-content-tab {
    margin: 0;
    flex-grow: 1;
    min-width: auto;
    height: 35px;
    font-size: 12px;

    &-box {
      width: 100vw;
    }
  }
}
</style>
