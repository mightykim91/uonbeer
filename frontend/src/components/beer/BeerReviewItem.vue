<template>
<div>
  <div v-if="this.review" class="review-box">

    <!-- username & rate -->
    <div class="review-username-box">
      <!-- username  -->
      <div>
        <span class="review-username">
          {{ review.author }}
        </span>
        <!-- rate -->
        <span style="font-size: 10px">
          <i
            v-for="index in 5"
            :key="index"
            :class="[ review.rate >= index ? 'star-active' : '', 'fas fa-star']">
          </i>
        </span>
      </div>

      <!-- date -->
      <div class="review-date">
        {{ review.created_date }}
      </div>
    </div>

    <!-- content -->
    <div class="review-content">
      {{ review.content }}
    </div>

  </div>
</div>
</template>

<script>
export default {
  name: 'BeerReviewItem',

  props: {
    review: Object
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.review {
  &-box {
    width: 40vw;
    margin: 5px auto;
    padding: 10px 5px;
    border: 1px solid lightgrey;
    border-radius: 5px;
  }

  &-username-box {
    @extend .flex-between;
    border-bottom: 1px solid lightgrey;
  }

  &-username {
    font-weight: bolder;
  }

  &-content {
    min-height: 40px;
    padding: 10px;
    text-align: left;
  }

  &-date {
    width: 100px;
    font-size: 10px;
  }
}
//별점 색깔
.star-active {
  color: $highlight-color !important;
}

@media screen and (max-width: 768px) {
  .review-box {
    width: 90vw;
  }
}

</style>