# AI Learning Buddy 🤖

An AI-powered learning assistant built using Python and locally running Large Language Models (LLMs) through Ollama.

The goal of this project is to create a beginner-friendly AI learning companion that explains programming concepts step by step, answers questions, remembers previous conversations, and helps learners understand coding through practical examples.

## 🎯 Project Objectives

- Build an AI learning assistant using Python.
- Integrate locally hosted LLMs using Ollama.
- Implement dynamic prompt management.
- Track token usage and response performance.
- Develop persistent conversation memory.
- Provide beginner-friendly programming explanations.

## 🛠️ Technologies Used

- Python
- Ollama
- Llama 3.2 (1B)
- JSON
- Python OOP
- Git & GitHub

## 🚀 Features and Development Progress

### 1. LLM Integration
- Integrated Ollama with Python.
- Connected to the Llama 3.2 (1B) model.
- Implemented AI question-and-answer functionality.

### 2. Prompt Management
- Developed a dynamic prompt management system.
- Organized prompts for consistent AI responses.
- Tested prompt manager integration.

### 3. Token Usage Tracking
- Implemented token usage reporting.
- Track input and output tokens.
- Calculate total token usage.
- Monitor response performance.

### 4. Conversation Memory (In Progress)
- Developing conversation history management.
- Implementing persistent memory using JSON.
- Working on contextual follow-up questions.
- Improving the assistant's ability to recall previous conversations.

## 📂 Project Structure

```
AI_Learning_Buddy_2.0/
│
├── app/
├── data/
├── docs/
│
├── src/
│   ├── __init__.py
│   ├── conversation_memory.py
│   ├── llm_client.py
│   └── prompt_manager.py
│
├── tests/
│   ├── __init__.py
│   └── test_memory.py
│
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

*Note: This is the proposed structure. Actual filenames and folders may vary as development progresses.*

## ⚙️ Getting Started

### 1. Install Python

Install Python 3.10 or later.

### 2. Install Ollama

Download Ollama from:

https://ollama.com/

### 3. Download the model

```bash
ollama pull llama3.2:1b
```

### 4. Install project dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python src/main.py
```

## 📌 Current Development Focus

- Completing persistent conversation memory.
- Improving contextual understanding.
- Testing conversation history retrieval.
- Improving response quality and consistency.

## 🔮 Future Enhancements

- Interactive learning sessions.
- Personalized learning paths.
- Coding exercises and quizzes.
- Learning progress tracking.
- Improved memory retrieval.

## 👩‍💻 About the Project

This project is being developed as a hands-on learning journey to explore Python programming, LLM integration, prompt engineering, and AI application development.

**Status:** Actively Developing 🚀
