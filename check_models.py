# check_models.py
import google.generativeai as genai
from config import API_KEY   # make sure your API_KEY is set in config.py

# Configure the API
genai.configure(api_key=API_KEY)

# List all available models
print("🔍 Fetching available models...\n")
models = genai.list_models()

for m in models:
    name = m.name
    supported = getattr(m, "supported_generation_methods", [])
    print(f"✅ {name} | Supports generateContent? {'generateContent' in supported}")
