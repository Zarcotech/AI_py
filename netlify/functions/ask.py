from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/.netlify/functions/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message')
    response = get_response(message)
    return jsonify({"response": response})

def get_response(message):
    return "This is a response to: " + message

if __name__ == '__main__':
    app.run(debug=True)
