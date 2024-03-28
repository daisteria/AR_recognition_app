import cv2
import numpy as np
from deepface import DeepFace

# Load the model
model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# frame counter; every 5 frames, makes prediction update
frame_count = 0

# init pred strings and rating
age_text = ""
gender_text = ""
race_text = ""
emotion_text = ""

# Initialize the video capture object
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        faces = model.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces:

            print(frame_count)

            # find face in frame
            face = frame[y:y+h, x:x+w]

            # predictions
            if frame_count % 10 == 0:
                emotions = DeepFace.analyze(face, actions=['emotion'],enforce_detection=False)
                emotion_text = "Emotion: " + emotions[0]['dominant_emotion']

            if frame_count % 30 == 0:
                genders = DeepFace.analyze(face, actions=['gender'], enforce_detection=False)
                gender_text = "Gender: " + genders[0]['dominant_gender']

            if frame_count % 60 == 0:
                races = DeepFace.analyze(face, actions=['race'],enforce_detection=False)
                race_text = "Race: " + races[0]['dominant_race']

            if frame_count % 25 == 0:
                ages = DeepFace.analyze(face, actions=['age'],enforce_detection=False)
                age_text = "Age: " + str(ages[0]['age'])

            # rm later; rating = estimate_rating(age_text, race_text, gender_text, emotion_text)
            print(age_text)
            print(gender_text)
            print(race_text)
            print(emotion_text)

            # put rectangle and emotion text above head
            # move text to side of face later + change colours
            cv2.putText(frame, emotion_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.putText(frame, gender_text, (x, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.putText(frame, age_text, (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.putText(frame, race_text, (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

            frame_count += 1

        cv2.imshow('frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()