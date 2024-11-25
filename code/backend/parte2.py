# Prendiamo l'url del video di youtube dal primo argomento del comando
import sys
url = sys.argv[1]

# Usiamo il Document Loader per caricare il video
from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    url,
	language=["it", "en"]
)

document = loader.load()[0]

# ora dobbiamo preparare un prompt per GPT per generare il riassunto del video
# Usiamo il prompt template di langchain
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
	("user", """
Utilizza il contenuto del testo fornito per rispondere alla domanda dell'utente. Rispondi che non conosci la risposta se non è contenuta nel testo.
Domanda: {question}
	 
Testo:
{transcript}
""")
])

# Ora possiamo invocare GPT per generare il riassunto. Avremo bisogno di una API key per OpenAI che verra' presa dall'environment
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# riscriviamo l'ultima parte usando le chain
from langchain_core.runnables import RunnablePassthrough
chain = ({"transcript": RunnablePassthrough(), "question": RunnablePassthrough()} | prompt_template | llm)

# Chiediamo all'utente di fare una domanda
print("Inserisci una domanda relativa al contenuto del video")
question = input()

# Eseguiamo la chain
answer = chain.invoke({"transcript": document.page_content, "question": question})

# Stampiamo il risultato
print(answer.content)