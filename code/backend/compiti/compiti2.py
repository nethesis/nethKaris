from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import nest_asyncio
import uvicorn
from langchain_core.vectorstores import VectorStoreRetriever

# Apply nest_asyncio to allow event loop reuse
nest_asyncio.apply()

# Create the FastAPI app
app = FastAPI()

@app.get("/documents/{query}", response_model=List[dict])
def get_documents(query: str):
    # carichiamo il db con i documenti
    db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory='chroma_db_gite')
    # creiamo un retriever
    retriever = VectorStoreRetriever(vectorstore=db, search_type="similarity", search_kwargs={"k": 3})
	# cerchiamo i documenti simili alla query
    matching_docs = retriever.invoke(query)

	# carichiamo il db con i riassunti
    db_riassunti = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory='chroma_db_riassunti')
    # creiamo un retriever
    retriever_riassunti = VectorStoreRetriever(vectorstore=db_riassunti, search_type="similarity", search_kwargs={"k": 3})
    # cerchiamo i documenti simili alla query
    matching_docs_riassunti = retriever_riassunti.invoke(query)
    
    if not matching_docs+matching_docs_riassunti:
        raise HTTPException(status_code=404, detail="No documents found matching the query.")


	# facciamo un array con il risultato dei documenti
    result = []
    for document in matching_docs+matching_docs_riassunti:
        result.append({
            'query': query,
			'title': document.metadata['title'],
			'content': document.page_content,
			'url': document.metadata['source']
		})  

    return result

# Run the FastAPI app
uvicorn.run(app, host="0.0.0.0", port=8000)

# verifica il funzionamento andando alla pagina http://karis.sf.nethserver.net:8000/documents/testquery