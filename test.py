### python3 test.py
Procfile
web: streamlit run bot.py


import openai
import os

# Define the OpenAI key from the environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Generate code with ChatGPT
prompt = [{
    "role": "user", 
    "content": "hello..."
}]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=prompt,
    temperature=0.1
)
response_message = response["choices"][0]["message"]
generated_code = response.choices[0].text.strip()
print(generated_code)
# Add necessary import statements
code_to_execute = "import math\n" + generated_code

# Execute the generated code
exec(code_to_execute, globals())

# Now you can call the generated function
print(factorial(5))





# Generate code with ChatGPT
prompt = "Write a Python function that calculates the factorial of a number."
response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
generated_code = response.choices[0].text.strip()

# Add necessary import statements
code_to_execute = "import math\n" + generated_code

# Execute the generated code
exec(code_to_execute, globals())

# Now you can call the generated function
print(factorial(5))

