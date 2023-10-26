from googlesearch import search
import openai
import os

# Define the OpenAI key from the environment variable
openai.api_key = os.environ['OPENAI_API_KEY']


def simple_internet_search(query):
    results = []
    for result in search(query, num_results=5, lang="en"):
        results.append(result)
    return results

# search_query = input("Enter your search query: ")
# search_results = simple_internet_search(search_query)

# for i, result in enumerate(search_results, start=1):
#     print(f"Result {i}: {result}")


def get_response(query):
    # Send conversation to AI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': query}]
    )
    content = response["choices"][0]["message"]["content"]
    return content

