from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate response
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Give market analysis for pharmaceutical sector in India"
)

print(response.text)