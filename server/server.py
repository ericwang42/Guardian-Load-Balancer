from flask import Flask, request

class FlaskApp:

    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return 'Welcome to our web server'

        @self.app.route('/handle_get', methods=['GET'])
        def handle_get():
            if request.method == 'GET':
                return 'Hit the GET endpoint', 200
    
    def run(self):
        self.app.run()
