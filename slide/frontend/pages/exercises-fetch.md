---
layout: cover
---

# Esercizi `fetch` 

---

# Esercizio 1: Caccia al Pokémon 

Recuperiamo informazioni su Pikachu usando `fetch`!

*   Apri `fetch-1-pokemon/pokemon.html` nel browser.
*   Apri `fetch-1-pokemon/script.js` in Visual Studio Code.
*   Useremo l'API PokéAPI: [https://pokeapi.co/](https://pokeapi.co/).
*   Endpoint: `/api/v2/pokemon/pikachu`.

---

# Esercizio 1: Caccia al Pokémon (2) ✏️

Scrivi il codice in `script.js` per:

1.  Fare una richiesta `fetch` all'API di Pikachu.
2.  Usare `.then` per gestire la risposta e convertirla in JSON.
3.  Usare un altro `.then` per mostrare i dati di Pikachu nella console (`console.log(data)`).

Apri la console del browser (tasto destro -> "Ispeziona" -> "Console"). Dovresti vedere i dati JSON.

---

# Esercizio 2: Trova un Pokémon a caso 

Mostriamo un Pokémon casuale!

*   Endpoint per la lista di tutti i Pokémon: `https://pokeapi.co/api/v2/pokemon?limit=10000`.

---

# Esercizio 2: Trova un Pokémon a caso (2) ✏️

Modifica il codice in `script.js` per:

1.  Fare una `fetch` per ottenere la lista di Pokémon.
2.  Scegliere un Pokémon casuale dalla lista (usa `Math.random()` e `data.results.length`).
3.  Fare *un'altra* `fetch` usando l'URL del Pokémon casuale (`pokemonCasuale.url`).
4.  Mostrare nome e immagine del Pokémon casuale nella pagina (come nell'esercizio 1).

---

# Esercizio 3: Gestione degli Errori ⚠️

Aggiungiamo la gestione degli errori!

---

# Esercizio 3: Gestione degli Errori (2) ✏️

Modifica il codice in `script.js` per:

1.  Controllare se la risposta è `ok` (`response.ok`) *dentro il primo `.then`*.
2.  Se non è `ok`, lanciare un errore con il codice di stato: `throw new Error(\`Errore HTTP! Stato: ${response.status}\`);`.
3.  Usare `.catch()` per "catturare" gli errori.

---

# Riassunto degli esercizi ✅

*   Richieste `fetch` a un'API pubblica.
*   Gestione risposte JSON.
*   Mostrare dati nella pagina.
*   Gestione degli errori (fondamentale!).
