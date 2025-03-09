import os
from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

app = Flask(__name__)

client = genai.Client(api_key = api_key)

# Define the POST endpoint
@app.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()

        if 'text' not in data:
            return jsonify({"error": "Missing 'text' in request body"}), 400

        text = data['text']

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text
        )

        return jsonify({"generated_text": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
