---
layout: cover
---

# Esercizi `fetch` 

---

# Esercizio 1: Caccia al Pokémon 

*   Useremo `fetch` e l'API PokéAPI: [https://pokeapi.co/](https://pokeapi.co/) per recuperare le informazioni su Pikachu
*   Apri `fetch-1-pokemon/pokemon.html` nel browser
*   Apri `fetch-1-pokemon/script.js` in Visual Studio Code
*   (continua nella prossima pagina)

---

# Esercizio 1: Caccia al Pokémon (2) ✏️

- Apri la console del browser (tasto F12, poi clicca il tab **Console**). Dovresti vedere "Risposta: Object"
- Clicca **Object** per vedere come è fatta la risposta dell'API
- Esamina il codice in `script.js`:
  - Esegue una richiesta `fetch` all'API di Pikachu.
  - Usa `.then` per convertire la risposta in formato JSON.
  - Usa un altro `.then` per mostrare i dati di Pikachu sulla console (`console.log(data)`).
  - Ora tocca a te: sotto l'immagine del pokemon, mostra sulla pagina web un paragrafo con indicato il peso del pokemon (Es: "Peso: 60"). Questo dato si trova nell'attributo `data.weight` della risposta dell'API

---

# Esercizio 2: Trova un Pokémon a caso ✏️

- Apri `fetch-2-pokemon-casuale/pokemon-casuale.html` nel browser
- Apri `fetch-2-pokemon-casuale/script.js` in Visual Studio Code
- Esamina il codice in `script.js`:
  - Esegue una richiesta `fetch` per recuperare i dati di 100 pokemon (`limit=100`)
  - Sceglie un Pokémon casuale dalla lista usando `Math.random()`
  - Esegue un'altra `fetch` usando l'URL del Pokémon casuale (`pokemonCasuale.url`)
  - Mostra nome e immagine del Pokémon casuale nella pagina (come nell'esercizio 1)

---

# Esercizio 3: Gestione degli Errori ✏️

* In questo esercizio devi solo esaminare il codice in `script.js`:
1.  Controlla se la risposta è `ok` (`response.ok`) *dentro il primo `.then`*.
2.  Se non è `ok`, lancia un errore con il codice di stato: `throw new Error("Errore HTTP! Stato: ${response.status}");`
3.  Usa `.catch()` per "catturare" e gestire gli errori

---

# Esercizio 3: Gestione degli Errori (2) ✏️

- Per simulare un errore di connessione assente:
  - Premi F12 sulla tastiera per aprire la console sviluppatori
  - Clicca il tab **Network**, poi **No throttling**, poi **Offline**
  - Premi F5 per ricaricare la pagina e ripetere la `fetch`, che ora fallirà
  - Ricordati di rimuovere lo stato **Offline** e reimpostare **No throttling** nella console sviluppatori!

<img src="/offline.png" class="mt-4 h-60" />
