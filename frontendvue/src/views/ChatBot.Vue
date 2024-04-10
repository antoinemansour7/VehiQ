<template>
    <div id="chatbot">
      <div v-for="(message, index) in messages" :key="index" :class="message.type + '-message'" class="message">
        {{ message.text }}
      </div>
      <input type="text" v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message...">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userMessage: '',
        messages: []
      };
    },
    methods: {
        sendMessage() {
            if (this.userMessage.trim() === '') return;
            
            this.messages.push({ text: 'User: ' + this.userMessage, type: 'user' });

            // Simulate bot response
            setTimeout(() => {
                let botResponse = '';

                switch (this.userMessage.toLowerCase()) {
                case 'hello':
                    botResponse = 'Bot: Hi there! How can I assist you today?';
                    break;
                case 'what services do you provide?':
                    botResponse = 'Bot: We provide a range of services including consultation, troubleshooting, and support.';
                    break;
                case 'how can i get in touch with customer support?':
                    botResponse = 'Bot: You can contact our customer support team through email at support@vehoq.com or by phone at 514-652-8734.';
                    break;
                default:
                    botResponse = 'Bot: Sorry, I am just a dummy bot and cannot respond intelligently.';
                }

                this.messages.push({ text: botResponse, type: 'bot' });
            }, 500);

            this.userMessage = '';
        }

    }
  };
  </script>
  
  <style scoped>
  #chatbot {
    font-family: Arial, sans-serif;
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .message {
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
  }
  .user-message {
    background-color: #DCF8C6;
    text-align: right;
  }
  .bot-message {
    background-color: #EEE;
    text-align: left;
  }
  </style>
  