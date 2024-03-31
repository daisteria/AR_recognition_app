from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/run_function')
# def run_function():
#     # Call the specific function from your_script.py
#     result = your_function_name()
#     return f'Result: {result}'

@app.route('/run_model')
def run_model():
    # Run the Python code to load the model
    subprocess.run(["python", "pred.py"])
    return 'Model loaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
