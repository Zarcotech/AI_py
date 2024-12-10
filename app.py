from flask import Flask, render_template, request, jsonify
import os
from chatbot import predict_class, get_response, intents

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('user_message')
    if user_message:
        intents_list = predict_class(user_message)
        response = get_response(intents_list, intents)
        return jsonify({"response": response})
    else:
        return "No message received", 400

if __name__ == '__main__':
    app.run(debug=True)
