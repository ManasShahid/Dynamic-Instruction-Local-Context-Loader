# 🧠 Dynamic Instruction & Local Context Loader (DY_INS)

A lightweight Python project to **dynamically load AI instructions and local context** from external files — making your AI tools flexible, modular, and easy to scale.

This project demonstrates how to separate **logic**, **data**, and **context** for building smarter, more maintainable AI applications.

---

## 🚀 Features

* 📁 Load AI instructions (like weather, math, or chemistry) directly from `.txt` files
* 💾 Load and use a **local context (`context.json`)** for memory and state persistence
* ⚡ Automatically handles missing or empty files
* 🧩 Modular & scalable — add or modify instructions without touching the main code
* 🧠 Ideal for AI agents, automation scripts, or any context-aware Python app

---

## 🧰 Folder Structure

```
dy_ins/
│
├── main.py                # Main application file
├── instructions/
│   ├── weather.txt        # Example instruction file
│   ├── math.txt           # (optional)
│   └── chemistry.txt      # (optional)
│
└── context.json           # Local context data
```

---

## 🧠 Example `main.py`

```python
import json
import os

def load_instruction(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ Instruction file not found: {file_path}")
        return ""

def load_context(context_path):
    try:
        with open(context_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ Context file not found: {context_path}. Using empty context.")
        return {}

# Paths
instruction_file = os.path.join("instructions", "weather.txt")
context_file = "context.json"

# Load files
instruction = load_instruction(instruction_file)
context = load_context(context_file)

print("✅ Instruction Loaded:")
print(instruction)
print("\n🌍 Context:")
print(context)
```

---

## 📘 Example `context.json`

```json
{
  "location": "Dubai",
  "units": "Celsius",
  "user_preferences": {
    "language": "English"
  }
}
```

---

## 📜 Example `weather.txt`

```
Provide the current temperature, humidity, and conditions
based on the user's location from the context file.
```

---

## 🪄 How to Run

```bash
# Step 1: Activate virtual environment (if not already)
.venv\Scripts\activate

# Step 2: Run the app
python main.py
```

---

## 🧩 Add a New Instruction

Just drop a new `.txt` file into the `instructions` folder — for example:

**math.txt**

```
Perform basic arithmetic calculations using the user's input.
```

Then, update this line in `main.py`:

```python
instruction_file = os.path.join("instructions", "math.txt")
```

That’s it — your new instruction is live! ⚡

---

## 🌍 Future Improvements

* 🔄 Auto-update context after execution
* 🧠 Integrate with OpenAI / LangChain for dynamic reasoning
* ☁️ Cloud-sync for shared contexts between devices

---

## 💡 Author

**Manas Shahid**
🧠 Developer & Digital Marketing Expert
📍 Pakistan

🔗 [LinkedIn](https://www.linkedin.com/in/manasshahid/)
💻 [GitHub](https://github.com/ManasShahid)

