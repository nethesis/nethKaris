// Diario gite Karis: http://karis.cloud.neth.eu/blogger-gb-news/

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
  loadingMessageClasses.add("message-bubble");

  // crea l'elemento HTML per il loader
  const loaderElement = document.createElement("span");
  const loaderClasses = loaderElement.classList;
  loaderClasses.add("loader");

  // aggiungi il loader al messaggio di caricamento
  loadingMessageElement.appendChild(loaderElement);

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
  fetch("http://karis.sf.nethserver.net:8888/generate/" + userMessageEncoded)
    .then((response) => response.json())
    .then((data) => {
      console.log("Risposta:", data);

      // crea l'elemento HTML per il messaggio del bot
      const botMessageElement = document.createElement("div");
      const botMessageClasses = botMessageElement.classList;
      botMessageClasses.add("message-bubble");
      botMessageClasses.add("bot-message");
      botMessageElement.textContent = data;

      // rimuovi il messaggio di caricamento
      loadingMessageElement.remove();

      // aggiungi il messaggio del bot alla chat
      // ...

      // scrolla la chat in basso
      // ...
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
      // ...

      // scrolla la chat in basso
      chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
    });

  // pulisci il campo di input
  document.getElementById("user-message").value = "";
}
