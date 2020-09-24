<template>
  <div v-if="showModal">
    <!-- overlay -->
      <div
        @click="hideModal"
        class="modal-overlay">
      </div>

    <!-- modal -->
    <div
      class="modal-container">
      <!-- title -->
      <div class="modal-header">
        <!-- close button -->
        <i @click="hideModal" class="far fa-times-circle">
        </i>
      </div>

      <!-- body -->
      <div class="modal-body">
        <beer-list-item-detail></beer-list-item-detail>
      </div>
    </div>    
      
  </div>
</template>

<script>
import BeerListItemDetail from '@/components/beer/BeerListItemDetail'

export default {
  name: 'ModalMain',

  components: {
    'beer-list-item-detail': BeerListItemDetail
  },

  computed: {
    showModal() {
      return this.$store.state.common.showModalMain
    },
  },

  methods: {
    hideModal() {
      this.$store.commit('common/toggleShowModal')
    },
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';
$modal-width: 50vw;
$modal-height: 70vh;

.modal {
  &-overlay {
    @include fixed-background;
    background-color: black;
    opacity: 0.8;
    z-index: 4;
  }

  &-container {
    position: fixed;
    top: 15vh;
    left: (100vw - $modal-width)/2;

    width: $modal-width;
    height: $modal-height;
    background-color: white;

    overflow: auto;
    z-index: 5; 

    &::-webkit-scrollbar {
      display: none;
    }
  }

  &-header {
    border-bottom: 1px solid lightgrey;
    text-align: right;
    padding: 10px 15px;
    
    i {
      transition: 200ms;
  
      &:hover {
        transform: rotateZ(180deg);
      }
    }
  }

  &-body {
    padding: 0 20px 15px;
  }
}

@media screen and (max-width: 768px) {
  .modal-container {
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
  }
}

</style>