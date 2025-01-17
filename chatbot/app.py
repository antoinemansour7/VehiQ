from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})