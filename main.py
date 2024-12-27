from openwebui import OpenWebUI
from flask import Flask, jsonify, request
import chatbot 

app = Flask(__name__)
web_ui = OpenWebUI(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    response = chatbot.get_response(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    web_ui.start()
