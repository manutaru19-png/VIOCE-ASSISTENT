# Voice Assistant using Python

## 📌 Project Overview

This project is a **simple Voice-Controlled Assistant built with Python**.
The assistant listens to the user's voice commands, converts them to text, and performs actions such as opening websites, telling the time, and responding with speech.

It uses **speech recognition and text-to-speech technologies** to interact with the user.

---

## 🚀 Features

* 🎤 Capture voice commands using microphone
* 🗣 Convert speech to text
* 🔊 Respond using text-to-speech
* 🌐 Open websites like Google, YouTube, WhatsApp, Instagram
* ⏰ Tell current time
* 🤖 Basic conversation support

---

## 🛠 Technologies Used

* Python 3.x
* speech_recognition
* pyttsx3
* webbrowser
* datetime
* pyjokes (optional)

---

## 📦 Required Libraries

Install the required libraries before running the program.

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
pip install pyjokes
```

If `pyaudio` fails to install:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 📂 Project Structure

```
voice_assistant/
│
├── voice_assistant.py
├── README.md
```

---

## ▶️ How to Run the Project

1. Open **Command Prompt / Terminal**
2. Navigate to the project folder

```bash
cd path_to_project_folder
```

3. Run the program

```bash
python voice_assistant.py
```

---

## 🎤 Example Voice Commands

You can say commands like:

* "Open Google"
* "Open YouTube"
* "Open WhatsApp"
* "Open Instagram"
* "What is the time"
* "Tell me a joke"

---

## ⚠️ Common Errors and Fixes

### ModuleNotFoundError

Install the missing module using:

```bash
pip install module_name
```

Example:

```bash
pip install pyjokes
```

### Microphone Not Detected

Make sure:

* Microphone is connected
* Microphone permission is enabled

---

## 📈 Future Improvements

* Add weather information
* Add email sending feature
* Control system applications
* Integrate AI chatbot

---

## 👨‍💻 Author

MANOJ KS 
PYTHIN INTER
