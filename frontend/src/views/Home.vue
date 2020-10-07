<template>
  <div>
    <the-header></the-header>
    
    <div v-if="isAuthed" class="home-section"> 
    </div>

    <home-intro v-else></home-intro>

    
  </div>
</template>

<script>
import TheHeader from '@/components/home/TheHeader'
import HomeIntro from '@/components/home/HomeIntro'

export default {
  name: 'Home',

  components: {
    'the-header': TheHeader,
    HomeIntro
  },
  
  computed: {
    isAuthed() {
      return this.$store.getters['common/isAuthed']
    }
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-section {
}

</style>
