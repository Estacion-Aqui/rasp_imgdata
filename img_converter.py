from flask import Flask, request, jsonify
import os, base64, datetime, fnmatch

app = Flask(__name__)
imgDir = ""

@app.route('/api/imgdata', methods=['POST'])
def img_convert():
    currentTime = datetime.datetime.now().strftime("%H%M%S%d%m%Y")
    img_data = request.get_json().get('img_data')
    cam_id = request.get_json().get('cam_id')
    spot_number = request.get_json().get('spot_number')

    filename = f"{cam_id}_{spot_number}_{currentTime}.png"

    with open(os.path.join(imgDir, filename), "wb") as fh:
        fh.write(base64.b64decode(img_data))

    return "OK"

for path, dirs, files in os.walk('..'):
  for dir in fnmatch.filter(dirs, 'resources'):
    imgDir = os.path.abspath(os.path.join(path, dir))

app.run(host='0.0.0.0', port=5000)
