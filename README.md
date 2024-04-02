# AR_recognition_app
A futuristic application with facial recognition that computes a person's social status rating based on their detected features (ie. age, race, gender, emotion). Similar to the Black Mirror episode.

For educational purposes only. Rating based on appearance reflects ethical concerns over dependency on judging individuals through AI.

# Live demo
There are two ways to try a live demo.
Note: demos take some time to initiate and run.

To quit, in the terminal, press CTRL-C.

## Browser
To try a live demo, run the following in the terminal:

```
pip install -r requirements.txt
waitress-serve --listen:127.0.0.1:8000 'webserver_app:app'
```

Then, navigate to <https://127.0.0.1:8000/> to see the live camera feed and detection. 

## Terminal (New Window)
This live demo will open a new window frame. In the terminal,

```
pip install -r requirements.txt
python app.py
```
