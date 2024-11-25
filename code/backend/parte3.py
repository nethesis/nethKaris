import sys

# Prendiamo l'url della playlist di video di youtube dal primo argomento del comando
url = sys.argv[1]

# prendiamo la lista di video dalla playlist
from get_playlist import get_video_url_from_playlist
video_urls = get_video_url_from_playlist(url)[:2]
print(f"Estratti {len(video_urls)} video dalla playlist")

# Usiamo il Document Loader per caricare il video
from langchain_community.document_loaders import YoutubeLoader

documents = []
for url in video_urls:
	loader = YoutubeLoader.from_youtube_url(
    	url,
		language=["it", "en"]
	)
	documents += loader.load()
print(f"Caricate le trascrizioni di {len(documents)} video")

# print(documents)

# ora usiamo un text splitter per dividere il testo in frasi
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=50,
)
documents = text_splitter.split_documents(documents)
print(f"Divise le trascrizioni in {len(documents)} documenti")
#print(documents)

# creiamo un vectorstore con i nostri documenti
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# creiamo un vectorstore con i nostri documenti
db = Chroma.from_documents(documents, OpenAIEmbeddings())
print("Creato il vectorstore con i documenti")

print("\nInserisci una domanda relativa al contenuto dei video")
question = input()

# Per rispondere ad una domanda dobbiamo trovare i documenti più rilevanti.
# Lo faremo cercando la similarità tra il testo della domanda e i documenti
from langchain_core.vectorstores import VectorStoreRetriever
retriever = VectorStoreRetriever(vectorstore=db, search_type="similarity", search_kwargs={"k": 10})

similar_documents = retriever.invoke(question)
print(f"Trovati {len(similar_documents)} documenti simili alla domanda")
#print(similar_documents)

# formattiamo i documenti in un testo unico che possa essere usato nel nostro prompt
text = ""
for document in similar_documents:
	text += document.page_content + "\n"
	text += "source: https://www.youtube.com/watch?v=" + document.metadata["source"] + "\n\n"


#print(text)

# ora dobbiamo preparare un prompt che usi la domanda e i documenti
# Usiamo il prompt template di langchain
from langchain_core.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([
	("user", """
Utilizza il contenuto del testo fornito per rispondere alla domanda dell'utente citando la fonte. Rispondi che non conosci la risposta se non è contenuta nel testo.
Domanda: {question}
	 
Testo:
{text}
""")
])

# Ora possiamo invocare GPT per generare il riassunto. Avremo bisogno di una API key per OpenAI che verra' presa dall'environment
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# riscriviamo l'ultima parte usando le chain
from langchain_core.runnables import RunnablePassthrough
chain = ({"text": RunnablePassthrough(), "question": RunnablePassthrough()} | prompt_template | llm)

# Eseguiamo la chain
answer = chain.invoke({"text": text, "question": question})

# Stampiamo il risultato
print(answer.content)