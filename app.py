from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Verificación de API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY no encontrada. Por favor, configura esta variable de entorno.")

system_prompt = """
Eres un asistente útil que responde preguntas basadas en la información proporcionada.
Eres un Asistente Especializado para guiarte hacer tus tramites sobre la Facultad de Ingenieria Electrica y Electronica (FIEE - UNI), de ahi continua dando informacion y respondiendo de manera conversacional.
RECUERDA: Ser conversacional y amigable, pero siempre manteniendo la profesionalidad.

1. Si te preguntan sobre temas relacionados al ciclo academico, analiza bien la data puesto que, las fechas son delicadas. 
En el año normalmente se dividen en 3 ciclos: Ciclo (Año actual menos - 3) (enero - marzo), Ciclo (Año actual - 1) (marzo - agosto) y Ciclo (Año actual menos - 2) (agosto - diciembre). Para eso fijate en la data que se te ha proporcionado.
Recuerda toda la conversación previa para proporcionar respuestas contextualizadas.
Si te preguntan sobre algo que no está en la información proporcionada, indica que no tienes 
esa información disponible.
"""

def crear_prompt_template():
    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

def main():

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = FAISS.load_local("vector_db_imagenes", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",  
        temperature=0.7
    )
    

    prompt = crear_prompt_template()

    chat_history = []
    
    print("¡Chatbot listo! Escribe 'salir' para terminar.")

    while True:
        query = input("\nTú: ")
        
        if query.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
            
        try:

            docs = retriever.invoke(query)
            
            context = "\n\n".join([
                f"Documento: {doc.metadata.get('filename', 'Desconocido')}\n" +
                f"Tipo: {doc.metadata.get('tipo', 'Desconocido')}\n" +
                f"Contenido: {doc.page_content}"
                for doc in docs
            ])
            
            formatted_prompt = prompt.format(
                chat_history=chat_history,
                question=f"Basándote en la siguiente información, responde esta pregunta: {query}\n\n" +
                        f"Información relevante:\n{context}"
            )           
            response = llm.invoke(formatted_prompt).content

            print("\nChatbot:", response)
            

            chat_history.append(HumanMessage(content=query))
            chat_history.append(AIMessage(content=response))
            
        except Exception as e:
            print(f"\nOcurrió un error: {str(e)}")
            
if __name__ == "__main__":
    main()