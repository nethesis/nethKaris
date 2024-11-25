---
layout: cover
---

# Esercizi JavaScript 💪

---

# Esercizio 1: Variabili e operazioni base 🧮

1. Apri il file javascript-1-variables/index.html sul browser.
2. Modifica il file javascript-1-variables/script.js e:
  
  - Crea una variabile per il nome di un animale:

  ```bash
  let animale = "cane";
  ```

  - Crea una variabile per il numero di zampe:

  ```bash
  let zampe = "cane";
  ```

  - Calcola la somma del totale delle zampe di due cani:

  ```bash
  let totaleZampe = zampe * 2;
  console.log("Totale zampe: " + totaleZampe);
  ```
3. Ricarica la pagina web e verifica il risultato nella Console del browser.

---

# Esercizio 2: Interazione con l'utente 🎤

1. Apri il file javascript-2-prompt-alert/index.html sul browser.
2. Modifica il file javascript-2-prompt-alert/script.js:
  - Chiedi all'utente il suo nome usando prompt:

  ```bash
  let nome = prompt("Come ti chiami?");
  ```
  - Saluta l'utente con un messaggio personalizzato:

  ```bash
  alert("Ciao, " + nome + "!");
  ```

---

# Esercizio 3: Condizioni (if/else) 🚦

1. Apri il file javascript-3-conditions/index.html sul browser.
2. Modifica il file javascript-3-conditions/script.js:
  - Chiedi all'utente la sua età:

  ```bash
  let eta = prompt("Quanti anni hai?");
  ```
  - Usa una condizione per verificare se è maggiorenne:

  ```bash
  if (eta >= 18) {
   alert("Sei maggiorenne!");
  } else {
   alert("Sei minorenne!");
  }
  ```

---

# Esercizio 4: Cicli e array 🔁

1. Apri il file javascript-4-loops/index.html sul browser.
2. Apri il file javascript-4-loops/index.html sul browser.
  - Crea un array con i tuoi 3 colori preferiti:

  ```bash
  let colori = ["rosso", "verde", "blu"];
  ```

  - Usa un ciclo for per stampare ogni colore nella Console:

  ```bash
  for (let i = 0; i < colori.length; i++) {
   console.log(colori[i]);
  }
  ```

---

  # Esercizio 5 (1/2): Gestione di una lista di nomi 🧑

  1. Apri il file javascript-5-user-list/index.html sul browser.

  - Aggiungi un text input alla tua pagina:

  ```html
  <input type="text" id="esempio" placeholder="inputFieldEsempio">
  ```

  - Aggiungi un pulsante che permetterà l'aggiunta del nome tramite il richiamo della funzione `aggiungiNome()`: 

  ```html
  <button onclick="aggiungiNome()">Aggiungi</button>
  ```

  - Aggiungi una lista sotto il pulsante contente l'array dei nomi:

  ```html
  <ul id="listaNomi"></ul>
  ```

---

  # Esercizio 5 (2/2): Gestione di una lista di nomi 🧑

  2. Modifica il file javascript-5-user-list/script.js:

  - Crea la funzione aggiungiNome(): 

  ```bash
  function aggiungiNome() {}
  ```

  - Associa il nome al valore del text input: 

  ```bash
  var nome = document.getElementById("nameInput").value;
  ```

  - Recupera la lista già esistente:

  ```bash
  var lista = document.getElementById("listaNomi");
  ```

  - Recupera la lista già esistente e aggiungi il nome:

  ```bash
  var lista = document.getElementById("listaNomi");
  lista.innerHTML += "<li>" + nome + "</li>";
  ```

  - Svuota il campo di input dopo aver aggiunto il nome:

  ```bash
  document.getElementById("nameInput").value = "";
  ```
