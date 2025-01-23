---
layout: cover
---

# Esercizi JavaScript 💪

---
src: ../pages/exercise-0-setup.md
hide: false
---

---

# Esercizio 1: Variabili e operazioni base 🧮

1. Apri il file `javascript-1-variables/index.html` sul browser.
2. Modifica il file `javascript-1-variables/script.js` e:
   - Crea una variabile per il nome di un animale:

    ```js
    let animale = "cane";
    ```

   - Crea una variabile per il numero di zampe:

    ```js
    let zampe = 4;
    ```
   
   - Crea una variabile per il numero di animali totali:
     
     ```js
     let numeroAnimali = 2;
     ```

---

# Esercizio 1: Variabili e operazioni base 🧮 (2)

- Calcola la somma del totale delle zampe di due cani:

    ```js
    let totaleZampe = zampe * numeroAnimali;
    console.log("Totale zampe: " + totaleZampe);
    ```
    
3. Ricarica la pagina web e verifica il risultato nella console del browser (premi F12 sulla tastiera).

---

# Esercizio 2: Interazione con l'utente 🎤

1. Apri il file `javascript-2-prompt-alert/index.html` sul browser.
2. Modifica il file `javascript-2-prompt-alert/script.js`:
   - Chiedi all'utente il suo nome usando `prompt`:

    ```js
    let nome = prompt("Come ti chiami?");
    ```
   - Saluta l'utente con un messaggio personalizzato:

    ```js
    alert("Ciao, " + nome + "!");
    ```

---

# Esercizio 3: Condizioni (if/else) 🚦

1. Apri il file `javascript-3-conditions/index.html` sul browser.
2. Modifica il file `javascript-3-conditions/script.js`:
   - Chiedi all'utente la sua età:

    ```js
    let eta = prompt("Quanti anni hai?");
    ```
   - Usa una condizione per verificare se è maggiorenne:

    ```js
    if (eta >= 18) {
    alert("Sei maggiorenne!");
    } else {
    alert("Sei minorenne!");
    }
    ```

---

# Esercizio 4: Cicli e array 🔁

1. Apri il file `javascript-4-loops/index.html` sul browser.
2. Modifica il file `javascript-4-loops/index.html`.
   - Crea un array con i tuoi 3 colori preferiti:

    ```js
    let colori = ["rosso", "verde", "blu"];
    ```

   - Usa un ciclo for per stampare ogni colore nella console del browser (premi F12 sulla tastiera):

    ```js
    for (let i = 0; i < colori.length; i++) {
      console.log(colori[i]);
    }
    ```

---

  # Esercizio 5: Gestione di una lista di nomi 🧑

  1. Apri il file `javascript-5-user-list/index.html` sul browser.

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

  # Esercizio 5: Gestione di una lista di nomi 🧑 (2)

  2. Modifica il file `javascript-5-user-list/script.js`:

     - Crea la funzione `aggiungiNome()`: 

      ```js
      function aggiungiNome() {}
      ```

     - Associa il nome al valore del text input: 

      ```js
      let nome = document.getElementById("nameInput").value;
      ```

     - Recupera la lista già esistente e aggiungi il nome:

      ```js
      let lista = document.getElementById("listaNomi");
      lista.innerHTML += "<li>" + nome + "</li>";
      ```

     - Svuota il campo di input dopo aver aggiunto il nome:

      ```js
      document.getElementById("nameInput").value = "";
      ```

---

  # Esercizio 6 : Lavoriamo con gli oggetti 🛠️

  1. Apri il file `javascript-6-object/index.html` sul browser.
  2. Modifica il file `javascript-6-object/script.js`:

     - Dichiara un oggetto persona che contenga nome, eta, citta, e hobby: 

       ```js
         let persona = {
            nome: '',
            eta: '',
            citta: '',
            hobby: [],
         };
       ```

     - Aggiungi almeno un elemento all'array hobby:

         ```js
         persona.hobby.push(...);
         ```

---

# Esercizio 6 : Lavoriamo con gli oggetti 🛠️ (2)

- Stampa in console il nome e la città della persona: 

    ```js
    console.log('Nome: ' + ...);
    ```


- Stampa in console l'array hobby ciclando su tutti gli elementi:

    ```js
    for (let i = 0; i < persona.hobby.length; i++) {
      ...
    }
    ```

- Stampa in console il primo elemento dell'array hobby:

    ```js
    console.log(persona.hobby[0]);
    ```

- Modifica il valore di "città" dell'oggetto persona

    ```js
    persona.citta = ...;
    ```
