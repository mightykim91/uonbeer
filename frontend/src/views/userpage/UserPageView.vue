<template>
  <div id="user-view-wrap">
    <h1>USERPAGE</h1>
    
    <div class="user-content-wrap">
      <div class="user-content-info">
        유저 사진
        유저 정보
      </div>
      <div class="user-content">

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'UserPageView',
  
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

#user-view-wrap {
  margin: 50px 10vw 100px;
}

.user-content-wrap {
  @extend .flex-center;
}

.user-content-box {
  display: grid;
}
</style>