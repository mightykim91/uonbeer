<template>
  <div
    class="beer-list-item-wrap flex-center">

    <!-- beer image -->
    <div class="beer-img-wrap" @click="show">
      <img :src="getRandomBeerImg()" alt="pic" class="beer-img">
    </div>

    <!-- beer info -->
    <div class="beer-info-box">

      <div class="beer-info-name">{{ item.name }}</div>
      <div>{{ item.country }}<span v-if="item.state">, {{ item.state }}</span></div>
      <div>{{ item.brewery }}</div>
      <div>ABV {{ item.abv }}</div>

      <div class="beer-match-rate">{{ matchRate }}%</div>
    </div>

    <div>
      
      <modal :name="String(beerId)">
        {{ item.name }}
        {{ item.abv}}
      </modal>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BeerListItem',
  
  props: {
    item: Object,
    beerId: Number
  },

  computed: {
    matchRate() {
      return Math.floor(Math.random() * 40, 1) + 60
    },
  },
  
  methods: {
    getRandomBeerImg() {
      let randomNumber = Math.floor(Math.random() * 5 + 1)
      return require(`../../assets/img/beer${randomNumber}.svg`)
    },
    show () {
      this.$modal.show(String(this.beerId));
    },
    hide () {
      this.$modal.hide(String(this.beerId));
    },
  },
}
</script>

<style lang="scss" scoped>
@use "sass:math";
@import '@/assets/style/base';

.beer-list-item-wrap {
  // display: flex;
  border: 1px solid lightgrey;

  &:hover {
    cursor: pointer;
    box-shadow: 5px 5px 10px grey;
  }
}

.beer-img {
  position: relative;
  top: -200px;
  left: 10px;
  z-index: 1;

  &-wrap {
    width: 150px;
    height: 220px;
    background-image: $gradient-main;
    overflow: hidden;
  }
}

.beer-info {
  &-box {
    flex-grow: 2;
    padding: 10px 20px;
    height: 200px;
    text-align: left;

    div {
      margin: 10px 0;
      color: $font-main;
    }
  }
  &-name {
    // border: none;
    // border-bottom: 6px solid;
    // border-image-slice: 1;
    // border-width: 3px;
    // border-image-source: linear-gradient(to left, #ffc506, #3e5de6);
    // border-bottom: 2px solid salmon;
    color: black !important;
    font-size: 1.5rem;
    font-weight: bolder;
  }
}

.beer-match-rate {
  color: black !important;
  font-size: 3rem;
  font-weight: bolder;
  text-align: center;
}
</style>