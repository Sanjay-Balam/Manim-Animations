import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
import re

load_dotenv()  # take environment variables from .env.

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")

app = Flask(__name__)

def get_manim_script_from_gemini(prompt):
    url = GEMINI_API_URL
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    params = {"key": GEMINI_API_KEY}
    response = requests.post(url, headers=headers, params=params, json=data)
    response.raise_for_status()
    # Extract the code from the response (adjust as per actual API response structure)
    script = response.json()['candidates'][0]['content']['parts'][0]['text']
    return script

def extract_python_code(script):
    # This will extract code between ```python ... ```
    match = re.search(r"```python(.*?)```", script, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback: remove any triple backticks
    return script.replace("```", "").strip()

def save_script_to_file(code, filename="generated_manim.py"):
    with open(filename, "w") as f:
        f.write(code)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    try:
        script = get_manim_script_from_gemini(prompt)
        code = extract_python_code(script)
        save_script_to_file(code)  # Save as generated_manim.py
        print("This is the script", code)
        return jsonify({"script": code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)