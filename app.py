from flask import Flask

app = Flask(__name__)

@app.route('/')
def appRun():
    return '<h1>Flask is running!</h1>'

if __name__ == '__main__':
    app.run(debug=True)