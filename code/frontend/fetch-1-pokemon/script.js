// 1. Usa fetch per fare una richiesta all'API di Pikachu:
// https://pokeapi.co/api/v2/pokemon/pikachu
fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
  // 2. Usa .then per gestire la risposta e convertirla in JSON
  .then((response) => {
    return response.json();
  })
  // 3. Usa un altro .then per accedere ai dati e mostrare nome e immagine
  .then((data) => {
    const pokemonContainer = document.getElementById("pokemon-container");
    const nomePokemon = document.createElement("h2");
    //Imposta il testo dell'h2 con il nome del pokemon
    nomePokemon.textContent = data.name;

    pokemonContainer.appendChild(nomePokemon);
    const immaginePokemon = document.createElement("img");
    //Imposta l'src dell'immagine del pokemon
    immaginePokemon.src = data.sprites.front_default;
    immaginePokemon.alt = `Immagine di ${data.name}`;
    pokemonContainer.appendChild(immaginePokemon);
  });
