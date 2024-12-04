import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")
print(f"API Key found: {'Yes' if api_key else 'No'}")

# Initialize Groq client
client = Groq(api_key=api_key)

# Test API
try:
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Say hello!"}],
        model="mixtral-8x7b-32768",
    )
    print("\nAPI Response:")
    print(chat_completion.choices[0].message.content)
    print("\nAPI is working correctly!")
except Exception as e:
    print(f"\nError testing API: {str(e)}")
