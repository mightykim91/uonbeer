<template>
  <div id="header-img" class="flex-center">
    <div class="header-msg">
      세상의 모든 맥주를
      <br class="show-on-mobile">
      검색해보세요!
    </div>
    <search-bar></search-bar>
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
#header-img {
  flex-direction: column;
  height: 100vh;
  background: #333333;
  background-image: url('../../assets/img/header.jpg');
  background-size: cover;
}

.header-msg {
  margin-bottom: 20px;
  font-size: 3rem;
  font-weight: bolder;
  color: white;
  text-shadow: 2px 2px 2px black;
}

.mobile-br {
  display: none;
}

@keyframes slide-bg {
    from {background-position-x: 0%;}
    from {background-position-x: 100%;}
}

@media screen and (max-width: 768px) {
  #header-img {
    animation: slide-bg 20s linear infinite alternate;
  }

  .header-msg {
    font-size: 2rem;
  }
}
</style>