from flask import Blueprint, request, jsonify
import chromadb
from transformers import AutoTokenizer, AutoModel
import torch
from pypdf import PdfReader
import os
import fitz
from werkzeug.utils import secure_filename
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np



chroma_bp = Blueprint('chroma_bp', __name__)


tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

db_path = r"C:\Users\PRATHMESH\Flask\Ai21Labs\chroma_db"
if not os.path.exists(db_path):
    os.makedirs(db_path)

client = chromadb.PersistentClient(path=db_path)
collection = client.get_or_create_collection(name="document_collection")




def extract_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        raise ValueError("Unsupported file format. Use .pdf or .txt")
    
    return text.strip() if text else "No text found in the document."






def text_to_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        output = model(**inputs)
        embedding = output.last_hidden_state[:, 0, :]  # CLS token
    return embedding.squeeze().tolist()





@chroma_bp.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files.get('file')
    if file:
        
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

       
        text = extract_text(file_path)
        embedding = text_to_embedding(text)

        
        collection.add(
            ids=[file.filename],
            embeddings=[embedding],
            metadatas=[{"filename": file.filename}]
        )

        return jsonify({"message": "File uploaded and embedded successfully!"}), 200
    else:
        return jsonify({"error": "No file uploaded."}), 400










@chroma_bp.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    
   
    files_in_db = collection.get(include=["metadatas"])
    if not files_in_db['metadatas']:
        return jsonify({"error": "No PDF files uploaded."}), 400
    
    
    latest_pdf = files_in_db['metadatas'][0]['filename']
    file_path = os.path.join(os.getcwd(), 'uploads', latest_pdf)

    try:

        pdf_document = fitz.open(file_path)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text("text")
        pdf_document.close()

        # Implement a basic search to answer the question (you can replace this with more sophisticated logic)
        if question.lower() in text.lower():
            return jsonify({"answer": f"Found the keyword '{question}' in the document."})
        else:
            return jsonify({"answer": "Sorry, I couldn't find any relevant information in the document."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


