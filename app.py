from flask import Flask, render_template, request, jsonify, send_from_directory
from chatbot import predict_class, get_response, intents
import os

app = Flask(__name__)

@app.route('/')

def home():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json['user_message']
        intents_list = predict_class(user_message)
        response = get_response(intents_list, intents)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
