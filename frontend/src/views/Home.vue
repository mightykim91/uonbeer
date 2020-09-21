<template>
  <div>
    <the-header></the-header>
    <div style="height: 1000px;">
      <test-list></test-list>
    </div>
  </div>
</template>

<script>
import TheHeader from '@/components/home/TheHeader'
import TestList from '@/components/test/TestList'
export default {
  name: 'Home',

  components: {
    'the-header': TheHeader,
    'test-list': TestList
  }
}
</script>

<style>

</style>