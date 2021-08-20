from flask import Flask 
from flask import request, jsonify
import base64

app = Flask(__name__)

spots = [
    {'id': 0,
     'plate': '',
     'empty': True},
     {'id': 1,
     'plate': 'GBM4E01',
     'empty': False}
]

@app.route('/easteregg')
def hello():
    return 'O Igão gostava da suco!'

@app.route('/api/v1/resources/spots/all', methods=['GET'])
def api_call():
    return jsonify(spots)

@app.route('/api/v1/resources/imgdata', methods=['POST'])

def imgconvert():
    img_data = request.get_json().get('img_data')
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(img_data))

app.run(host='0.0.0.0', port=5000)