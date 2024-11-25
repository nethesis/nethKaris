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

  // Dopo aver aggiunto il nome pulisci l'id del campo di input per permettere all'utente di inserire un nuovo nome ( id del tag <input> del file index.html)
  document.getElementById("...").value = "";
}
