// Usa fetch per fare una richiesta all'API di Pikachu
fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
  // Usa .then per gestire la risposta e convertirla in JSON
  .then((response) => {
    return response.json();
  })
  // Usa un altro .then per accedere ai dati e mostrare nome e immagine
  .then((data) => {
    // stampa su console la risposta dell'API
    console.log("Risposta:", data);

    // recupera l'elemento HTML per il contenitore del pokemon
    const pokemonContainer = document.getElementById("pokemon-container");

    // crea un elemento h2 per il nome del pokemon
    const nomePokemon = document.createElement("h2");
    // imposta il testo dell'h2 con il nome del pokemon
    nomePokemon.textContent = data.name;
    pokemonContainer.appendChild(nomePokemon);

    // crea un elemento img per l'immagine del pokemon
    const immaginePokemon = document.createElement("img");
    // imposta l'src dell'immagine del pokemon
    immaginePokemon.src = data.sprites.front_default;
    immaginePokemon.alt = `Immagine di ${data.name}`;
    pokemonContainer.appendChild(immaginePokemon);

    // crea un elemento p per il peso del pokemon
    // ...
  });
