
<h1 align="center">🔍 Autocomplete Search System with Frequency Count</h1>

<div align="center">
  <table>
    <tr>
      <td width="55%">
        <h3><b>About the Project</b></h3>
        <p>
          This intelligent Python-based search engine combines a fast <strong>Trie data structure</strong> with <strong>fuzzy matching</strong> and an <strong>LRU Cache</strong> to create a real-time autocomplete experience. 
          It accepts both <code>text</code> and <code>voice</code> inputs, ranks results by frequency, and offers search analytics.
        </p>
      </td>
      
  </table>
</div>

---

## 📁 Project Structure

```bash
Autocomplete_search_system_with_frequency_count/
├── main.py                # Entry point; handles user input and flow
├── trie.py                # Implements the Trie data structure
├── search_engine.py       # Handles frequency tracking and suggestions
├── fuzzy_search.py        # Adds fuzzy matching functionality
├── lru_cache.py           # Implements LRU caching for faster access
├── products.txt           # Dataset of available product names
└── README.md              # Project documentation (this file)
```

---

## ✅ Features

- 🔤 Fast **prefix-based autocomplete** using Trie
- 🧠 **Fuzzy matching** with Levenshtein distance (DP)
- 📊 **Frequency-based search ranking**
- ⚡ **LRU Cache** to optimize repeated queries
- 🎤 **Voice recognition input** option
- 📈 Built-in **search analytics dashboard**
- 📄 Loads suggestions from a custom `products.txt` file

---

## 🧰 Tech Stack

| Tool / Concept         | Description                        |
|------------------------|------------------------------------|
| 🐍 Python 3.x          | Programming Language               |
| 📁 Standard Library     | No third-party packages needed     |
| 🌳 Trie Structure       | For prefix-based autocomplete      |
| 🔁 LRU Cache            | Speeds up recent query results     |
| 🔡 Levenshtein Distance| Fuzzy matching implementation      |
| 🎙️ Voice Input         | Voice-to-text feature (via `speech_recognition`) |

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/Technicalarpan/Autocomplete_search_system_with_frequency_count.git
cd Autocomplete_search_system_with_frequency_count
```

### Step 2: Run the Program

```bash
python main.py
```

You can now type or speak your query and explore smart suggestions.

---

## 💻 Sample Output

```
Loading product list...
Smart Search & Autocomplete System Initialized.
Type your search query or 'voice' to speak, 'analytics' for stats, 'exit' to quit:
Search: laptop
Suggestions: ['laptop bag', 'laptop cooling pad', 'laptop backpack', 'laptop docking station', 'laptop charger']
Selected: laptop bag
```

### 🧠 Fuzzy Matching

```
Search: zeiss lenus
Suggestions: ['zeiss lenses']
Selected: zeiss lenses
```

### 🎤 Voice Input

```
Search: voice
🎙️ Speak your search query...
🗣️ You said: laptop
Suggestions: ['laptop bag', 'laptop cooling pad', 'laptop backpack', 'laptop docking station', 'laptop charger']
Selected: laptop bag
```

### 📊 Analytics Output

```
Search: analytics

📊 Total Searches Made: 16
🔝 Top searched products:
1. laptop bag - 2 times 
2. fitbit versa - 2 times 
3. leica m10 - 2 times 
4. bluetooth headset - 1 times 
5. gopro hero 10 - 1 times 
```

---

## ⚙️ How It Works

| Module           | Responsibility                           |
|------------------|-------------------------------------------|
| `trie.py`        | Builds and manages the prefix tree        |
| `fuzzy_search.py`| Matches similar inputs using edit distance |
| `lru_cache.py`   | Optimizes performance with recent lookups |
| `search_engine.py`| Handles ranking and history               |
| `main.py`        | Orchestrates interaction, voice, and analytics |
| `products.txt`   | Base product database                     |

---

## 📦 Requirements

- Python 3.x  
- Optional: `speech_recognition` for voice feature

> ✅ No external libraries required unless you enable voice input

---

## 🧪 Sample Dataset

Contents of `products.txt`:

```
iPhone 13
iPhone 12
iPhone Case
Headphones
Hair Dryer
HDMI Cable
Hard Disk
Hat
...
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Use, modify, and distribute freely.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---

## 👨‍💻 Author

| Name             | Contact Info                                  |
|------------------|-----------------------------------------------|
| Arpan Mukherjee | [@Technicalarpan](https://github.com/Technicalarpan) • techarpan1@gmail.com |

---

## ⭐ Give A Star

If this project helped you, consider giving it a ⭐ on GitHub to help others discover it!

---



<h3 align="center">💫 Made with ❤️ by Arpan Mukherjee 💫</h3>
