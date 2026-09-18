import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ API key not found")
    exit()

client = Groq(api_key=api_key)

print("\n🔍 Checking available models...\n")

try:
    models = client.models.list()

    for model in models.data:
        print("✅", model.id)

except Exception as e:
    print("❌ Error:", e)