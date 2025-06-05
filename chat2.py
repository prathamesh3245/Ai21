from flask import Flask, request, jsonify
from ai21 import AI21Client
from pymongo import MongoClient
from ai21.models.chat import UserMessage
from flask_cors import CORS
from Chromdb2 import chroma_bp


app = Flask(__name__)
CORS(app)


app.register_blueprint(chroma_bp)


MONGO_URI = "mongodb://localhost:27017/"
client_mongo = MongoClient(MONGO_URI)
db = client_mongo["Ai21"] 
collection = db["Ai21Labs"]


API_KEY = "GwuFbC7Fm1DyDZmt917mvuC4C0XxG5gg"
client = AI21Client(api_key=API_KEY)



@app.route('/chat', methods=['POST'])
def chat_with_ai21():
    data = request.json
    prompt = data.get("question", "")  # instead of 'prompt'


    messages = [UserMessage(content=prompt)]

    response = client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        top_p=1.0
    )

    ai_text = response.choices[0].message.content if response.choices else "No response"


    response_data = {
        "user_prompt": prompt,
        "ai_response": ai_text
    }
    inserted_doc = collection.insert_one(response_data)
    
    response_data["_id"] = str(inserted_doc.inserted_id)

    return jsonify({"message": "Response stored successfully!", "data": response_data})


if __name__ == '__main__':
    app.run(debug=True)


