<template>
  <div class="calendar-wrap">
    <v-calendar
    is-expanded
    :min-date='minDate'
    :attributes="attributes"
    />
  </div>
</template>

<script>
export default {
  name: 'UserCalendar',
  
  data() {
    return {
      minDate: new Date(2020, 8, 1),
      attributes: [
        {
          key: 'today',
          highlight: true,
          popover: { label: '맥주와 함께하기 좋은 오늘입니다!' },
          dates: new Date(),
        }
      ]
    }
  },

  created() {
    // userReviewArray = api.getUserReviewArray
    // UserPageView에서 미리 수행한 뒤 store에 state로 저장, 호출하여 사용

    //  dummy data
    const userReviewArray = [
      {
        beer: 'Cass',
        created_date: new Date(2020, 9, 6),
      },
      {
        beer: 'Cass',
        created_date: new Date(2020, 9, 6),
      },
      {
        beer: 'Cass',
        created_date: new Date(2020, 9, 6),
      },
      {
        beer: 'Klaud',
        created_date: new Date(2020, 9, 10),
      },
    ]

    function toAttributesFormat(review) {
      return {
        dates: review.created_date,
        dot: { color: 'red' },
        popover: { label: review.beer }
      }
    }
    
    this.attributes = [
      ...this.attributes,
      ...userReviewArray.map(review => toAttributesFormat(review))
    ]
  }
}
</script>

<style lang="scss" scoped>
.calendar-wrap {
  width: 100vw;
  max-width: 800px;
}
</style>