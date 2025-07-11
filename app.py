import streamlit as st
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API key setup
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("Defina a variável de ambiente OPENAI_API_KEY.")
    st.stop()

# Page title and description
st.set_page_config(page_title="SUPORTE COM IA", layout="centered")
st.title("🛠️ ASSISTENTE INTELIGENTE")
st.caption("Sistema de atendimento que usa IA com base em documentação técnica em PDF")

# User input field
user_input = st.text_input("Descreva o detalhadamente da sua dúvida:",placeholder="Como socorrer uma pessoa com hemorragia?", key="user_input", on_change=lambda: st.session_state.update({"user_input_submitted": True}))

# PDF loading and vector database creation
@st.cache_resource
def carregar_base_pdf():
    try:
        loader = PyPDFLoader("document.pdf")
        documentos = loader.load_and_split()
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vetor = FAISS.from_documents(documentos, embeddings)
        return vetor.as_retriever()
    except Exception as e:
        st.error(f"Erro ao carregar PDF: {str(e)}")
        return None

# Button to start the support process
execute_button = st.button("Executar atendimento")

# Check if button was clicked or Enter was pressed
if (execute_button or st.session_state.get("user_input_submitted", False)) and user_input:
    # Reset the submission flag
    if "user_input_submitted" in st.session_state:
        st.session_state.user_input_submitted = False
    # Loading the PDF manual
    with st.spinner("Carregando manual do sistema..."):
        retriever = carregar_base_pdf()
        
        # Check if retriever loaded successfully
        if retriever is None:
            st.error("Não foi possível carregar o manual PDF. Verifique se o arquivo 'document.pdf' existe.")
            st.stop()
    
    # Simulate the support process
    status = {
        "atendente": "O atendente está analisando o problema...",
        "especialista": "O Especialista em Diagnóstico está procurando a melhor abordagem...",
        "tecnico": "Técnico está elaborando uma resposta adequada com base no documento..."
    }

    # Show each step with individual spinners
    for etapa, mensagem in status.items():
        with st.spinner(mensagem):
            time.sleep(1.5)
        st.markdown(f"✅ {mensagem}")

    # Process the actual query with AI
    with st.spinner("Processando sua consulta com IA..."):
        try:
            chain = RetrievalQA.from_chain_type(
                llm=ChatOpenAI(temperature=0, model_name="gpt-4o-mini", openai_api_key=openai_api_key),
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=False
            )

            resposta = chain.invoke({"query": user_input})["result"]
            
        except Exception as e:
            st.error(f"Erro ao processar a consulta: {str(e)}")
            st.info("Por favor, tente novamente ou verifique sua conexão com a internet.")
            st.stop()

    st.success("✅ Atendimento finalizado.")
    
    # Show the final result
    st.markdown("### Resposta do Técnico:")
    st.info(resposta)
