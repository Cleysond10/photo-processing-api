from flask import Flask, jsonify, request
from classification import get_photo_classification

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def getAll():
    return jsonify(['HELLO', 'WORLD'])


app.run(port=5000, host='localhost', debug=True)
