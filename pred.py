import cv2
from cv2 import CascadeClassifier, VideoCapture
import numpy as np
from deepface import DeepFace

# Initialize the video capture object after confirmation
def init_camera() -> VideoCapture:
    cap = cv2.VideoCapture(0)
    return cap

def weigh_age(age) -> int:
    weighed = age // 100
    return weighed

def weigh_gender(gender) -> int:
    # gender labels: ['man', 'woman']
    weighed = 0
    if gender == 'man':
        weighed = 1

    return weighed

def weigh_race(race) -> int:
    # race labels: ['asian', 'indian', 'black', 'white', 'middle eastern', 'latino hispanic']
    weighed = 0
    if race == 'white':
        weighed = 3
    elif race == 'asian':
        weighed = 2
    elif race == 'indian' or race == 'middle eastern':
        weighed = 1

    return weighed

def weigh_emotion(emotion) -> int:
    # emotion labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    weighed = 0
    if emotion == 'happy':
        weighed = 2
    elif emotion == 'neutral' or emotion == 'surprise':
        weighed = 1

    return weighed

# estimate rating /100 of detected face based on weighted factors
# returns percentage int rounded to two decimals
def estimate_rating(age, race, gender, emotion) -> int:
    age_rating = weigh_age(age) * 1
    race_rating = weigh_race(race) * 3
    gender_rating = weigh_gender(gender) * 3
    emotion_rating = weigh_emotion(emotion) * 2

    # highest rating possible: 1+9+3+4=17
    # scaled by 1.5 to average out rating
    total_rating = age_rating + race_rating + gender_rating + emotion_rating
    total_rating = round(total_rating / 17 * 1.2 * 100, 2)

    return total_rating

def load_model() -> CascadeClassifier:
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

def main(model, cap):
    # init variables
    frame_count = 0

    age_text_display = ""
    age_val = 0
    gender_text_display = ""
    gender_val = ""
    race_text_display = ""
    race_val = ""
    emotion_text_display = ""
    emotion_val = ""
    rating_text = ""

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        faces = model.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces:
            # find face in frame
            face = frame[y:y+h, x:x+w]

            # predictions
            if frame_count % 16 == 0:
                print("--- FREEZE ON EMOTION DETECTION ---") # rm later
                emotions = DeepFace.analyze(face, actions=['emotion'],enforce_detection=False)
                emotion_text_display = "Emotion: " + emotions[0]['dominant_emotion']
                emotion_val = emotions[0]['dominant_emotion']

            if frame_count % 31 == 0:
                print("--- FREEZE ON GENDER DETECTION ---") # rm later
                genders = DeepFace.analyze(face, actions=['gender'], enforce_detection=False)
                gender_text_display = "Gender: " + genders[0]['dominant_gender']
                gender_val = genders[0]['dominant_gender']

            if frame_count % 59 == 0:
                print("--- FREEZE ON RACE DETECTION ---") # rm later
                races = DeepFace.analyze(face, actions=['race'],enforce_detection=False)
                race_text_display = "Race: " + races[0]['dominant_race']
                race_val = races[0]['dominant_race']

            if frame_count % 43 == 0:
                print("--- FREEZE ON AGE DETECTION ---") # rm later
                ages = DeepFace.analyze(face, actions=['age'],enforce_detection=False)
                age_text_display = "Age: " + str(ages[0]['age'])
                age_val = ages[0]['age']

            # rm later; rating = estimate_rating(age_text, race_text, gender_text, emotion_text)
            print(age_val)
            print(gender_val)
            print(race_val)
            print(emotion_val)
            print(estimate_rating(age_val, race_val, gender_val, emotion_val))

            rating_text = "Rating: " + str(estimate_rating(age_val, race_val, gender_val, emotion_val))

            # set semi transparent black background to the side of face
            alpha = 0.4  # Opacity of the rectangle (0.0 - 1.0)
            overlay = frame.copy()
            cv2.rectangle(overlay, (x+w+5,y+10), (x+w+200, y+135), (0, 0, 0), -1)
            cv2.rectangle(overlay, (x,y), (x+w,y+h), (255,255,255), 1)
            cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

            # set predictions to frame
            cv2.putText(frame, emotion_text_display, (x+w+15, y+35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
            cv2.putText(frame, gender_text_display, (x+w+15, y+55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
            cv2.putText(frame, age_text_display, (x+w+15, y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
            cv2.putText(frame, race_text_display, (x+w+15, y+95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
            cv2.putText(frame, rating_text, (x+w+15, y+115), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

            frame_count += 1

        cv2.imshow('frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    model = load_model()
    cap = init_camera()
    main(model, cap)