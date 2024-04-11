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
          zIndex: this.isOpen ? '999' : '-1',
          borderRadius: '10px',
          boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)' // Box shadow for depth effect
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
  /* Styles for the chatbot window */
  .chatbot-window {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    padding: 20px;
  }
  
  .message-container {
    overflow-y: auto;
    height: calc(100% - 70px);
    width: 100%;
  }
  
  .message {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
  }
  
  .user-message {
    background-color: #ada3b8; /* User message background color */
    color: white;
    align-self: flex-end;
  }
  
  .bot-message {
    background-color: #f0f0f0; /* Bot message background color */
  }
  
  .input-message {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    width: calc(100% - 22px);
    font-size: 16px;
  }
  
  /* Hover effect for input message */
  .input-message:hover {
    background-color: #eaeaea;
    transition: background-color 0.3s ease;
  }
  </style>
  