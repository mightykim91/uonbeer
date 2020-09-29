<template>
  <div>
    <!-- header -->
    <div class="user-header">
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
      <!-- user info -->
      <div v-if="selectedTab === 1" class="user-info-wrap">
        <div class="user-info-box">

          <h1>username: {{ userData.username }}</h1>
          <h3>리뷰 개수: {{ userData.reviewCount }}</h3>

        </div>

        <!-- chart -->
        <div class="user-info-box flex-center">
          chart or something..
        </div>


      </div>



      <!-- reviews -->
      <beer-review-list v-if="selectedTab === 2"></beer-review-list>
      <!-- wish list -->
      <beer-list v-if="selectedTab === 3"></beer-list>
      <!-- calendar -->

    </div>

  </div>
</template>

<script>
// components
import BeerList from '@/components/beer/BeerList'
import BeerReviewList from '../../components/beer/BeerReviewList'


export default {
  name: 'UserPageView',

  components: {
    'beer-list': BeerList,
    'beer-review-list': BeerReviewList,
  },

  data() {
    return {
      selectedTab: 1,
      tabName: ['유저 정보', '리뷰', '위시리스트', '다이어리']
    }
  },

  methods: {
    onSelectTab(index) {
      this.selectedTab = index
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
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.user-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 230px;
  background-color: #f2f2f2;
  // background-image: url('../../assets/img/header.jpg');
  // background-size: 50%;
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

.user-info-wrap {
  display: flex;
  justify-content: space-between;
  width: 80vw;
}

.user-info-box {
  background-color: white;
  width: 39vw;
  height: 300px;
  border: 1px solid lightgrey;
}

@media screen and (max-width: 768px) {
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
