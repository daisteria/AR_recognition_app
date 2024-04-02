# AR_recognition_app
A futuristic application with facial recognition that computes a person's social status rating based on their detected features (ie. age, race, gender, emotion). Similar to the Black Mirror episode.

For educational purposes only. Rating based on appearance reflects ethical concerns over dependency on judging individuals through AI.

# Live demo
There are two ways to try a live demo.
Note: demos take some time to initiate and run.

To quit, in the terminal, press CTRL-C.

## Browser
To try a live demo, run the following in a powershell terminal of the root directory:

```
pip install -r requirements.txt
waitress-serve --listen:127.0.0.1:8000 'webserver_app:app'
```

Then, navigate to <https://127.0.0.1:8000/> to see the live camera feed and detection. 

## Terminal - New Window (Recommended)
This live demo will open a new window frame. In the terminal,

```
pip install -r requirements.txt
python app.py
```

## Non-technical Users
This is a walkthough for non-technical users to try a live demo.

1. Download the zip of this project by pressing the green 'Code' button.
2. Unzip the folder, and right-click the unzipped project.
3. Open the unzipped project in terminal (Powershell).
4. In terminal, ensure that you're in the right directory by running the ```ls``` command. This should output a list of files, with the last listed file named "webserver_app.py". If only one file outputs, run ```cd``` and hit TAB before pressing the RETURN key.
5. Run the following commands to view a live demo:
   ``` pip install -r requirements.txt```
   ```python app.py```


# Troubleshooting

## Python version
If the Python version installed is not 3.10.0, attempting to try a live demo will result in a failure. To avoid this, run ```$env:PYTHON_VERSION=3.10.0``` in the terminal before trying the live demo.
If Python is not installed, then run ```pip install python==3.10.0``` or download Python v.3.10.0 from the official Python site.

## tensorflow version unavailable
During ```pip install -r requirements.txt```, if an Error occurs that a dependency does not match any other versions, simply remove that dependency line from requirements.txt and run the command again. 

## waitress-serve unavailable
If waitress-serve does not work as expected (i.e. an Error occurs or the terminal does not output a "Serving to ..." line, then try the Terminal - New Window live demo instead.
