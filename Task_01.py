import os
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()

# Retrieve your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

def generate_response(messages):
    response = completion(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key=api_key  # Secure way to load your API key
    )
    return response['choices'][0]['message']['content']

# Example usage
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a fun fact about space."}
]

response = generate_response(messages)
print(response)
