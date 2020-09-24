<template>
  <div class="modal-body">
        {{ item.name }}

        <div class="beer-content-box">
          <!-- beer info -->
          <div class="beer-info">
            {{ item }}
          </div>

          <!-- beer graph -->
          <div class="beer-graph">
            chart or something
          </div>
        </div>

        <!-- review -->
        <div class="review-wrap">

          <div class="review-title">리뷰</div>

          <!-- review input -->
          <div class="review-input-wrap">
            <div class="review-input-photo"></div>
            <textarea
              v-model="reviewContent"
              placeholder="리뷰를 작성해주세여"
              class="review-input" cols="30" rows="10">
            </textarea>

            <!-- review input submit button -->
            <div
              class="review-submit-btn-wrap">
              <div class="review-submit-btn">등록</div>
            </div>
          </div>

          <!-- review list -->
          <div v-if="beerReviewArray.length"></div>
          <div v-else class="no-review-wrap">
            작성된 리뷰가 없습니다. <br>
            첫 리뷰 작성자가 되어주세요!
          </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'BeerListItemDetail',

  data() {
    return {
      reviewContent: null,
    }
  },

  computed: {
    item() {
      return this.$store.state.beer.beerItem
    },
    beerReviewArray() {
      return this.$store.state.beer.beerReviewArray
    }
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';
$modal-width: 50vw;

.modal-wrap {
  position: fixed;
  top: 10vh;
  left: (100vw - $modal-width)/2;
  width: $modal-width;
  height: 80vh;

  // border-radius: 5px;
  background-color: white;

  overflow: auto;
  z-index: 5; 

  &::-webkit-scrollbar {
    display: none;
  }
}


.modal-title {
  border-bottom: 1px solid lightgrey;
  text-align: right;
  padding: 10px 15px;
  
  i{
    transition: 200ms;
    &:hover {
      color: tomato;
      transform: rotateZ(180deg);
    }
  }
}

.modal-overlay {
  @include fixed-background;
  background-color: black;
  z-index: 4;
}


.beer-content-box {
  display: flex;

  div {
    width: 30vw;
    height: 300px;
    border: 1px solid salmon;
  }
}

.review {
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

</style>