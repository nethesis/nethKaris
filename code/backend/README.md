# WORKSHOP AI

## Requisiti

* Un portatile
* Python 3


## Preparare l'ambiente

Scaricare il codice sorgente

```
git clone https://github.com/Stell0/NethAIWorkshop2024.git
cd NethAIWorkshop2024
```

Decifrare il file api_key.zip con l'API KEY di OpenAI

```
unzip -P PASSWORD api_key.zip
```

Esportare la variabile d'ambiente con l'API key di OpenAI

```
export $(cat api_key.txt)
```

Installare le librerie necessarie

```
pip install -r requirements.txt
```


## Parte 1

In questa parte useremo Langchain per fare un'applicazione che fa il riassunto di un video di YouTube

* LangChain
* Installazione librerie
* Document loaders
* Prompts and Templates

Eseguire il programma

```
python parte1.py https://www.youtube.com/watch?v=0HP6mUlf8xw
```


## Parte 2 - Augmented Generation

In questa parte estenderemo l'applicazione della prima parte per poter fare domande sul video usato nella prima parte

* chains - catene di componenti di LangChain

Eseguire il programma

```
python parte2.py https://www.youtube.com/watch?v=0HP6mUlf8xw
```


## Parte 3 - Retrieval Augmented Generation

In questa parte metteremo il contenuto di alcuni video in un database (Vectorstore) per poi fare domande sul contenuto dei video

* Text Splitters - per dividere il testo in piccoli frammenti
* Embeddings - rappresentazione vettoriale del testo
* Vectorstores - database per salvare il testo e i vettori
* Retrievers - ricerca dei vettori salvati nel vectorstore

Eseguire il programma (test)
```
python parte3.py https://www.youtube.com/playlist?list=PLWzKfs3icbT6yhDTpO1GyDlz9AXdWSiGr
```

Eseguire la parte 3 con tutti i documenti della playlist e un modello migliore

```
python parte3playground.py https://www.youtube.com/playlist?list=PLWzKfs3icbT6yhDTpO1GyDlz9AXdWSiGr
```

