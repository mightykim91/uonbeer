<template>
  <div
    :class="show ? '' : 'nav-hide'"
    id="nav">
  
    <!-- menu button -->
    <div
      v-if="show"
      @click="onClickMenu"
      id="menu-btn"
      class="flex-center">
        <i class="fas fa-bars"></i>
    </div>

    <!-- logo -->
    <div
      v-if="show"
      @click="onClickLink('/')"
      class="nav-logo flex-center">
      LOGO HERE
    </div>

    <!-- auth buttons pc && not authed -->
    <div
      v-if="show && !isAuthed"
      class="hide-on-mobile flex-center">
      <div @click="onClickLink('/auth/signup')">회원가입</div>
      <div
        @click="onClickLink('/auth/login')"
        class="nav-login-btn flex-center">로그인</div>
    </div>

    <!-- user button authed || mobile  -->
    <div
      v-if="show"
      @click="onClickUser"
      :class="[ isAuthed ? '' : 'show-on-mobile', 'nav-user-button flex-center']">
      <i class="fas fa-user-circle"></i>
    </div>

    <!-- user botton dropdown menu -->
    <div
      @click="onClickUser"
      v-if="showUserDropdown"
      class="user-dropdown-box">
      <div v-if="isAuthed">
        <div
          class="user-dropdown-item">마이페이지</div>
        <div
          @click="onClickLogout"
          class="user-dropdown-item">로그아웃</div>
      </div>
      <div v-else>
        <div
          @click="onClickLink('/auth/signup')"
          class="user-dropdown-item">회원가입
        </div>
        <div
          @click="onClickLink('/auth/login')"
          class="user-dropdown-item">로그인
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { hasScrolledDown, smoothScrollTo } from '@/util/common/scroll'
import api from '@/api/api'
import 'vuex'

export default {
  name: 'TheNavBar',

  data() {
    return {
      show: true,
      showUserDropdown: false,
      isCheckingScroll: false,
    }
  },

  computed: {
    isAuthed() {
      return !!this.$cookies.get('auth') | this.$store.state.common.cookie
    }
  },

  methods: {
    hideOnScroll() {
      if (!this.isCheckingScroll) {
        this.isCheckingScroll = true
        
        hasScrolledDown()
        .then(res => {
          this.show = !res
          this.isCheckingScroll = false
        })
      }      
    },
    onClickMenu() {
      this.$store.commit('common/toggleShowSidebar')
    },
    onClickLink(path) {
      this.$router.push(path)
        .catch(smoothScrollTo(0))
        .catch(() => {})
    },
    onClickUser() {
      this.showUserDropdown = !this.showUserDropdown
    },
    onClickLogout() {
      api.logout()
        .then(() => {
          this.$cookies.remove('auth')
          this.$store.commit('common/toggleCookie')
          this.$router.push('/')
          })
        .catch(() => alert('서버에러'))
    }
  },

  mounted() {
    document.addEventListener('scroll', this.hideOnScroll)
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

#nav {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;

  display: flex;
  justify-content: space-between;
  align-items: center;
  height: $nav-height;
  padding: 0 10vw;

  border-bottom: 1px solid lightgrey;
  background-color: #333333;
  background-image: $gradient-main;
  color: whitesmoke;
  font-size: 0.8rem;

  transition: ease-out 200ms;
  z-index: 2;

  div:hover {
    cursor: pointer;
  }
}

.nav-hide {
  height: 0 !important;
}

.nav-logo {
  width: 150px;
  height: $nav-height - 15;
  border: 3px solid $highlight-color;
  background: black;
  color: white;
  font-weight: bolder;
}

#menu-btn {
  display: flex;
  align-items: center;
  height: $nav-height - 10;
  // width: 116px;
  font-size: 1.2rem;
  text-align: left;
  transition: ease-in-out 300ms;

  &:hover {
    cursor: pointer;
    color: $highlight-color;
  }
}

.nav-login-btn {
  margin-left: 10px;

  height: $nav-height - 10;
  width: 60px;
  border-radius: 20px;
  background-color: #555555;
  color: white;
  transition: ease-out 200ms;

  &:hover {
    background-image: none;
    background-color: $highlight-color;
  }
}

.nav-user-button {
  width: 45px;
  font-size: 1.5rem;
}

.user-dropdown-box {
  position: absolute;
  top: $nav-height;
  right: 7.5vw;
  background-color: $font-main;
  color: white;
  
  .user-dropdown-item {
    @extend .flex-center;
    width: 120px;
    height: 40px;

    &:hover {
      background-color: $highlight-menu;
    }
  }
}

@media screen and (max-width: 768px) {
  #nav {
    padding: 0;
  }

  #menu-btn {
    width: 45px;
    justify-content: center;
  }

  .user-dropdown-box {
    right: 0;
  }
}
</style>