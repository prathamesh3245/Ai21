AI21Labs Document Chatbot 🤖📄

An intelligent document-based chatbot powered by LLMs and vector search that allows users to interact with their uploaded files via natural language queries.

🚀 Features
- Semantic Search on uploaded documents using sentence-transformers
- LLM Response Generation via AI21 Labs' Jamba model
- Custom Vector DB using ChromaDB
- REST API Backend built in Flask
- React Frontend (in progress) for chat interface
- PDF Upload and Parsing

🧠 Tech Stack
- Backend: Flask, Python
- LLM: AI21 Labs Jamba
- Vector DB: ChromaDB
- Embeddings: sentence-transformers
- Frontend: React.js (ongoing)
- Database: MongoDB (Mongoose-style schemas)

🗂 File Structure
- `chat2.py` – Main API logic & chat flow
- `chromadb2.py` – Handles PDF upload + embedding
- `chroma_db/` – Custom vector database logic
- `uploads/` – Stores uploaded PDFs

📦 Setup
```bash
git clone https://github.com/prathamesh3245/Ai21.git
cd Ai21
pip install -r requirements.txt
python chat2.py
