from flask import Flask, render_template, request, jsonify
import subprocess
import cv2
import webbrowser

from pred import init_camera, load_model, process_frame

app = Flask(__name__)
cam = cv2.VideoCapture(0)
model = None

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/init_camera')
# def run_camera():
#     global cam
#     # Call the specific function from pred.py
#     cam = init_camera()
#     return f'Result: {cam}'

@app.route('/load_model')
def load_model():
    global model
    # Call the specific function from pred.py
    model = load_model()
    return f'Result: {model}'

@app.route('/process_image', methods=['POST'])
def process_image_route():
    image_data = request.json.get('image')
    # Process the image using functions from pred.py
    result = process_frame(image_data)
    return jsonify({'result': result})

@app.route('/run_model', methods=['GET', 'POST'])
def run_model():
    # Run the Python code to load the model
    subprocess.run(["python", "pred.py"])
    return 'Model loaded successfully!'

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()