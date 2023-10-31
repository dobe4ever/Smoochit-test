import os
import openai
from flask import Flask, render_template, request
from utils import load_json, save_json

openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/get_response")
# def get_response():
#     message = request.args.get("message")
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": message}],
#         max_tokens=100
#     )
#     response = completion["choices"][0]["message"]["content"]
#     return response
    
@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    
    # load messages history json
    conversation = load_json("conversation.json")     
    # Append the new user message to the message history
    conversation.append({"role": "user", "content": message})
    # save conversation
    save_json(conversation, "conversation.json")
    # Get the system message + the most recent messages
    context = [conversation[0]] + conversation[-10:]
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=context,
        max_tokens=100
    )
    response = completion["choices"][0]["message"]["content"]
    
    conversation.append({"role": "assistant", "content": response})
    save_json(conversation, "conversation.json")
    
    return response

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)



