<template>
  <div class="flex-center beer-list-box">
    <div 
      v-for="(item, index) in searchResultArray" :key="index">
      <beer-list-item :item="item" :beer-id="index+1"></beer-list-item>
    </div>
  </div>
</template>

<script>
// components
import BeerListItem from './BeerListItem'

export default {
  name: 'BeerList',

  components: {
    'beer-list-item': BeerListItem
  },

  computed: {
    searchResultArray() {
      return this.$store.state.search.searchResultArray
    }
  },

  methods: {
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.beer-list-box {
  margin: 0 10vw;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
}

@media screen and (max-width: 768px){
  .beer-list-box {
    margin: 0 10px;
    grid-template-columns: 1fr;
    grid-gap: 10px;
  }
}
</style>