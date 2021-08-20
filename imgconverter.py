from flask import Flask, request, jsonify, os, base64, datetime

app = Flask(__name__)

@app.route('/api/imgdata', methods=['POST'])

def imgconvert():
    filename = datetime.datetime.now().strftime("%H%M%S%d%m%Y") + ".png"

    img_data = request.get_json().get('img_data')

    with open(filename, "wb") as fh:
        fh.write(base64.b64decode(img_data))

    return "OK"

app.run(host='0.0.0.0', port=5000)