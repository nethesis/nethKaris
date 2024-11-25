---
layout: cover
---

# Esercizio HTML, CSS & JavaScript 💪

---

# Esercizio finale: Lista della spesa 📝

Crea una semplice webapp per la lista della spesa

- Su Visual Studio Code apri il file `javascript-7-grocery-list/grocery-list.html`
- Apri lo stesso file anche sul browser
- Aggiungi un titolo alla pagina inserendo un tag `<title>...</title>` all'interno del tag `<head>`. Il titolo dovrà apparire nella scheda del browser
- Aggiungi un `<div>` con classe CSS `container` all'interno del `<body>`
- (continua nella prossima pagina)

---

# Esercizio finale: Lista della spesa 📝 (2)

- All'interno del `<div>` aggiungi:
  - un titolo `<h1>` "Grocery list" (lista della spesa)
  - un elenco `<ul>` con ID `grocery-list`
  - un campo di testo `<input type="text" />` con ID `new-item`
  - un campo di testo numerico con valore iniziale "1":
  ```html
  <input type="number" id="new-quantity" value="1" />
  ```
  - un pulsante con testo "Add"
- (continua nella prossima pagina)

---

# Esercizio finale: Lista della spesa 📝 (3)

- Importa il file `script.js` come ultimo elemento del `<body>`, es:

```html
...
<body>
  ...
  <script src="script.js"></script>
</body>
...
```

- Completa il codice nel file `script.js`:
  - L'utente può aggiungere elementi alla lista della spesa scrivendo descrizione (ad es. "Farina") e quantità (ad es. "3") nelle due caselle di input e cliccando il pulsante "Add"
  - (continua nella prossima pagina)

---

# Esercizio finale: Lista della spesa 📝 (4)

- La funzione `addItem` deve:
  - Recuperare gli elementi HTML della descrizione e della quantità digitate dall'utente, usando `getElementById`
  - Aggiungere all'array `groceryList` un oggetto con attributi `description` e `quantity`
  - Recuperare l'elemento HTML relativo all'elenco `<ul>`, usando `getElementById`
  - Svuotare il contenuto HTML dell'elenco, settando `innerHTML = ""`
  - Eseguire un ciclo `for` su tutti gli elementi dell'array `groceryList`, aggiungendo ogni volta all'`innerHTML` dell'elenco un elemento `<li>` che riporti la descrizione e la quantità dell'elemento, es:

```js
list.innerHTML += "<li>" + groceryList[i].description + " - " + groceryList[i].quantity + "</li>";
```

  - Resettare le due caselle di testo, impostando una stringa vuota per la descrizione e "1" per la quantità
  - (continua nella prossima pagina)

---

# Esercizio finale: Lista della spesa 📝 (5)

- Aggiungi stile alla pagina
  - Aggiungi l'attributo `class="nomeClasse"` agli elementi a cui vuoi applicare stile
  - Crea un file `style.css` nella stessa cartella del file HTML (`javascript-7-grocery-list`)
  - Includi il file `.css` all'interno del tag `<head>` del codice HTML per caricare lo stile nella pagina
    - Es: `<link rel="stylesheet" href="style.css" />`
  - Scrivi nel file `style.css` le regole di stile, usando colori, margini, padding e le altre proprietà CSS secondo i tuoi gusti
