from flask import Flask, jsonify, request
from classification import get_photo_classification
from histogram import generate_histogram

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def getAll():
    return jsonify(['HELLO', 'WORLD'])


@app.route('/classification', methods=['POST'])
def getPhotoClassification():
    json = request.get_json()
    classification = get_photo_classification(json["photo"])
    return jsonify(classification)


@app.route('/histogram', methods=['POST'])
def generateHistogram():
    json = request.get_json()
    histogram = generate_histogram(json["photo"])
    return jsonify(histogram)


app.run(port=5000, host='localhost', debug=True)
