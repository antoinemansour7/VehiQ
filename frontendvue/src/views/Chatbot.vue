<template>
    <div v-if="isOpen" class="chatbot-window" :style="chatbotWindowStyle">
      <!-- Chat interface content -->
      <div class="message-container">
        <div v-for="(message, index) in messages" :key="index" class="message" :class="{ 'user-message': message.user === 'user', 'bot-message': message.user === 'bot' }">{{ message.text }}</div>
      </div>
      <input v-model="newMessage" @keyup.enter="sendMessageAndClear" placeholder="Type a message..." class="input-message">
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      isOpen: Boolean
    },
    data() {
      return {
        messages: [],
        newMessage: ''
      };
    },
    computed: {
      chatbotWindowStyle() {
        return {
          position: 'fixed',
          bottom: this.isOpen ? '80px' : '-380px', // Adjust the bottom position to show above the button
          right: '20px',
          width: '300px',
          height: '400px',
          border: '1px solid #ccc',
          backgroundColor: '#f4f4f4', // Background color
          zIndex: this.isOpen ? '999' : '-1'
        };
      }
    },
    mounted() {
      // Fetch initial messages from Rasa server when component is mounted
      this.getInitialMessages();
    },
    methods: {
      getInitialMessages() {
        axios.get('http://localhost:5002/api')
          .then(response => {
            this.messages = response.data.messages;
          })
          .catch(error => {
            console.error('Error fetching initial messages:', error);
          });
      },
      sendMessageAndClear() {
            // Call sendMessage method
            this.sendMessage();

            // Clear the input field
            this.newMessage = '';
        },
        sendMessage() {
            // Ensure the new message is not empty
            if (!this.newMessage.trim()) return;

            // Add the new message to the messages array
            this.messages.push({ text: this.newMessage, user: 'user' });

            // Send the message to the Rasa server
            axios.post('http://localhost:5002/api', { text: this.newMessage })
            .then(response => {
                // Add the response message to the messages array
                this.messages.push({ text: response.data.text, user: 'bot' });
            })
            .catch(error => {
                console.error('Error sending message:', error);
            });
        }
    }
  };
  </script>
  
  <style scoped>
  .chatbot-window {
    /* Styles for the chatbot window */
  }
  
  .message-container {
    overflow-y: auto;
    height: calc(100% - 50px);
    padding: 10px;
  }
  
  .message {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
    max-width: 70%;
  }
  
  .user-message {
    background-color: #d6cde0; /* User message background color */
    color: white;
    align-self: flex-end;
  }
  
  .bot-message {
    background-color: #d3d3d3; /* Bot message background color */
  }
  
  .input-message {
    margin: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: calc(100% - 20px);
    align-self: flex-end;
  }
  </style>
  