# 🧠 Prompt2Browse

**Prompt2Browse** is an AI-powered browser automation tool that transforms natural language prompts into real-time web interactions — then captures the final result as a **PNG screenshot**.

---

## 🚀 Features

- Accepts **natural language input**
- Uses **Gemini API** (Google) for intelligent prompt understanding
- Automates browser actions using **Playwright**
- Saves the final output as a **screenshot** (PNG format)
- Lightweight and extensible

---

## 💬 Example Prompt

```

Go to Amazon and search for a watch

````

**What happens:**  
✅ The prompt is interpreted using Gemini API  
✅ The browser opens and navigates to Amazon  
✅ It searches for "watch"  
✅ A screenshot of the final result page is saved as `output.png`

---

## 🛠 Tech Stack

- **Python** – Core logic
- **Playwright** – Browser automation
- **Gemini API** – Natural language understanding

---

## 🧑‍💻 Installation

### 1. Clone the repository
```bash
git clone https://github.com/madhavphanisai/prompt2browse.git
cd prompt2browse
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

In `main.py`, replace the API key value:

```python
API_KEY = "your-gemini-api-key-here"
```

### 4. Run the project

```bash
python main.py
```

---

## 📸 Output

After execution, a screenshot will be saved as:

```
output.png
```

This represents the final state of the webpage based on the user's prompt.

---

## 📁 Project Structure

```
prompt2browse/
├── main.py            # Main script
├── requirements.txt   # Project dependencies
└── output.png         # Screenshot saved after execution
```

---

## 🔐 API Key Security

Make sure to keep your Gemini API key secure. For production use, store it using environment variables or a `.env` file and avoid pushing secrets to public repositories.

---

## 🤝 Contributing

Have ideas or suggestions?
Feel free to fork the repo, open issues, or submit pull requests!

---

## 🔗 Connect

Built with 💡 by [Pasupuleti Madhav Phani Sai](https://www.linkedin.com/in/madhavphanisai)


