<template>
  <div v-if="isOpen" class="chatbot-window" :style="chatbotWindowStyle">
    <!-- Chat interface content -->
    <div class="message-container" ref="messageContainer">
      <div
        v-for="(message, index) in messages"
        :key="index"
        class="message"
        :class="{
          'user-message': message.user === 'user',
          'bot-message': message.user === 'bot',
        }"
      >
        {{ message.text }}
      </div>
      <div v-if="isLoading" class="loading-indicator">Typing...</div>
    </div>
    <input
      v-model="newMessage"
      @keyup.enter="sendMessageAndClear"
      placeholder="Type a message..."
      class="input-message"
      aria-label="Type your message here"
    />
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    isOpen: Boolean,
  },
  data() {
    return {
      messages: [],
      newMessage: "",
      isLoading: false,
    };
  },
  computed: {
    chatbotWindowStyle() {
      return {
        position: "fixed",
        bottom: this.isOpen ? "80px" : "-380px",
        right: "20px",
        width: "300px",
        height: "400px",
        border: "1px solid #ccc",
        backgroundColor: "#f4f4f4",
        zIndex: this.isOpen ? "999" : "-1",
        borderRadius: "10px",
        boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.1)",
      };
    },
  },
  methods: {
    scrollToBottom() {
      this.$nextTick(() => {
        if (this.$refs.messageContainer) {
          this.$refs.messageContainer.scrollTop =
            this.$refs.messageContainer.scrollHeight;
        }
      });
    },
    sendMessageAndClear() {
      if (!this.newMessage.trim()) return;
      this.sendMessage();
      this.newMessage = "";
    },
    sendMessage() {
      this.isLoading = true;
      this.messages.push({ text: this.newMessage, user: "user" });
      axios
        .post(process.env.VUE_APP_CHAT_ENDPOINT, { message: this.newMessage })
        .then((response) => {
          response.data.forEach((msg) => {
            this.messages.push({ text: msg.text, user: "bot" });
          });
        })
        .catch((error) => {
          console.error("Error sending message:", error);
          this.messages.push({
            text: "Failed to get response from the server.",
            user: "bot",
          });
        })
        .finally(() => {
          this.isLoading = false;
          this.scrollToBottom();
        });
    },
  },
};
</script>

<style scoped>
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
  background-color: #ada3b8;
  color: white;
  align-self: flex-end;
}

.bot-message {
  background-color: #f0f0f0;
}

.input-message {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  width: calc(100% - 22px);
  font-size: 16px;
}

.input-message:hover {
  background-color: #eaeaea;
  transition: background-color 0.3s ease;
}

.loading-indicator {
  color: #aaa;
  font-style: italic;
}
</style>
