from flask import Flask, render_template, request
import chatbot
from chatbot import predict_class, get_response, intents
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app = Flask(__name__, template_folder=os.getcwd())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form.get('user_message')
    if user_message:
        intents_list = predict_class(user_message)
        response = get_response(intents_list, intents)
        return response
    else:
        return "No message received", 400

if __name__ == '__main__':
    app.run(debug=True)
