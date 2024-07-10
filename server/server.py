from flask import Flask, request

class FlaskApp:

    def __init__

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to our web server'

@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        return 'Hit the GET endpoint', 200

if __name__ == 'main':
    app.run()
