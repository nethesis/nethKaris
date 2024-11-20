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

# Esempio di pagina HTML

```html
<!DOCTYPE html>
<html>
<head>
    <title>La mia prima pagina</title>
</head>
<body>
    <h1>Benvenuto! Questo è un titolo</h1>
    <p>Questo è un paragrafo di testo. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

    <ul>
        <li>Elemento lista 1</li>
        <li>Elemento lista 2</li>
        <li>Elemento lista 3</li>
    </ul>

    <a href="https://www.wikipedia.org/">Questo è un link</a>
</body>
</html>
```

//// aprire html_example_1

---
layout: image-right
image: https://cover.sli.dev
---

# Code

Use code snippets and get the highlighting directly, and even types hover!

```ts {all|5|7|7-8|10|all} twoslash
// TwoSlash enables TypeScript hover information
// and errors in markdown code blocks
// More at https://shiki.style/packages/twoslash

import { computed, ref } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

doubled.value = 2
```

<arrow v-click="[4, 5]" x1="350" y1="310" x2="195" y2="334" color="#953" width="2" arrowSize="1" />

<!-- This allow you to embed external code blocks -->
<<< @/snippets/external.ts#snippet

<!-- Footer -->

[Learn more](https://sli.dev/features/line-highlighting)

<!-- Inline style -->
<style>
.footnotes-sep {
  @apply mt-5 opacity-10;
}
.footnotes {
  @apply text-sm opacity-75;
}
.footnote-backref {
  display: none;
}
</style>
