---
layout: cover
---

# `fetch`: Il Postino del Web ✉️

---

# Ripasso: Il Browser come Messaggero 🚀

*   Chiediamo una pagina web (es. Google).
*   Il browser "chiama" il server. 
*   Il server invia HTML, CSS e JavaScript. 
*   Il browser mostra la pagina. ️

---

# `fetch`: Richieste Speciali ️📡

Invece di caricare *tutta* la pagina, `fetch` chiede *solo dati*.  È come mandare il messaggero a prendere un'informazione specifica. 

---

# Perché Usiamo `fetch` nel Chatbot? 🕵️‍♂️

1.  **Utente scrive:** "Ciao!" 
2.  **`fetch` invia:** Il messaggio all'AI. 
3.  **AI elabora:** Pensa a una risposta. 
4.  **`fetch` riceve:** La risposta dell'AI. 
5.  **Chatbot mostra:** "Ciao! Come posso aiutarti?" 

---

# Esempio Pratico ‍✍️

```javascript
fetch('[URL non valido rimosso]!')
  .then(response => response.json())
  .then(data => {
    console.log(data.risposta); // "Ciao! Come posso aiutarti?"
  });
```

---

# Analizziamo il Codice 🔍

* `fetch`('indirizzo'): "Chiama" il server.
* .then(...): "Quando arriva la risposta…". ⏳
* response.json(): Trasforma la risposta in dati comprensibili (JSON). ➡️
* data.risposta: Accede alla parte "risposta" dei dati.

---

# Chiamate Asincrone: L'Attesa Non è un Problema! ⏰

Normalmente, JavaScript esegue il codice riga per riga. ➡️⬇️

`fetch` è asincrono: non blocca l'esecuzione del resto del codice mentre aspetta la risposta. ⏳ 
Questo significa che la pagina web rimane reattiva anche durante l'attesa! ️

---

# Promise: La Promessa di una Risposta 🥶

Una Promise in JavaScript rappresenta il risultato (che arriverà in futuro) di un'operazione asincrona, come una chiamata a `fetch`. È come una "promessa" che il server risponderà.

* Pendente: La richiesta è stata inviata, ma non c'è ancora una risposta. ⏳
* Risolta (Fulfilled): La richiesta è andata a buon fine e abbiamo la risposta. ✅
* Rifiutata (Rejected): C'è stato un errore (es. il server non risponde). ❌

---

# .then: Cosa Fare "Quando..." ➡️ 😱

Il .then() si usa con le Promise. Serve a specificare cosa fare quando la Promise è "risolta" (cioè quando abbiamo la risposta). È come dire: "Quando arriva il pacco, aprilo e guarda cosa c'è dentro". ➡️

Esempio:

```javascript
fetch('indirizzo') // Crea una Promise
  .then(response => { // Cosa fare QUANDO la Promise è risolta
    console.log("Risposta arrivata!");
    return response.json(); // Prepara i dati per il prossimo .then
  })
  .then(data => { // Usa i dati
    console.log(data);
  });
```


---

# Gestione degli Errori: Essere Preparati a Tutto ⚠️

Cosa succede se il server non risponde? O se c'è un errore? Dobbiamo gestire queste situazioni

Usiamo .catch() per "catturare" gli errori:

```javascript 
fetch('indirizzo_sbagliato') // Indirizzo che non esiste
  .then(response => response.json())
  .then(data => {
    console.log(data); // Questo non verrà eseguito se c'è un errore
  })
  .catch(error => {
    console.error("Si è verificato un errore:", error); // Mostra l'errore nella console
    // Qui possiamo mostrare un messaggio di errore all'utente
    const messaggioErrore = document.createElement('div');
    messaggioErrore.textContent = "Errore di connessione. Riprova più tardi.";
    document.getElementById('chat-box').appendChild(messaggioErrore);
  });
```
---

# Codici di Stato HTTP: Un Linguaggio Universale 🌌

Quando il browser fa una richiesta con fetch, il server risponde con un codice di stato HTTP. Questi codici sono come dei "messaggi" standard che indicano se la richiesta è andata a buon fine o se c'è stato un errore.

* 200 OK: Tutto a posto! ✅
* 404 Not Found: Pagina non trovata. ❌
* 500 Internal Server Error: Errore del server. ⚙️

Possiamo controllare il codice di stato nella risposta:

```javascript
fetch('indirizzo')
    .then(response => {
        if (!response.ok) { // response.ok è true solo se il codice di stato è tra 200 e 299
            console.error(`Errore HTTP! Stato: ${response.status}`);
            throw new Error(`Errore HTTP! Stato: ${response.status}`); //  Serve a farlo catturare dal .catch
        }
        return response.json();
    })
    .then(data => { /* ... */ })
    .catch(error => { /* ... */ });
```

---

# Esempio Completo con Gestione degli Errori e Codici di Stato 📍

Ecco un esempio che mette insieme tutto:

```javascript
fetch('indirizzo')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Errore HTTP! Stato: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    const messaggioChat = document.createElement('div');
    messaggioChat.textContent = data.testo;
    document.getElementById('chat-box').appendChild(messaggioChat);
  })
  .catch(error => {
    console.error("Si è verificato un errore:", error);
    const messaggioErrore = document.createElement('div');
    messaggioErrore.textContent = "Errore di connessione. Riprova più tardi.";
    document.getElementById('chat-box').appendChild(messaggioErrore);
  });
```

----

# Riassunto Finale ✨

- `fetch` chiede dati al server.
- È `asincrono`: non blocca il codice. ⏳
- Le `Promise` rappresentano il risultato futuro.
- `.then` specifica cosa fare quando la Promise è risolta. ➡️
- `JSON` è il formato per i dati.
- Gestire gli errori è fondamentale!