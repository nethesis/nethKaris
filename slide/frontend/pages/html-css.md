# HTML

- HTML (HyperText Markup Language) è il linguaggio base per creare pagine web
- Definisce la struttura e il suo contenuto di un pagina web, ad es. titoli, paragrafi, immagini, link
- ? Impalcatura di una casa

---

# Tag HTML

- HTML usa dei "tag" (come `<p>`, `<h1>`, `<body>`) per strutturare il contenuto
- I tag spesso appaiono in coppia: tag di apertura e tag di chiusura
- Ogni pagina HTML ha una struttura base con `<html>`, `<head>` e `<body>`
  - `<head>` contiene informazioni sulla pagina
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

- `<h1>`, `<h2>` ... `<h6>`: Titoli di diverso livello
- `<p>`: Paragrafo
- `<div>`: Contenitore generico
- `<span>`: Testo inline
- `<a href="">`: Link
- `<img src="">`: Immagini
- `<ul>`: Lista non ordinata
- `<ol>`: Lista ordinata
- `<li>`: Elemento della lista
- `<form>`: Modulo per compilare e inviare dati
- `<input>`: Campo di input
- `<button>`: Pulsante

---

