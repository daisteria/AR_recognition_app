from flask import Flask, render_template
import subprocess

from pred import init_camera, load_model, main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init_camera')
def run_camera():
    # Call the specific function from pred.py
    result = init_camera()
    return f'Result: {result}'

@app.route('/run_model', methods=['GET', 'POST'])
def run_model():
    # Run the Python code to load the model
    subprocess.run(["python", "pred.py"])
    return 'Model loaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
