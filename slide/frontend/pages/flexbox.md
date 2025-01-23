---
layout: cover
---

# Come sono andate le vacanze? 🎅

---
layout: cover
---

# Avete fatto gli esercizi per le vacanze? 🧐

---
layout: cover
---

# Relatori, come va la relazione? 📝


---

# Quali attrezzi ci mancano per costruire la UI finale del chatbot? 🛠️

- Flexbox: strumento di layout CSS per impaginare facilmente gli elementi nella pagina web del chatbot.
- `fetch`: istruzione Javascript per eseguire chiamate di rete. Ci servirà per inviare i messaggi dell'utente alla AI e ricevere le sue risposte

---
layout: cover
---

# Flexbox 💪📦

---

# Ripasso: proprietà CSS `display`

Specifica il modo in cui sarà visualizzato l'elemento. Può assumere svariati valori, i principali sono:

- `block`: mostra l'elemento su una nuova linea e di default occupa tutta la larghezza, come `<p>` e `<div>`. Eventuali proprietà `width` o `height` saranno rispettate
- `inline`: l'elemento è posizionato sulla stessa linea degli altri elementi (come `<span>`), occupando solo lo spazio necessario. Eventuali proprietà `width` o `height` saranno ignorate
- `inline-block`: mostra l'elemento sulla stessa linea come `inline`, ma è possible impostare `width` e `height`
- `none`: l'elemento non appare e non sarà presente nell'albero HTML
- `flex`: mostra l'elemento come un contenitore flex di tipo block
- `inline-flex`: mostra l'elemento come un contenitore flex di tipo inline

---
layout: image
image: /display-property.png
backgroundSize: contain
---

---

# Flexbox


- È uno strumento di layout CSS che semplifica l'allineamento, la distribuzione e il ridimensionamento degli elementi all'interno di un contenitore
- Si adatta facilmente a spazi disponibili, sia in direzione orizzontale che verticale
- Utile per costruire layout complessi come barre di navigazione e photo gallery, ma non solo

---

# Flexbox (2)

- Immagina di avere una scatola (contenitore) con degli oggetti (elementi) dentro. Come vogliamo disporre questi oggetti all'interno del contenitore?
  - In riga o in colonna: puoi decidere se gli elementi devono essere disposti uno accanto all'altro (orizzontalmente) o uno sopra l'altro (verticalmente) usando `flex-direction`
  - Allineamento: puoi centrare gli elementi, spostarli a destra, a sinistra o distribuire lo spazio tra di loro con proprietà come `justify-content` (per l'allineamento orizzontale) e `align-items` (per l'allineamento verticale)
  - Distanza: puoi specificare la distanza minima tra gli elementi usando le proprietà `gap`, `row-gap` e `column-gap`

---
layout: two-cols-header
---

# flex-direction

::left::

<img class="w-96" src="/flex-direction.png" />

::right::

```css
.container {
  display: flex;
  flex-direction: row | row-reverse | column | column-reverse;
}
```

Il carattere `|` qui sopra significa "oppure", va specificato un solo valore tra quelli elencati.

---
layout: two-cols-header
---

# justify-content

::left::

<img class="h-110" src="/justify-content.png" />

::right::

```css
.container {
  display: flex;
  justify-content: flex-start | flex-end | center | 
    space-between | space-around | space-evenly
}
```

Il carattere `|` qui sopra significa "oppure", va specificato un solo valore tra quelli elencati.

---
layout: two-cols-header
---

# align-items

::left::

<img class="h-110" src="/align-items.png" />

::right::

```css
.container {
  display: flex;
  align-items: stretch | flex-start | flex-end | 
    center | baseline
}
```

Il carattere `|` qui sopra significa "oppure", va specificato un solo valore tra quelli elencati.

---
layout: two-cols-header
---

# gap

::left::

<img class="h-110" src="/gap.png" />

::right::

```css
.container {
  display: flex;
  gap: 1rem; /* È possibile specificare
    qualunque dimensione, es. 2.5rem, oppure 20px, ecc */
}
```

Oppure, specificando sia il gap tra le righe che quello tra le colonne:

```css
.container {
  display: flex;
  gap: 1rem 2rem; /* row-gap column gap */
}
```

---

# Approfondimenti su Flexbox

- Guida CSS-TRICKS: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- Guida MDN: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox
