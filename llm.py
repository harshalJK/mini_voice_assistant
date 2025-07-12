import openai
from openai import OpenAI

client = OpenAI(api_key="")  # replace with your real key

def ask_llm(prompt):
    print("🤖 Thinking...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content
    print("💬 Bot:", reply)
    return reply
