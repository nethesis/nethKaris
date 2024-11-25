---
layout: cover
---

# Javascript 🧠

---

# Cos'è JavaScript?

- JavaScript (JS) è un linguaggio di programmazione per rendere le pagine web interattive.
- Se l'HTML è lo scheletro di una pagina e il CSS il vestito, JavaScript è il cervello!
- Con JavaScript possiamo fare cose come:
  - Mostrare messaggi quando si clicca un pulsante
  - Nascondere o cambiare il contenuto di una pagina
  - Creare giochi, animazioni e tanto altro!

---

# Come funziona JavaScript?

- Il browser web (ad esempio Chrome o Firefox) è in grado di leggere ed eseguire JavaScript.
- Possiamo scrivere il nostro codice JavaScript:
 - Direttamente in una pagina HTML
 - Oppure in un file separato con estensione .js.

---
layout: two-cols
---

```html
<!DOCTYPE html>
<html>
  <head>
    <title>La mia prima pagina JS</title>
  </head>
  <body>
    <h1>Benvenuti!</h1>
    <button onclick="saluta()">Clicca qui</button>

    <script>
      function saluta() {
        alert('Ciao a tutti! 🎉');
      }
    </script>
  </body>
</html>
```

# Cosa fa questo codice?

1. Crea un pulsante sulla pagina.
2. Quando clicchiamo il pulsante, JavaScript mostra un messaggio con la scritta "Ciao a tutti!" in una finestra pop-up.

::right::

<img src="/js-1.png" />

---

# Concetti fondamentali di JavaScript

# 1.  Variabili

- Le variabili sono "scatole" in cui possiamo memorizzare informazioni, come numeri o parole.
- Possiamo crearle con le parole chiave let o const.

```bash
let nome = 'Mario'; // Una variabile che contiene il nome
let eta = 16;       // Una variabile che contiene un numero
const scuola = 'Liceo'; // Una variabile che non può essere cambiata
```

---

# 2. Tipi di dati

- In JavaScript, le variabili possono contenere diversi tipi di informazioni:
 - Stringhe (testo): Racchiuse tra virgolette, ad esempio "Ciao!".
 - Numeri: Ad esempio 42 o 3.14.
 - Booleani (vero/falso): true o false.
 - Array: Una lista ordinata di valori.

```bash
let messaggio = 'Buongiorno!'; // Stringa
let temperatura = 25;         // Numero
let isStudent = true;         // Booleano
let numeri = [10, 20, 30]; // Array
```

---

# Gli array

- Gli array servono per memorizzare più valori in una sola variabile.
- Ogni valore in un array ha un indice che parte da 0 (il primo elemento si trova in posizione 0, il secondo in posizione 1, e così via).

```bash
let numeri = [10, 20, 30]; // Un array con 3 numeri
let colori = ['rosso', 'verde', 'blu']; // Un array con 3 stringhe
```

---

# Come accedere ai valori di un array?

- Possiamo usare il numero dell'indice tra parentesi quadre per accedere a un valore.

```bash
console.log(colori[0]); // Mostra: "rosso"
console.log(numeri[2]); // Mostra: 30
```

---

# Aggiungere elementi a un array

- Possiamo aggiungere nuovi elementi a un array con il metodo .push().

```bash
colori.push('giallo'); // Ora l'array è ['rosso', 'verde', 'blu', 'giallo']
console.log(colori);
```

---

# 3. Operatori

Gli operatori ci permettono di fare operazioni con i dati.

| Operatore |	Significato	| Esempio |	Risultato |
| --------  |  -------- | --------  |  -------- |
| `+` | Addizione |	5 + 2	| 7 |
| `-` | Sottrazione |	5 - 2	| 3 |
| `*` | Moltiplicazione |	5 * 2	| 10 |
| `/` | Divisione |	6 / 2	| 3 |
| `===` | Uguaglianza |	5 === 5	| true |
| `>` | Maggiore |	6 > 2	| true |

--- 

# 4. Condizioni if/else

- Le condizioni ci permettono di eseguire del codice solo se una certa regola è vera.

```bash
let ora = 10;

if (ora < 12) {
  console.log('Buongiorno!'); // Mostra "Buongiorno!" se l'ora è prima di mezzogiorno
} else {
  console.log('Buon pomeriggio!');
}
```

---

# 5. Cicli (loops)

- I cicli servono per ripetere un'azione più volte.
- Ad esempio, stampare i numeri da 1 a 5:

```bash
for (let i = 1; i <= 5; i++) {
  console.log(i); // Mostra: 1, 2, 3, 4, 5
}
```

---

# 6. Funzioni

- Le funzioni sono gruppi di istruzioni che possiamo riutilizzare.
- Possiamo "chiamare" una funzione per far eseguire il codice al suo interno.

```bash
function saluta(nome) {
  console.log('Ciao ' + nome + '!');
}

saluta('Luigi'); // Mostra: "Ciao Luigi!"
saluta('Anna');  // Mostra: "Ciao Anna!"
```

---

# 7. Eventi

- JavaScript può "ascoltare" quello che succede sulla pagina web, come cliccare un pulsante o muovere il mouse.

```bash
document.getElementById('mioBottone').addEventListener('click', function() {
  alert('Hai cliccato il bottone!');
});
```

---
layout: two-cols
---

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Esempio completo</title>
  </head>
  <body>
    <h1>Prova JavaScript!</h1>
    <p>Scrivi il tuo nome e premi invio:</p>
    <input type="text" id="nomeInput" />
    <button onclick="saluta()">Invia</button>

    <script>
      function saluta() {
        let nome = document.getElementById('nomeInput').value;
        alert('Ciao ' + nome + '! 😊');
      }
    </script>
  </body>
</html>
```

::right::

<img src="/js-2.png" />
