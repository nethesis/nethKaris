// 1. Fai una fetch per ottenere la lista di tutti i Pokémon (limit=10000)
fetch("https://pokeapi.co/api/v2/pokemon?limit=10000")
  .then((response) => {
    // 2. Controlla se la risposta è ok (response.ok)
    if (!response.ok) {
      // 3. Se non è ok, lancia un errore con il codice di stato: throw new Error(...)
      throw new Error(`Errore HTTP! Stato: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    const pokemonCasuale =
      data.results[Math.floor(Math.random() * data.results.length)];

    return fetch(pokemonCasuale.url); // Ritorna la promise della seconda fetch
  })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Errore HTTP! Stato: ${response.status}`);
    }
    return response.json();
  })
  .then((dettagliPokemon) => {
    // 4. Mostra il nome e l'immagine del Pokémon nel div con id "pokemon-container"
    const pokemonContainer = document.getElementById("pokemon-container");
    const nomePokemon = document.createElement("h2");
    nomePokemon.textContent = dettagliPokemon.name;
    pokemonContainer.appendChild(nomePokemon);
    const immaginePokemon = document.createElement("img");
    immaginePokemon.src = dettagliPokemon.sprites.front_default;
    immaginePokemon.alt = `Immagine di ${dettagliPokemon.name}`;
    pokemonContainer.appendChild(immaginePokemon);
  })
  .catch((error) => {
    // 5. Gestisci l'errore e mostra un messaggio all'utente nel div con id "pokemon-container"
    const pokemonContainer = document.getElementById("pokemon-container");
    const messaggioErrore = document.createElement("p");
    messaggioErrore.textContent =
      "Si è verificato un errore nel caricamento dei Pokémon: " + error.message;
    pokemonContainer.appendChild(messaggioErrore);
  });
