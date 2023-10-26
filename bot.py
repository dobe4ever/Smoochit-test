from flask import Flask, render_template

app = Flask(__name__)


@app.route('/templates')
def home():
    return render_template('index.html')


def run():
  app.run(host='0.0.0.0', port=8080)