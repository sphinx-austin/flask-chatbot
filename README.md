# Chatbot Deployment with Flask and JavaScript

This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ https://github.com/sphinx-austin/flask-chatbot.git
$ cd flask-chatbot
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
OR
Install all dependencies
```
$ (venv) pip install -r requirements.txt
```

Note: (venv) infront of the code means you are running on a virtual ennvironment

Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.

Done!!

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
