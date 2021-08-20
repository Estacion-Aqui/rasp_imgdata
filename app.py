from flask import Flask 
from flask import request, jsonify

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
