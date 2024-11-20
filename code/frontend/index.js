document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");
  const messages = document.getElementById("messages");

  const standardResponses = {
    hello: "Hello! How can I assist you today?",
    default: "Sorry, I did not understand that. Can you please repeat?",
  };

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const userMessage = input.value.trim();
    if (userMessage === "") return;

    addMessage(userMessage, "user-message");
    input.value = "";

    const response =
      standardResponses[userMessage.toLowerCase()] || standardResponses.default;
    addMessage(response, "bot-message");
  });

  function addMessage(text, className) {
    const div = document.createElement("div");
    div.className = `message ${className}`;
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }
});
