<template>
  <div class="beer-list-item-wrap flex-center">

    <!-- beer image -->
    <div 
      @click="onClickBeerItem"
      class="beer-img-wrap">
      <img
        :src="item.image_url? item.image_url:getRandomBeerImg()" alt="pic" class="beer-img">
    </div>

    <!-- beer info -->
    <div class="beer-info-box">

      <div class="beer-info-name">{{ item.name }}</div>
      <div>{{ item.country }}<span v-if="item.state">, {{ item.state }}</span></div>
      <div>{{ item.brewery }}</div>
      <div>ABV {{ item.abv }}</div>

      <!-- <div class="beer-match-rate">{{ matchRate }}%</div> -->
    </div>
  </div>
</template>

<script>
// modules
import api from '@/api/api'

// components
export default {
  name: 'BeerListItem',

  props: {
    item: Object,
    beerId: Number,
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
    fetchReview() {
      api.getReviewByBeer({ beer: this.beerId})
        .then((res) => {
          this.$store.state.beer.beerReviewArray = res.data
        })
        .catch(()=> alert('err'))
    },
    onClickBeerItem() {
      this.$store.commit('beer/setBeerItem', this.item)
      this.$store.state.beer.beerReviewArray = []
      this.fetchReview()
      this.$store.commit('common/toggleShowModal')
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
  // top: -200px;
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

.modal-info {
  &-title {
    padding: 5px;
    text-align: right;
    border-bottom: 1px solid lightgrey;

    i {
      transition: 200ms;
      font-size: 1.3rem;

      &:hover {
        color: tomato;
        transform: rotateZ(180deg);
      }
    }
  }

  &-name {
    height: 20px;
    border-bottom: 1px solid lightgrey;
  }

  &-box {
    display: flex;
    height: 220px;

    div {
      width: 300px;
      border: 1px solid salmon;
    }
  }
}

.review-input {
  width: 300px;
  height: 150px;
}

@media screen and (max-width: 768px) {
  .modal-info-box {
    display: inherit;
    max-width: 100vw;
  }
}

</style>