import cv2
import webbrowser
from flask import Flask, render_template, render_template_string, Response
from pred import main, load_model, init_camera, process_frame

app = Flask(__name__)
model = load_model()
video_capture = init_camera()

# Function to generate video frames
def gen_frames():
    frame_count = 0
    age_val = 0
    gender_val = ""
    race_val = ""
    emotion_val = ""
    while True:
        success, frame = video_capture.read()  # Read a frame from the camera
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        if not success:
            break
        frame_count += 1

        # Process the frame using the modified main() function
        processed_frame, age_val, gender_val, race_val, emotion_val = process_frame(model, frame, frame_count, age_val, gender_val, race_val, emotion_val)

        # Encode the processed frame to JPEG
        ret, buffer = cv2.imencode('.jpg', processed_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('client_index.html')

# Route to stream video frames
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()