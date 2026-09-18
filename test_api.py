import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

models_to_test = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b"
]

for model in models_to_test:

    print("\nTesting:", model)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Say hello in one sentence."
                }
            ]
        )

        print("✅ WORKING MODEL:", model)
        print("🤖 AI:", response.choices[0].message.content)

    except Exception as e:
        print("❌ Not available")
        print(e)