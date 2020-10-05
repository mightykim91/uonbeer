<template>
  <div class="beer-detail-wrap">
    <div class="beer-name-box">
      <div class="beer-name">{{ item.name }}</div>
        <div></div>
    </div>

    <div
      class="beer-content-box">
      <!-- beer img -->
      <div class="beer-img flex-center">
        <img :src="item.image_url? item.image_url:'asdf'">
      </div>
      <!-- beer info -->
      <div class="beer-info">
        <p class="info-title">맥주 정보</p>
        <p>스타일 : {{ item.style }}</p>
        <p>지역 : {{ item.country }}
          <span v-if="item.state">, {{ item.state }}</span>
        </p>
        <p>도수 : {{ item.abv }}</p>
      </div>
    </div>

    <!-- review -->
    <div class="review-wrap">
      <div class="flex-between">
        <div v-if="beerReviewArray.length">
          <div v-if="!isReviewCreate" class="info-title">
            평점 {{ avgRate }}
            <span style="margin-left: 10px;">
              {{ beerReviewArray.length }}개의 리뷰가 있습니다.</span>
          </div>
        </div>
        <div v-else>
          <div v-if="!isReviewCreate" class="info-title">
            평점 제공 불가
            <span style="margin-left: 10px;">
              {{ 1 - beerReviewArray.length }}개의 리뷰가 더 필요해요. </span>
          </div>        
        </div>

        <div v-if="isReviewCreate" class="info-title">리뷰 작성</div>

        <div 
          @click="toggleReview"
          class="base-btn">
          <span v-if="isReviewCreate"><i class="fas fa-list"></i> 리뷰 목록</span>
          <span v-else><i class="fas fa-pen"></i> 리뷰 작성</span>
        </div>
      </div>

      <!-- review create -->
      <beer-review-create
        @toggle-review="toggleReview"
        v-if="isReviewCreate"
        :itemId="item.id">
      </beer-review-create>

      <!-- review list -->
      <div v-if="!isReviewCreate" class="review-list-wrap">
        <!-- when reviews -->
        <div v-if="beerReviewArray.length" style="display:flex!important; flex-direction: column; align-items:start">
          <div v-for="reviews in beerReviewArray" :key="reviews.id" style="overflow: hidden">
            <i
              v-for="index in 5"
              :key="index"
              :class="[ reviews.rate >= index ? 'star-active' : '', 'fas fa-star']">
            </i>
            <i class="far fa-user" style="margin: 0 10px 0 30px;"></i><span style="margin-right: 50px">{{reviews.author}}</span> {{ reviews.content}}
          </div>
        </div>

        <div v-else class="no-review-wrap">
          작성된 리뷰가 없습니다. <br>
          첫 리뷰 작성자가 되어주세요!
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import BeerReviewCreate from '@/components/beer/BeerReviewCreate'

export default {
  name: 'BeerListItemDetail',

  components: {
    'beer-review-create': BeerReviewCreate,
  },

  data() {
    return {
      reviewContent: null,
      isReviewCreate: false,
      avgRate: 0
    }
  },

  computed: {
    item() {
      this.calavgRate()
      return this.$store.state.beer.beerItem
    },
    beerReviewArray() {
      return this.$store.state.beer.beerReviewArray
    }
  },

  methods: {
    calavgRate() {
      let sum = 0
      this.$store.state.beer.beerReviewArray.forEach((e) => { sum += e.rate})
      this.avgRate = sum / this.$store.state.beer.beerReviewArray.length
    },
    toggleReview() {
      this.isReviewCreate = !this.isReviewCreate
    },
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.beer {

  &-name {
    margin-bottom: 10px;
    font-size: 1.8rem;
    font-weight: bolder;

    &-box {
      margin: 10px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;

      border-bottom: 1px solid black;
      border-image-source: linear-gradient(to right, $highlight-color, crimson);
      border-image-slice: 60 30;
    }
  }

  &-info {
    padding: 5px;
    text-align: left;
    background-color: white;
    border-radius: 5px;

    .info-attr {
      font-weight: bold;
    }
  }

  &-img {
    background-color: #fefefe;
    border: 1px dashed lightgrey;

    img {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
    }
  }
}

.info-title {
  margin: 10px 0;
  text-align: left;
  font-size: 1.3rem;
  font-weight: bold;

  span {
    color: grey;
    font-size: 0.8rem;
    font-weight: light;
  }
}

.beer-content-box {
  display: flex;
  background: white;

  div {
    width: 30vw;
    height: 250px;
    // border: 1px solid salmon;
  }
}

.review {
  &-wrap {
    margin-top: 30px;
  }

  &-title {
    padding: 10px;
  }

  &-input-wrap {
    display: flex;
    // border-top: 1px solid lightgray;
    // border-bottom: 1px solid lightgray;
  }

  &-input {
    width: 75vw;
    height: 60px;
    transition: 200ms;
    border: none;
    padding: 10px 15px;
    
    &:focus {
      outline: none;
    }
  }

  &-submit-btn {
    @extend .flex-center;
    
    width: 65px;
    height: 30px;
    border-radius: 15px;
    background-color: #333333;
    color: white;
    font-size: 0.8rem;

    &-active {
      background-color: $highlight-color;
    }

    &-wrap {
      @extend .flex-center;
      width: 100px;
    }
  }
}

.no-review-wrap {
  padding: 50px;
}

@media screen and (max-width: 768px) {
  .modal-wrap {
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
  }

  .beer-content-box {
    display: inherit;
    div {
      width: auto;
    }
  }
}

//별점 색깔
.star-active {
  color: $highlight-color !important;
}
</style>