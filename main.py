import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# 🔹 Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("🚨 GEMINI_API_KEY not found in .env file!")

# 🔹 Configure Gemini client
genai.configure(api_key=API_KEY)

# 🔹 Function to load agent instructions
def load_instruction(file_path):
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        print(f"⚠️ File not found: {abs_path}. Using default instruction.")
        return "You are a general assistant."
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 🔹 Function to load local context from JSON
def load_context(file_path):
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        print(f"⚠️ Context file not found: {abs_path}. Using empty context.")
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 🔹 Load files
weather_instruction = load_instruction("instructions/weather.txt")
local_context = load_context("context.json")

# 🔹 Create Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# 🔹 Function to ask question with dynamic + local context
def ask_weather(question, context):
    context_text = "\n".join([f"- {k}: {v}" for k, v in context.items()])
    prompt = f"""
{weather_instruction}

Here’s the local context for this conversation:
{context_text}

User question: {question}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# 🔹 Example usage
if __name__ == "__main__":
    print("🌤 Weather Assistant Ready with JSON context!\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("👋 Goodbye!")
            break
        answer = ask_weather(user_input, local_context)
        print("AI:", answer)
