import gradio as gr
import os
from dotenv import load_dotenv
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt import system_prompt

# Load env
load_dotenv()
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Embeddings + VectorStore
embeddings = download_hugging_face_embeddings()
index_name = "ieee-ai-chat"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

# Chat model
chatModel = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Gradio function
def chatbot_fn(message, history=[]):
    response = rag_chain.invoke({"input": message})
    return response["answer"]

demo = gr.Interface(
    fn=chatbot_fn,
    inputs="text",
    outputs="text",
    title="IEEE AI ChatBot",
    description="Chatbot powered by Pinecone + Gemini"
)

if __name__ == "__main__":
    demo.launch()
