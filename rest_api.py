import json
from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
    return json.dumps({'name': 'alice', 'email':'alice@gmail.com'})
    
app.run()