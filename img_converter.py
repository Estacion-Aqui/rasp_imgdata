from flask import Flask, request, jsonify
from PIL import Image
import os, base64, datetime, fnmatch, io, cv2
import numpy as np

app = Flask(__name__)
imgDir = ""

@app.route('/api/imgdata', methods=['POST'])
def img_convert():
    currentTime = datetime.datetime.now().strftime("%H%M%S%d%m%Y")
    img_data = request.get_json().get('img_data')
    cam_id = request.get_json().get('cam_id')
    spot_number = request.get_json().get('spot_number')
    status = request.get_json().get('spot_status')

    filename = f"{cam_id}_{status}_{currentTime}.jpeg"
    filepath = os.path.join(imgDir, filename)

    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2.imwrite(filepath, img)
    cv2.imwrite(os.path.join("backups", filename), img)

    return "OK"

for path, dirs, files in os.walk('..'):
  for dir in fnmatch.filter(dirs, 'resources'):
    imgDir = os.path.abspath(os.path.join(path, dir))

app.run(host='0.0.0.0', port=5000)
