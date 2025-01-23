from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough

# Usiamo il Document Loader per le gite
from langchain_community.document_loaders import WebBaseLoader
wordpress_urls = [
    "http://karis.cloud.neth.eu/mantova-2024/",
    "http://karis.cloud.neth.eu/campania-2023/",
	"http://karis.cloud.neth.eu/firenze-05-2024/",
	"http://karis.cloud.neth.eu/grecia-2022/",
	"http://karis.cloud.neth.eu/vienna-e-monaco-2023/",
	"http://karis.cloud.neth.eu/firenze-2024/",
	"http://karis.cloud.neth.eu/bali-2023/",
	"http://karis.cloud.neth.eu/antibes-2024/",
]
loader = WebBaseLoader(wordpress_urls)

documents = loader.load()

# creiamo un vectorstore con i nostri documenti
print("Creiamo il vectorstore con i documenti...")
db = Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory='chroma_db_gite')
print("Creato il vectorstore con i documenti")

# Riassunti
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
	("user", "Riassumi in italiano il test seguente in un singolo paragrafo. Scrivi direttamente il riassunto senza nessun preambolo: {text}"),
])

# Carichiamo il modello di GPT
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# creaimo la chain per generare il riassunto
chain = ({"text": RunnablePassthrough()} | prompt_template | llm)

riassunti = []
for document in documents:
	# Invochiamo il modello con il template
	summary = chain.invoke({"text": document.page_content}).content
	print(f"Riassunto: {summary}\n")
	document_summary = document
	document_summary.page_content = summary
	riassunti.append(document_summary)

# creiamo un vectorstore con i riassunti
print("Creiamo il vectorstore con i riassunti...")
db_riassunti = Chroma.from_documents(riassunti, OpenAIEmbeddings(), persist_directory='chroma_db_riassunti')
print("Creato il vectorstore con i riassunti")
