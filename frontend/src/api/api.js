import axios from '../axios.js'

export default {
    //account
    login(data) {
        // return new Promise(function(resolve) {resolve({data: { key: 'temp'}})})
        return axios({
            url: 'rest-auth/login/',
            method: 'post',
            data: {
                email: data.email,
                password: data.password
            }
        })
    },
    logout() {
        return axios({
            url: 'rest-auth/logout/',
            method: 'post',
        })
    },
    signup(data) {
        return axios({
            url: 'rest-auth/registration/',
            method: 'post',
            data: {
                username: data.username,
                email: data.email,
                password1: data.password1,
                password2: data.password2,
            }
        })
    },
    getUser() {
        return axios({
            url: 'rest-auth/user/',
            method: 'get'
        })
    },

    //search
    search(data) {
        return axios({
            url: 'beer/search',
            method: 'get',
            params: { keyword: data.keyword }
        })
    },
    getSingleBeer(data) {
        return axios({
            url: 'beer/'+data,
            method: 'get',
        })
    },

    //review
    ReviewCreate(data) {
        return axios({
            url: 'review/create/',
            method: 'post',
            data: { 
                content: data.content, 
                rate: data.rate
            },
            headers: { 'Authorization': data.auth}
        })
    }
}