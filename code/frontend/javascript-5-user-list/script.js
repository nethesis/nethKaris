// Funzione per aggiungere un nome alla lista
function aggiungiNome() {
  // Recupera il nome utente che hai inserito nel campo di input tramite l'id nel tag <input> del file index.html
  var nome = document.getElementById("...").value;

  // Controlla se il campo di input non è vuoto per proseguire
  if (nome) {
    // Recupera la lista esistente tramite l'id nel tag <ul> del file index.html
    var lista = document.getElementById("listaNomi");
    // Aggiunge il nome alla lista
    lista.innerHTML += "<li>" + nome + "</li>";
  }

  // Pulisci il campo di input
  document.getElementById("...").value = "";
}
