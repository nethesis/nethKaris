from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import nest_asyncio
import uvicorn
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from fastapi.middleware.cors import CORSMiddleware

# Apply nest_asyncio to allow event loop reuse
nest_asyncio.apply()

# Create the FastAPI app
app = FastAPI()

origins = ["*"]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/documents/{query}", response_model=List[dict])
def get_documents(query: str):
    # carichiamo il db con i documenti
    db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory='chroma_db')
    # creiamo un retriever
    retriever = VectorStoreRetriever(vectorstore=db, search_type="similarity", search_kwargs={"k": 3})
	# cerchiamo i documenti simili alla query
    matching_docs = retriever.invoke(query)
    
    if not matching_docs:
        raise HTTPException(status_code=404, detail="No documents found matching the query.")


	# facciamo un array con il risultato dei documenti
    result = []
    for document in matching_docs:
        result.append({
            'query': query,
			'title': document.metadata['title'],
			'content': document.page_content,
            'summary': document.metadata['summary'],
			'url': document.metadata['source']
		})  

    return result

@app.get("/generate/{query}", response_model=str)
def get_generate(query: str):
    # carichiamo il db con i documenti
	db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory='chroma_db')
	# creiamo un retriever
	retriever = VectorStoreRetriever(vectorstore=db, search_type="similarity", search_kwargs={"k": 3})
	# cerchiamo i documenti simili alla query
	matching_docs = retriever.invoke(query)
	
	if not matching_docs:
		raise HTTPException(status_code=404, detail="No documents found matching the query.")

	# formattiamo i documenti in un testo unico che possa essere usato nel nostro prompt
	text = ""
	for document in matching_docs:
		text += document.page_content + "\n"
		text += "source: " + document.metadata["source"] + "\n\n"
    
	# Usiamo il modello di GPT
	llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
	prompt_template = ChatPromptTemplate.from_messages([
		("system", """
Utilizza il contenuto del testo fornito per rispondere alla domanda dell'utente rispettando le seguenti regole:
   - **Cita la fonte**: includi il link alla pagina web da cui proviene il testo nel formato "fonte: http://..."
   - **Rispondi alla domanda**: scrivi una risposta alla domanda dell'utente in modo chiaro e conciso.
   - **Non inventare informazioni**: Usa solo le informazioni presenti nel testo fornito.
   - **Usa la lingua dell'utente**: Rispondi nella lingua in cui è stata fatta la domanda
"""),
		("user","Domanda: {question}\n\nTesto:\n{text}")
	])
	chain = ({"text": RunnablePassthrough(), "question": RunnablePassthrough()} | prompt_template | llm)
	answer = chain.invoke({"text": text, "question": query}).content
	return answer

# Run the FastAPI app
uvicorn.run(app, host="0.0.0.0", port=8888)

# verifica il funzionamento andando alla pagina http://karis.sf.nethserver.net:8000/documents/testquery