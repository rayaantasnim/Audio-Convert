<div align="center">

# 🎙️ Premium Hybrid Text-to-Speech (TTS) Generator

</div>

A robust, fail-safe Python utility that generates studio-quality voiceovers using cloud architecture, backed by an instantaneous 100% offline fallback system. Never let network drops interrupt your audio generation workflow again.

---

## ✨ Key Features

- **🌐 Hybrid Architecture:** Leverages Microsoft's cutting-edge cloud neural networks for crystal-clear, premium speech synthesis.
- **🔌 Zero-Lag Offline Fallback:** Automatically detects internet loss or API limits, instantly shifting production to local system hardware with **0% web dependency**.
- **🧠 Smart Gender Matching:** When falling back to offline mode, the system analyzes your original choice and selects a matching local voice (Male/Female) seamlessly.
- **💾 Auto-Increment Saving:** Generates smart, chronological file strings (`speech_001.mp3`, `speech_002.mp3`) so your past recordings are never overwritten.
- **📟 Interactive CLI Studio:** Features a dynamic, typing-animated console menu allowing real-time voice and accent selection.

---

## Architecture Overview

* **Phase 1: Input & Validation**
  * The user inputs a text string into the command line interface.
  * The script validates that the text is not empty and captures the chosen premium voice model.
* **Phase 2: Primary Generation Pipeline (Online)**
  * The program attempts a high-speed asynchronous connection to the Microsoft Azure Neural Voice cloud matrices using `edge-tts`.
  * **Success Path:** If the network is stable, it synthesizes a studio-grade, natural human voiceover file.
* **Phase 3: Automated Fail-Safe Pipeline (Offline)**
  * **Trigger Event:** If a network timeout, socket error, or API restriction is detected, the program intercepts the failure without crashing.
  * **Gender Alignment:** The script scans the host computer's operating system registry (Windows SAPI5, macOS SpeechSynthesis, or Linux Espeak) to match the originally selected voice gender.
  * **Local Processing:** The system triggers `pyttsx3` to compile the audio locally using 100% offline computing.
* **Phase 4: Direct Export**
  * The active pipeline passes the audio buffer to an auto-incrementing file stream, automatically saving it sequentially (e.g., `speech_001.mp3`) to prevent data loss.



## 🚀 Getting Started

### 📋 Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### 📦 Installation

Clone this repository or download the script file, then install the required dependencies using pip:

```bash
pip install edge-tts pyttsx3 asyncio
```

> **Note for Linux Users:** If you run into issues with the offline engine (`pyttsx3`), you may need to install the system audio layer tools:
> ```bash
> sudo apt-get update && sudo apt-get install espeak ffmpeg libespeak1
> ```

---

## 💻 Usage

Execute the script directly from your terminal terminal:

```bash
python tts_generator.py
```

### Interactive Flow:
1. **Input text:** Paste or type the text you want converted into speech.
2. **Select Voice Configuration:** Choose between available options:
   - `[1]` Microsoft Christopher (Male - US)
   - `[2]` Microsoft Ava (Female - US)
   - `[3]` Microsoft Brian (Male - UK)
3. **Output Generation:** The program automatically processes the audio and outputs a non-conflicting `.mp3` file in the native directory.

---

## 🛠️ Built With

* [edge-tts](https://github.com) - Interface for Microsoft Azure Cognitive Services text-to-speech.
* [pyttsx3](https://github.com) - Offline text-to-speech library supporting SAPI5, NSSpeechSynthesizer, and espeak.
* [asyncio](https://python.org) - Asynchronous I/O framework for concurrent network operations.

---

<hr>

<div align="center">

*Authorized by **Rayaan Tasnim** <br> 
© All rights reserved <br>
Powered by **Olympiad Edge** <br> 
Backed up by the **IDAI Universe***

</div>