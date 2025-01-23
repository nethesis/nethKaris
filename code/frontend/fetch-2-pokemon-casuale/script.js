// 1. Fai una fetch per ottenere la lista di tutti i Pokémon (limit=10000)
fetch("https://pokeapi.co/api/v2/pokemon?limit=10000")
  .then((response) => response.json())
  .then((data) => {
    // 2. Scegli un Pokémon casuale dalla lista (usa Math.random e data.results.length)
    const pokemonCasuale =
      data.results[Math.floor(Math.random() * data.results.length)];

    // 3. Fai un'altra fetch per ottenere i dettagli del Pokémon casuale (usa pokemonCasuale.url)
    fetch(pokemonCasuale.url)
      .then((response) => response.json())
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
      });
  });
