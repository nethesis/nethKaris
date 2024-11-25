---
layout: cover
---

# HTML 👨‍💻

---

# HTML

- HTML (HyperText Markup Language) è il linguaggio base per creare pagine web
- Definisce la **struttura** e il **contenuto** di un pagina web
  - ad es. titoli, paragrafi, immagini, link

<!-- Metafora dell'impalcatura della casa -->

---

# Tag HTML

- HTML usa dei **tag** (come `<p>`, `<h1>`, `<body>`) per strutturare il contenuto
- I tag spesso appaiono in coppia: tag di apertura e tag di chiusura
- Ogni tag può contenere altri tag figli: **struttura ad albero**
- Ogni pagina HTML è una struttura base con `<html>`, `<head>` e `<body>`
  - `<head>` contiene informazioni sulla pagina, ad es. il titolo
  - `<body>` contiene il contenuto effettivo che vedrà l'utente

---
layout: two-cols
---

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Titolo della pagina</title>
    </head>
    <body>
        <h1>Benvenut&#601;! Questo &egrave; un titolo</h1>
        <p>
            Questo &egrave; un paragrafo di testo. 
            Lorem ipsum dolor sit amet...
        </p>

        <div>
            <input type="text" />
            <button>Pulsante</button>
        </div>

        <a href="https://www.wikipedia.org/">
            Link a Wikipedia
        </a>

        <div>
            <img src="https://media.tenor.com/McPQygGOuXYAAAAi/gladgers-hacker-gers-guardians-of-galaxy.gif" alt="hacker" />
        </div>
    </body>
</html>
```

::right::

<img src="/html-1.png" />

---

# Tag principali

- `<h1>`, `<h2>` ... `<h6>`: Titoli di livello
- `<p>`: Paragrafo
- `<div>`: Contenitore generico. Usato anche per layout di stile
- `<span>`: Testo inline
- `<a href="...">`: Link ad un'altra pagina web
- `<img src="...">`: Immagine
- `<ul>`: Lista non ordinata
- `<ol>`: Lista ordinata
- `<li>`: Elemento della lista
- `<form>`: Modulo per compilare e inviare dati
- `<input>`: Campo di input
- `<button>`: Pulsante

---

# Attributi HTML

- Gli elementi HTML posso avere **attributi**
- Gli attributi forniscono informazioni aggiuntive agli elementi
- Vanno specificati nel tag iniziale dell'elemento
- Solitamente ogni attributo è costituito da una coppia nome/valore, es. `name="value"`

---

# Sintassi di tag HTML e attributi

<img src="/tag-syntax.png" />

---

# Attributi comuni

- `class`: usato per assegnare una classe CSS ad un elemento HTML e applicargli uno stile.

```html
<p class="important-text">C'era una volta...</p>
```

- `id`: usato per assegnare un identificativo univoco ad un elemento HTML. Utile per identificare un elemento in JavaScript.

```html
<input type="text" id="myTextInput" />
```

- `href`: attributo del tag `<a>` per specificare l'indirizzo di destinazione (URL).

```html
<a href="https://www.wikipedia.org/">Go to Wikipedia</a>
```

---

# Attributi comuni (2)

- `src`: attributo del tag `<img>` per specificare l'indirizzo dell'immagine da visualizzare.

```html
<img src="img_student.jpg">
```

- `alt`: usato per specificare il testo alternativo di un'immagine. Il testo alternativo viene mostrato al posto dell'immagine se l'immagine non è disponibile, ad es.:
  - errore nell'attributo `src`
  - connessione lenta
  - l'utente usa uno screen reader

```html
<img src="img_student.jpg" alt="Student wearing a jacket">
```

---
layout: cover
---

# CSS 🌈

---

# CSS

- CSS (Cascading Style Sheets) è il linguaggio base per decorare una pagina web
- Definisce lo **stile**, l'apparenza e il posizionamento di ogni elemento della pagina, ad es.:
  - Colore
  - Dimensione
  - Allineamento
  - Spaziatura rispetto ad altri elementi

---

# Regole CSS

- Una regola CSS è formata da un selettore e da un blocco di dichiarazioni
- In caso di regole in conflitto, vince la regola più specifica

```css
h1 {    /* selettore: applica la regola agli elementi "h1" (titoli) */
    color: green;   /* dichiarazione: colora il testo di verde */
    text-align: center;     /* dichiarazione: allinea il testo al centro */
    margin-bottom: 2rem;    /* dichiarazione: margine inferiore di 32 pixel */
}

.important-text {   /* applica la regola agli elementi con classe "important-text" */
    text-decoration: underline;     /* sottolineatura */
    font-weight: bold;      /* grassetto */
    color: blue;
}

