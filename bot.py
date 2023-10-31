import os

import openai
from flask import Flask, render_template, request

openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    response = completion["choices"][0]["message"]["content"]
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



