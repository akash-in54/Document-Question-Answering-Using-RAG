# Document Question Answering Using RAG

An AI-powered application that enables users to upload PDF documents and ask natural language questions.  
The system uses **Retrieval-Augmented Generation (RAG)** to provide **accurate, context-aware answers** strictly based on the document content.


##  Features

- Upload PDF documents
- Ask questions in natural language
- Context-aware answers grounded in document data
- Reduces hallucination using Retrieval-Augmented Generation (RAG)
- Simple and interactive Streamlit interface

---

## How It Works

1. User uploads a PDF document  
2. The document is split into overlapping text chunks  
3. Text chunks are converted into vector embeddings  
4. Embeddings are stored in a FAISS vector database  
5. User query retrieves the most relevant chunks  
6. Retrieved context is passed to a Large Language Model  
7. LLM generates an answer based only on the document context  

---

## Tech Stack

- Python
- LangChain
- FAISS (Vector Database)
- HuggingFace Sentence Transformers
- Groq LLM (LLaMA 3.1)
- Streamlit
- Retrieval-Augmented Generation (RAG)

---

## Project Structure

AI_PDF_CHATBOT/
│
├── app.py # Streamlit application
├── pdf_utils.py # PDF loading and chunking
├── vectorstore.py # Embeddings and FAISS vector store
├── qa_chain.py # RAG pipeline using LangChain Runnable
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files



---

##  How to Run the Project

###  Clone the Repository
'''bash
git clone https://github.com/<your-username>/Document-Question-Answering-Using-RAG.git
cd AI_PDF_CHATBOT

---
# Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

---

# Install Dependencies
pip install -r requirements.txt

---

# Set Environment Variable
Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here


---

# Run the Application
streamlit run app.py

Open your browser at:
http://localhost:8501



