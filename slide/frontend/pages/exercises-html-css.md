---
layout: cover
---

# Esercizi HTML & CSS 💪

---
src: ../pages/exercise-0-setup.md
hide: false
---

---

# Esercizio 1: Sostituiamo un'immagine 🖼️

Cambia il percorso di un'immagine in una pagina web

- Su Visual Studio Code apri il file `html-1-change-image/change-image.html`
- Apri lo stesso file sul browser (Chrome, Edge, Firefox...)
- Cerca un'immagine sul web (es. su [Google Immagini](https://www.google.com/imghp)) e scaricala sul computer
- Sposta il file dell'immagine dentro la cartella `html-1-change-image/`
- Modifica l'immagine contenuta in `change-image.html` modificando l'attributo `src` del tag `img`, ad esempio `<img src="./nomeImmagine.jpg" />`. I caratteri `./` indicano che il file `nomeImmagine.jpg` si trova nella stessa cartella del file attuale (`test.html`)
- Ricarica la pagina `change-image.html` sul browser per vedere le tue modifiche (F5 sulla tastiera)

---

# Esercizio 2: Cambiamo lo stile 🎨

Modifica lo stile di una pagina web

- Su Visual Studio Code apri il file `html-2-change-style/change-style.html`
- Apri il file `html-2-change-style/change-style.html` sul browser (Chrome, Edge, Firefox...)
- Su Visual Studio Code, esamina la struttura HTML di `change-style.html` e le classi CSS utilizzate dai vari tag
- Su Visual Studio Code apri anche il file `html-2-change-style/style.css`
- Cambia lo stile della pagina secondo i tuoi gusti, modificando il file `style.css` per cambiare:
  - i colori del testo (`color`)
  - i colori di sfondo (`background-color`)
  - l'allineamento del testo (`text-align`)
  - l'arrotondamento del pulsante
  - margini e padding
- Ricarica la pagina `change-style.html` sul browser per vedere le tue modifiche (F5 sulla tastiera)

---

# Esercizio 3: I miei preferiti 🏆

Crea una pagina web in cui mostrare una classifica: ad esempio i tuoi 3 film preferiti, oppure le tue 3 canzoni preferite, oppure i tuoi 3 libri preferiti ecc.

- Su Visual Studio Code apri il file `html-3-favorites/favorites.html`
- Apri lo stesso file anche sul browser (Chrome, Edge, Firefox...)
- Aggiungi un titolo nella pagina web inserendo un tag `<h1>` all'interno del tag `<body>`, ad es. "I miei 3 film preferiti"
- Ricarica la pagina web sul browser per vedere le tue modifiche (F5 sulla tastiera)
- Aggiungi un titolo alla pagina inserendo un tag `<title>...</title>` all'interno del tag `<head>`. Il titolo dovrà apparire nella scheda del browser
- Aggiungi un titolo `<h2>` sotto il titolo H1 e scrivi il titolo del primo classificato (es. il nome del tuo film preferito)
- Aggiungi un paragrafo `<p>` sotto il titolo H2 e descrivi brevemente perché ti è piaciuto
- (continua nella prossima pagina)

---

# Esercizio 3: I miei preferiti (2) 🏆

- Aggiungi un link `<a href="...">` sotto il titolo H2 che porta alla pagina Wikipedia del film. Per aprire il link in una nuova scheda del browser, usare l'attributo `target="_blank"`.
  - Ad esempio: `<a href="https://en.wikipedia.org/wiki/Interstellar_(film)" target="_blank">Apri su Wikipedia</a>`
- Aggiungi un titolo `<h2>` sotto il link precedente per il secondo classificato
- Aggiungi un paragrafo `<p>` per descrivere il secondo classificato
- Aggiungi un link a Wikipedia per il secondo classificato
- Aggiungi titolo, paragrafo e link anche per il terzo classificato
- (continua nella prossima pagina)

---

# Esercizio 3: I miei preferiti (3) 🏆

- Aggiungi stile alla pagina
  - Aggiungi l'attributo `class="nomeClasse"` agli elementi a cui vuoi applicare qualche stile
    - Ad es: `<h1 class="mainTitle">I miei film preferiti</h1>`
  - Crea un file `style.css` nella stessa cartella del file HTML (`html-3-favorites`)
  - Includi il file `.css` all'interno del tag `<head>` del codice HTML per caricare lo stile nella pagina
    - Es: `<link rel="stylesheet" href="style.css" />`
  - Scrivi nel file `style.css` le regole di stile, ad es:

```css
.mainTitle {
  text-align: center;
  color: light;
}

.movieDescription {
    ...
}
```

---

# Esercizio 4: Chatbot 🤖

Aggiungi stile ad una conversazione con un chatbot

- Su Visual Studio Code apri il file `html-4-chatbot/chatbot.html`
- Apri lo stesso file anche sul browser (Chrome, Edge, Firefox...)
- Crea un file `style.css` nella stessa cartella del file HTML (`html-4-chatbot`)
- Includi il file `.css` all'interno del tag `<head>` del codice HTML
  - Es: `<link rel="stylesheet" href="style.css" />`
- Scrivi nel file `style.css` le regole di stile per ottenere uno stile simile a quello della pagina successiva

---
layout: image
image: /chatbot-html.png
backgroundSize: contain
---

---
layout: image
image: /chatbot-html-frames.png
backgroundSize: contain
---
---

# Esercizio 4: Chatbot 🤖 (4)

Suggerimenti per il file di stile

```css
body {
  ...
}

.container {
  max-width: 40rem;
  margin: auto; /* centra orizzontalmente il contenitore */
}

.user-message {
  display: inline-block;
  ...
}

.message-input {
  width: 79%;
  font-size: 1rem;
  border: none;
  ...
}
...
```
