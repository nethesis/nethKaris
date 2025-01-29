// usa fetch per ottenere una lista di 100 Pokémon
fetch("https://pokeapi.co/api/v2/pokemon?limit=100")
  .then((response) => response.json())
  .then((data) => {
    // scegli un Pokémon casuale dalla lista usando Math.random
    const pokemonCasuale =
      data.results[Math.floor(Math.random() * data.results.length)];

    // esegui un'altra fetch per ottenere i dettagli del Pokémon casuale
    fetch(pokemonCasuale.url)
      .then((response) => response.json())
      .then((dettagliPokemon) => {
        // mostra il nome e l'immagine del Pokémon nel div con id "pokemon-container"
        const pokemonContainer = document.getElementById("pokemon-container");
        const nomePokemon = document.createElement("h2");
        nomePokemon.textContent = dettagliPokemon.name;
        pokemonContainer.appendChild(nomePokemon);
        const immaginePokemon = document.createElement("img");
        immaginePokemon.src = dettagliPokemon.sprites.front_default;
        immaginePokemon.alt = `Immagine di ${dettagliPokemon.name}`;
        pokemonContainer.appendChild(immaginePokemon);
      });
  });
