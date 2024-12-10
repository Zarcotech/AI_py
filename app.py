from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS
import chatbot
from chatbot import predict_class, get_response, intents

app = Flask(__name__, template_folder=os.getcwd())
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json.get('user_message')
        if user_message:
            intents_list = predict_class(user_message)
            response = get_response(intents_list, intents)
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'No message received'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
