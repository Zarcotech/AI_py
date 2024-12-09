from flask import Flask, render_template, request
import chatbot
from chatbot import predict_class, get_response, intents

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    intents_list = predict_class(user_message)
    response = get_response(intents_list, intents)
    return response

if __name__ == '__main__':
    app.run(debug=True)
