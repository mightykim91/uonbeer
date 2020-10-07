<template>
  <div>
      <p>WELCOME</p>
      <div id="video-pannel">
      </div>
      <button v-on:click="leave">나가기</button>
      <textarea v-model="chat"></textarea>
      <button v-on:click="send">send</button>
      <p v-for="message in messages" v-bind:key="message.id">{{ message }}</p>
  </div>
</template>

<script>
import io from 'socket.io-client'
import Peer from 'peerjs'

const socket = io('http://j3a405.p.ssafy.io:3000')
const myPeer = new Peer(undefined,{
    host: 'j3a405.p.ssafy.io',
    port: 9000,
    path:'/myapp',
    debug:3,
})
    
export default {
    name: 'FaceCall',
    data(){
        return {
            chat: '',
            messages: [],
            roomId: 10, //Room ID MUST BE MODIFED
            userId: '',
            
        }
    },
    mounted(){
        myPeer.on('open', userId => {
            console.log("id" + userId)
            this.userId = userId
            socket.emit('join', this.roomId, userId)
        })
        // socket.on('join', (msg) => {
        //     this.messages.push(msg)
        // })
        // socket.on('leave', (msg) => {
            
        //     this.messages.push(msg)
        // })
        socket.on('chat', (userId, msg) => {
            this.messages.push(`${userId}: ${msg}`)
        })


        const panel = document.querySelector('#video-pannel')
        const myVideo = document.createElement('video')

        myVideo.muted = true

        const peers = {}

        navigator.mediaDevices.getUserMedia({
            video: true, 
            audio: true,
        }).then(stream => {
            addVideoStream(myVideo, stream)

            myPeer.on('call', call => {
                call.answer(stream)
                const video = document.createElement('video')
                call.on('stream', userVideoStream => {
                    addVideoStream(video, userVideoStream)
                })
            })

            socket.on('join', (userId, msg) => {
                connectToUser(userId, stream)
                this.messages.push(msg)
            })
        })

        socket.on('leave', (userId, msg) => {
            if (peers[userId]){
                peers[userId].close()
            }
            this.messages.push(msg)
        })

        function connectToUser(userId, stream){
            const call = myPeer.call(userId, stream)
            const video = document.createElement('video')
            call.on('stream', userVideoStream => {
                addVideoStream(video, userVideoStream)
            })
            call.on('close', () => {
                video.remove()
            })
            peers[userId] = call
        }

        function addVideoStream(video, stream){
            video.srcObject = stream
            video.addEventListener('loadedmetadata', () => {
                video.play()
            })
            panel.append(video)
        }

        
    },
    methods: {
        send: function(){
            socket.emit('chat', this.roomId, this.userId, this.chat)
        },
        leave: function(){
            socket.emit('leave', this.roomId, this.userId)
            this.$router.push({name: 'Home'})
        }
    }
}
</script>

<style>

</style>