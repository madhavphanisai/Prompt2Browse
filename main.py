import requests
import json
from playwright.sync_api import sync_playwright
import time
import re

# 🔐 Your Gemini API key here
API_KEY = "your-gemini-api-key-here"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def parse_prompt_to_steps(prompt):
    # Formatted instruction for Gemini
    instruction = f"""
You are a browser automation assistant.
Convert this user instruction into a JSON list of step-by-step browser actions.

Valid action types:
- go_to: {{ "action": "go_to", "url": "https://..." }}
- type:  {{ "action": "type", "selector": "CSS_SELECTOR", "text": "..." }}
- click: {{ "action": "click", "selector": "CSS_SELECTOR" }}
- press: {{ "action": "press", "key": "Enter" }}

User Instruction: {prompt}

Respond only with the JSON list of actions.
"""

    headers = { "Content-Type": "application/json" }

    payload = {
        "contents": [
            {
                "parts": [
                    { "text": instruction }
                ]
            }
        ]
    }

    response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        try:
            gemini_output = response.json()
            raw_text = gemini_output["candidates"][0]["content"]["parts"][0]["text"].strip()
            # Clean markdown like ```json
            cleaned = re.sub(r"^```json|```$", "", raw_text.strip(), flags=re.MULTILINE)
            steps = json.loads(cleaned)
            return steps
        except Exception as e:
            print("❌ Failed to parse Gemini output:", e)
            print("🔍 Raw response:\n", raw_text)
            return []
    else:
        print("❌ Gemini API error:", response.status_code, response.text)
        return []

def perform_browser_actions(actions):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for action in actions:
            try:
                if action["action"] == "go_to":
                    print(f"🌐 Navigating to {action['url']}")
                    page.goto(action["url"])
                elif action["action"] == "type":
                    print(f"⌨️ Typing '{action['text']}' in {action['selector']}")
                    page.wait_for_selector(action["selector"])
                    page.fill(action["selector"], action["text"])
                elif action["action"] == "click":
                    print(f"🖱️ Clicking {action['selector']}")
                    page.wait_for_selector(action["selector"])
                    page.click(action["selector"])
                elif action["action"] == "press":
                    print(f"⏎ Pressing {action['key']}")
                    page.keyboard.press(action["key"])
                else:
                    print("⚠️ Unknown action type:", action)
            except Exception as e:
                print("❌ Error executing action:", e)

        time.sleep(5)
        page.screenshot(path="screenshot.png")
        print("📸 Screenshot saved as screenshot.png")
        browser.close()

if __name__ == "__main__":
    user_prompt = input("🧠 Enter your prompt: ")
    steps = parse_prompt_to_steps(user_prompt)

    if steps:
        print("✅ Running browser automation...")
        perform_browser_actions(steps)
    else:
        print("⚠️ No valid steps received from Gemini.")
