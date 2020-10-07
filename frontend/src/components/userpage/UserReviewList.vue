<template>
<div v-if="reviewArray">
  <beer-review-item
    v-for="(item, index) in reviewArray" :key="index">
  </beer-review-item>
</div>
</template>

<script>
import BeerReviewItem from '@/components/beer/BeerReviewItem'

export default {
  name: 'UserReviewList',

  components: {
    BeerReviewItem,
  },

  props: {
    reviewArray: Array
  }


}
</script>

<style>

</style>