# AR_recognition_app
A futuristic application with facial recognition that computes a person's social status rating based on their detected features (ie. age, race, gender, emotion). Similar to the Black Mirror episode.

For educational purposes only. Rating based on appearance reflects ethical concerns over dependency on judging individuals through AI.

# Live demo (browser)

To try a live demo, run the following in the terminal:

```
pip install -r requirements.txt
waitress-serve --listen:127.0.0.1:8000 'webserver_app:app'
```

Then, navigate to <https://127.0.0.1:8000/> to see the live camera feed and detection. 
