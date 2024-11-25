import time
from get_playlist import get_video_url_from_playlist
from langchain_community.document_loaders import YoutubeLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
import sys

url = sys.argv[1]

# prendiamo la lista di video dalla playlist
print(f"Prendiamo i video dalla playlist {url}...")
video_urls = get_video_url_from_playlist(url)
print(f"Estratti {len(video_urls)} video dalla playlist")

# Usiamo il Document Loader per caricare il video
print("Carichiamo le trascrizioni dei video...")
documents = []
for url in video_urls:
	try:
		loader = YoutubeLoader.from_youtube_url(
    		url,
			language=["it", "en"]
		)
		documents += loader.load()
		print(f"Caricato il video {url}")
		# cerchiamo di evitare di farci bannare da youtube
		#time.sleep(1)
	except:
		print(f"Errore nel caricare il video {url}")
		continue
print(f"Caricate le trascrizioni di {len(documents)} video")

# print(documents)

# ora usiamo un text splitter per dividere il testo in frasi
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=50,
)
documents = text_splitter.split_documents(documents)
print(f"Divise le trascrizioni in {len(documents)} documenti")
#print(documents)

# creiamo un vectorstore con i nostri documenti
print("Creiamo il vectorstore con i documenti...")
db = Chroma.from_documents(documents, OpenAIEmbeddings())
print("Creato il vectorstore con i documenti")

# Per rispondere ad una domanda dobbiamo trovare i documenti più rilevanti. Lo faremo cercando la similarità tra il testo della domanda e i documenti
retriever = VectorStoreRetriever(vectorstore=db, search_type="similarity", search_kwargs={"k": 10})

# preparamo un prompt che usi la domanda e i documenti
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", """
Utilizza il contenuto del testo fornito per rispondere alla domanda dell'utente citando la fonte. Rispondi che non conosci la risposta se non è contenuta nel testo.
Domanda: {question}
	 
Testo:
{text}

ricordati di citare la fonte
""")
])

# Carichiamo il modello di GPT
llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

# componiamo la chain
chain = ({"text": RunnablePassthrough(), "question": RunnablePassthrough()} | prompt_template | llm)

# facciamo partire un ciclo che fa domande e scrive le risposte
while True:
	print("\nInserisci una domanda relativa al contenuto dei video")
	question = input()

	similar_documents = retriever.invoke(question)

	# formattiamo i documenti
	text = ""
	for document in similar_documents:
		text += document.page_content + "\n"
		text += "source: https://www.youtube.com/watch?v=" + document.metadata["source"] + "\n\n"
	
	print(text)
	# Eseguiamo la chain
	answer = chain.invoke({"text": text, "question": question})

	# Stampiamo il risultato
	print(answer.content)