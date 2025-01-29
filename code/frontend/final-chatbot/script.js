// Diario gite Karis: http://karis.cloud.neth.eu/blogger-gb-news/

const apiUrl = "http://karis.sf.nethserver.net:8888/generate";

// apri i link ai documenti in una nuova scheda
const renderer = new marked.Renderer();
renderer.link = function (href, title, text) {
  const link = marked.Renderer.prototype.link.apply(this, arguments);
  return link.replace("<a", "<a target='_blank'");
};
marked.setOptions({
  renderer: renderer
});

function addMessage(e) {
  // non ricaricare la pagina quando viene premuto INVIO nel campo di input
  e.preventDefault();

  // recupera il messaggio dell'utente
  let userMessage = document.getElementById("user-message").value.trim();

  // non fare niente se il messaggio dell'utente è vuoto
  if (userMessage.length == 0) {
    return;
  }

  // crea l'elemento HTML per il messaggio dell'utente
  const userMessageElement = document.createElement("div");
  const userMessageClasses = userMessageElement.classList;
  userMessageClasses.add("message-bubble");
  userMessageClasses.add("user-message");
  userMessageElement.textContent = userMessage;

  // crea l'elemento HTML per il messaggio di caricamento
  const loadingMessageElement = document.createElement("div");
  const loadingMessageClasses = loadingMessageElement.classList;
  loadingMessageClasses.add("message-bubble", "loading-message");

  // crea l'elemento HTML per il loader
  const loaderElement = document.createElement("span");
  const loaderClasses = loaderElement.classList;
  loaderClasses.add("loader");

  // crea l'elemento HTML per il testo del loader
  const loaderTextElement = document.createElement("span");
  loaderTextElement.textContent = "Sto pensando...";

  // aggiungi il loader e il testo al messaggio di caricamento
  loadingMessageElement.appendChild(loaderElement);
  loadingMessageElement.appendChild(loaderTextElement);

  // recupera l'elemento HTML della chat
  const chatMessagesElement = document.getElementById("chat-messages");

  // aggiungi il messaggio dell'utente alla chat
  chatMessagesElement.appendChild(userMessageElement);

  // aggiungi il messaggio di caricamento alla chat
  chatMessagesElement.appendChild(loadingMessageElement);

  // scrolla la chat in basso
  chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;

  // codifica il messaggio dell'utente per l'invio al server (sostituisce spazi e caratteri speciali)
  const userMessageEncoded = encodeURI(userMessage);

  // invia il messaggio dell'utente al server e attendi la risposta
  fetch(apiUrl + "/" + userMessageEncoded)
    .then((response) => response.json())
    .then((data) => {
      // crea l'elemento HTML per il messaggio del bot
      const botMessageElement = document.createElement("div");
      const botMessageClasses = botMessageElement.classList;
      botMessageClasses.add("message-bubble");
      botMessageClasses.add("bot-message");
      htmlContent = marked.parse(data);
      botMessageElement.innerHTML = htmlContent;

      // rimuovi il messaggio di caricamento
      loadingMessageElement.remove();

      // aggiungi il messaggio del bot alla chat
      chatMessagesElement.appendChild(botMessageElement);

      // scrolla la chat in basso
      chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
    })
    .catch((error) => {
      console.error("Errore:", error);

      // crea l'elemento HTML per il messaggio di errore
      const errorMessageElement = document.createElement("div");
      const errorMessageClasses = errorMessageElement.classList;
      errorMessageClasses.add("message-bubble");
      errorMessageClasses.add("error-message");
      errorMessageElement.textContent = "Qualcosa è andato storto 😭";

      // rimuovi il messaggio di caricamento
      loadingMessageElement.remove();

      // aggiungi il messaggio del bot alla chat
      chatMessagesElement.appendChild(errorMessageElement);

      // scrolla la chat in basso
      chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
    });

  // pulisci il campo di input
  document.getElementById("user-message").value = "";
}
