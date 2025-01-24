# Scuola AI Backend

## Raccolta Pagine Web
### Sorgente Dati
- Blog Karis: http://karis.cloud.neth.eu/
- Implementazione mediante document loader

## Indicizzazione (Embeddings)
### OpenAI Embeddings
- Conversione del testo in vettori numerici
- Cattura della semantica del contenuto

## Memorizzazione (Vectorstore)
### Chroma DB
- Database vettoriale semplice e pratico
- Configurazione persistente per mantenere i dati
- Ottimizzato per ricerche di similitudine

## Ricerca Documenti (Retriever)
### Funzionalità
- Ricerca basata su similitudine semantica
- Limite di 3 documenti nelle risposte
- Ranking basato su rilevanza

## Generazione Risposte
### OpenAI GPT
- Utilizzo di modelli linguistici avanzati
- Prompt engineering per risposte contestuali
- Integrazione con i documenti recuperati

## API Backend (FastAPI)
### Endpoints
1. GET /documents/{query}
   - Restituisce riassunti dei documenti simili
   - Ricerca basata sulla query dell'utente

2. GET /generate/{query}
   - Genera risposte utilizzando il modello linguistico
   - Integra le informazioni dai documenti recuperati

### Caratteristiche
- Framework FastAPI per performance e semplicità
- Documentazione automatica degli endpoint
- Gestione asincrona delle richieste