p.important-text {   /* applica la regola SOLO ai paragrafi con classe "important-text" */
    color: red;
}

#myTextInput {  /* applica la regola all'elemento con ID "myTextInput" */
    background-color: yellow;
}
```

---

# Regole CSS (2)

- Il selettore usato più comunemente è il selettore di classe CSS

```html
<p class="important-text">C'era una volta...</p>
```

<div class="mb-4"></div>

```css
.important-text {
    text-decoration: underline;
    font-weight: bold;
    color: blue;
}
```

---

# Colori

In CSS, i colori vengono utilizzati per definire l'aspetto visivo degli elementi (es. testo, sfondi, bordi). Possono essere specificati in diversi modi:
- Colori per nome: `red`, `blue`, `green`, `black`, `white`, ecc.
- Colori RGB e RGBA: specifica i valori dei canali rosso, verde e blu da 0 a 255.
```css
color: rgb(255, 0, 0); /* Rosso */
color: rgb(0, 255, 0); /* Verde */
color: rgb(0, 0, 255); /* Blu */
color: rgb(255, 255, 0); /* Giallo */
color: rgb(128, 128, 128); /* Grigio */
```

- Colori esadecimali: colori composti da tre coppie: #RRGGBB (red, green, blue). Ogni coppia esadecimale va da `00` (più scuro) a `ff` (più chiaro)
```css
color: #ff0000; /* Rosso */
color: #00ff00; /* Verde */
color: #0000ff; /* Blu */
color: #ffff00; /* Giallo */
color: #333333; /* Grigio scuro */
color: #dddddd; /* Grigio scuro */
```

---

# Unità di misura

Le unità di misura vengono utilizzate per definire dimensioni (come larghezze, altezze, margini, dimensione del testo, ecc.).

- `px` (pixel): Misura fissa e precisa. `1px` è un punto sullo schermo
  - Es. `font-size: 16px;`
- `rem`: Misura migliore per creare layout scalabili. Solitamente `1rem` equivale a `16px`
  - Es. `margin-right: 2rem;`
- `%`: Relativa all'elemento HTML genitore nella struttura ad albero
  - Es: `width: 50%;` è metà della larghezza dell'elemento genitore.

---

# Proprietà `display`

Specifica il modo in cui sarà visualizzato l'elemento. Può assumere svariati valori, i principali sono:

- `inline`: l'elemento è posizionato sulla stessa linea degli altri elementi (come `<span>`), occupando solo lo spazio necessario. Eventuali proprietà `width` o `height` saranno ignorate
- `block`: mostra l'elemento su una nuova linea e di default occupa tutta la larghezza, come `<p>` e `<div>`
- `inline-block`: mostra l'elemento sulla stessa linea come `inline`, ma è possible impostare `width` e `height`
- `none`: l'elemento non appare e non sarà presente nell'albero HTML
- `flex`: mostra l'elemento come un contenitore flex di tipo block (ne parleremo nelle prossime lezioni)
- `inline-flex`: mostra l'elemento come un contenitore flex di tipo inline (ne parleremo nelle prossime lezioni)

---

# Usare le regole CSS in un pagina HTML

- Definire le regole CSS in un file `.css`
- Includere il file `.css` all'interno del tag `<head>` del codice HTML
  - Es. `<link rel="stylesheet" href="style.css" />`
- Assegnare agli elementi elementi HTML le classi CSS per applicargli stile

---

# Usare le regole CSS in un pagina HTML (2)

```css
/* style.css */
.important-text {
    text-decoration: underline;
    font-weight: bold;
}
...
```

<div class="mb-4"></div>

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Titolo della pagina</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    ...
    <p class="important-text">C'era una volta...</p>
  </body>
</html>
```

---
layout: image
image: /html-css.png
backgroundSize: contain
---

---

# Layout gerarchico

- Organizzare gerarchicamente i container in un layout di una pagina web è fondamentale per garantire una struttura logica e mantenibile
- Pensare ad ogni sezione della pagina come un contenitore
- Iniziare dalla struttura generale della pagina (header, contenuto principale, footer) e suddividere ciascun contenitore in sezioni più piccole
- Ogni contenitore potrà essere stilizzato con regole CSS

```html
<div class="container">
  ...
  <div class="chat">
    ...
  </div>
</div>
```

---
layout: image
image: /chatbot-html-frames.png
backgroundSize: contain
---

---

# Approfondimenti su HTML e CSS

- W3Schools: https://www.w3schools.com/
- Tutorial HTML: https://www.w3schools.com/html/html_intro.asp
- Esempi HTML: https://www.w3schools.com/html/html_examples.asp
- Tutorial CSS: https://www.w3schools.com/css/css_intro.asp
- Esempi CSS: https://www.w3schools.com/css/css_examples.asp
