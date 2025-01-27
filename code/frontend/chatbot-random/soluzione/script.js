let randomAnswers = [
  "Uhmm non lo so",
  "Scusa, non ho capito :(",
  "Boh! Vuoi sentire una barzelletta?",
  "Mah! Non so cosa dirti",
  "Non te lo posso dire"
];
let chatMessages = [];

function addMessage(e) {
  // non ricaricare la pagina quando viene premuto INVIO nel campo di input
  e.preventDefault();

  // recuperiamo il messaggio dell'utente
  let userMessage = document.getElementById("user-message").value;

  // non fare niente se il messaggio dell'utente è vuoto
  if (userMessage.length == 0) {
    return;
  }

  let messageObj = { type: "user-message", message: userMessage };

  // aggiungiamo il messaggio dell'utente all'array dei messaggi
  chatMessages.push(messageObj);

  // scegli una risposta casuale
  let randomIndex = Math.floor(Math.random() * randomAnswers.length);
  let botMessage = { type: "bot-message", message: randomAnswers[randomIndex] };
  // aggiungiamo il messaggio del bot all'array dei messaggi
  chatMessages.push(botMessage);

  // popoliamo la chat con i messaggi
  let chatElement = document.getElementById("chat-messages");
  chatElement.innerHTML = "";

  for (let i = 0; i < chatMessages.length; i++) {
    chatElement.innerHTML +=
      '<div class="' + chatMessages[i].type + '">' + chatMessages[i].message;
    ("</div>");
  }

  // pulisci il campo di input
  document.getElementById("user-message").value = "";
}
