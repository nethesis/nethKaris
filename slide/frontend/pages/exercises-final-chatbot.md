---
layout: cover
---

# Chatbot finale 🤖

---
src: ../pages/exercise-0-setup.md
hide: false
---

---

# Esercizio 1: Elenco gite conosciute 🧳

- Apri il file `final-chatbot/index.html` sul browser (Chrome, Edge, Firefox...) per vedere com'è fatta la pagina web
- Apri il file anche su Visual Studio Code
- Modifica il codice HTML aggiungendo un messaggio all'inizio della conversazione che elenca le gite conosciute:
  - Aggiungi `<div class="message-bubble">` all'interno del `div` con ID `chat-messages`
  - Aggiungi un paragrafo (`<p>...</p>`) con all'interno il testo `Ciao! Questo è l'elenco delle gite di cui sono a conoscenza:`
  - (continua nella prossima pagina)

---

# Esercizio 1: Elenco gite conosciute 🧳 (2)

- Sotto al paragrafo, aggiungi il seguente elenco puntato:

```html
<ul style="list-style-position: inside">
  <li>Firenze 05/2024</li>
  <li>Parma 2023</li>
  <li>Mantova 2024</li>
  <li>Campania 2023</li>
  <li>Grecia 2022</li>
  <li>Firenze 02/2024</li>
  <li>Vienna e Monaco 2023</li>
  <li>Museo del Balì 2023</li>
  <li>Antibes 2024</li>
</ul>
```

- La AI estrae i dati delle gite prendendoli dal sito su cui hanno lavorato i vostri compagni del gruppo Gestione documenti: http://karis.cloud.neth.eu/blogger-gb-news/
- Ricorda di chiudere correttamente tutti i tag HTML aperti

---

# Esercizio 2: Aggiungi la risposta del bot alla chat 💬

- Su Visual Studio Code apri il file `final-chatbot/script.js`
- Esamina il codice e cerca di capirlo, leggendo i commenti presenti nel codice
- Modifica il file per aggiungere la risposta del bot alla chat. Prendi spunto guardando come è stato aggiunto il messaggio dell'utente alla chat (Cerca l'istruzione sotto il commento `// aggiungi il messaggio dell'utente alla chat`)
- Aggiungi un'istruzione Javascript per scrollare automaticamente la chat in basso dopo aver aggiunto il messaggio del bot alla chat. Questo succede già quando l'utente invia il suo messaggio, puoi copiare il codice da lì

---

# Esercizio 3: Gestione degli errori ❌

- Su Visual Studio Code apri il file `final-chatbot/script.js`
- Il codice di gestione degli errori è in buona parte già presente (il codice sotto `catch`), ma è necessario aggiungere il messaggio di errore alla chat, come hai già fatto con il messaggio del bot
- Per simulare un errore di connessione assente:
  - Premi F12 sulla tastiera per aprire la console sviluppatori
  - Clicca il tab **Network**, poi **No throttling**, poi **Offline** (continua nella prossima pagina)

<img src="/offline.png" class="h-60" />

---

# Esercizio 3: Gestione degli errori ❌ (2)

- Dopo aver il messaggio di errore alla chat, chiedendo qualcosa al chatbot dovrebbe rispondere così:

<img src="/chatbot-error.png" class="h-96" />

---

# Esercizio 4: Cambia i colori del chatbot 🎨

- Su Visual Studio Code apri il file `final-chatbot/style.css`
- Cambia i colori della chat modificando le regole CSS
- Complimenti, hai sistemato e personalizzato il chatbot!

<div class="mt-16 text-9xl text-center">🎉</div>
