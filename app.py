from flask import Flask, render_template, jsonify, request
from chat import get_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config[' SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.get('/')
def index_get():
    return render_template('base.html')


@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    # sentence = request.form['question']

    # response = get_response(sentence)
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
    # return jsonify({"response": response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
