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

# il nostro documento è ora pronto per essere analizzato. Ma vediamo prima cosa c'è dentro
print(document)

# ora dobbiamo preparare un prompt per GPT per generare il riassunto del video
# Usiamo il prompt template di langchain
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
	("user", "Riassumi in italiano il seguente transcript di un video: {transcript}")
])

# valorizziamo il template con il contenuto del documento
template = prompt_template.invoke({"transcript": document.page_content})
print(template)

# Ora possiamo invocare GPT per generare il riassunto.
# Avremo bisogno di una API key per OpenAI che verra' presa dall'environment
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# Invochiamo il modello con il template
answer = llm.invoke(template)

# Stampiamo il risultato
print(answer.content)






