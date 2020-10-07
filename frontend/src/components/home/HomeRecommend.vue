<template>
  <div>

    <!-- title -->
    <div class="home-line"></div>

    <div class="home-title">
      {{ username }}님을 위한
      <br class="show-on-mobile">
      오늘의 추천 맥주
      <div class="home-title-sub">
        ※ 추천 맥주는 사용자 활동을 바탕으로 <br>
        매일 오후 2시 업데이트 됩니다.
      </div>
    </div>
    
    <div class="home-line"></div>

    <!-- content -->
    <div v-if="isLoading" class="home-loading">
      <div>
        빅데이터 분석을 통해
        <br class="show-on-mobile">
        취향에 맞는 맥주를
        <br class="show-on-mobile">
        냉장고에서 고르는 중입니다...</div>
      <vue-loading
        type="cylon" color="#29a3e9"
        :size="{ width: '80px', height: '50px' }">
      </vue-loading>
    </div>

    <div v-else></div>
  </div>
</template>

<script>
// components

// modules
import api from '@/api/api'

export default {
  name: 'HomeRecommend',

  components: {
  },

  data() {
    return {
      isLoading: true,
    }
  },
  
  computed: {
    username() {
      return this.$cookies.get('username')
    },
  },

  methods: {
  },

  created() {
    console.log('created')
    console.log(this.$cookies.get('auth'))
    api.getRecommendArray(this.$cookies.get('auth'))
    .then((res) => {
      console.log(res)
    })
  },

  mounted() {
    console.log('mounted')
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-line {
  width: 50vw;
  min-width: 250px;
  height: 0;
  margin: 50px auto;
  border-bottom: 1px solid lightgrey;
}

.home-title {
  margin: 50px auto;
  font-weight: bolder;
  font-size: 1.5rem;
  line-height: 150%;

  &-sub {
    margin-top: 30px;
    font-weight: normal;
    font-size: 1rem;
    color: grey;
    line-height: 130%;
  }
}

.home-section {
  margin: 50px 10vw;
}

.home-loading {
  @extend .flex-center;
  flex-direction: column;
  margin-bottom: 200px;
  height: 300px;
}

.vue-loading {
  margin: 50px auto !important;
}
</style>
