# 🤖 AI Interview Assistant

An AI-powered Interview Assistant built using **Python**, **Streamlit**, and **Google Gemini API** that helps candidates prepare for technical interviews by analyzing resumes, generating personalized interview questions, conducting AI-driven interviews, evaluating responses, and providing detailed interview reports.

---

## 🚀 Features

### 📄 Resume Analysis
- Upload PDF Resume
- Resume Parsing
- Candidate Profile Extraction
- AI-based Resume Analysis

### 📊 ATS Resume Analysis
- ATS Score Generation
- Skills Match Analysis
- Missing Keywords Detection
- Resume Strengths
- Resume Weaknesses
- Improvement Suggestions

### 🎯 AI Interview
- Resume-based Interview Questions
- Technical Question Generation
- Behavioral Questions
- Personalized Interview Flow

### 🎤 Voice Support
- Speech-to-Text Answer Recording
- Manual Text Editing
- Interactive Interview Experience

### 📈 AI Evaluation
- Technical Knowledge Assessment
- Communication Skills Evaluation
- Problem Solving Assessment
- Confidence Level Analysis
- Hiring Recommendation

---

# 🏗️ Project Architecture

```
                    Resume (PDF)
                          │
                          ▼
                 Resume Parsing Service
                          │
                          ▼
                  Interview Supervisor
                          │
      ┌──────────────┬───────────────┬──────────────┐
      ▼              ▼               ▼              ▼
 Resume Agent     ATS Agent     Question Agent   Evaluation Agent
      │              │               │              │
      └──────────────┴───────────────┴──────────────┘
                          │
                          ▼
                  Streamlit User Interface
```

---

# 🧠 AI Agents

### Resume Agent
- Extracts candidate information
- Identifies skills
- Detects projects
- Creates candidate profile

### ATS Agent
- Performs ATS Resume Analysis
- Calculates ATS Score
- Finds missing keywords
- Suggests resume improvements

### Question Agent
- Generates resume-based interview questions
- Technical Questions
- HR Questions
- Project-based Questions

### Evaluation Agent
- Evaluates candidate responses
- Scores technical knowledge
- Measures communication
- Provides hiring recommendation

### Supervisor Agent
- Coordinates all AI agents
- Controls interview workflow
- Manages interview lifecycle

---

# 💻 Tech Stack

## Programming Languages
- Python
- SQL

## Artificial Intelligence
- Google Gemini 2.5 Flash API
- Generative AI
- Prompt Engineering
- Multi-Agent AI Architecture

## NLP
- Resume Parsing
- Speech-to-Text
- AI Response Evaluation

## Framework
- Streamlit

## Libraries
- google-generativeai
- streamlit
- streamlit-mic-recorder
- PyPDF2
- python-dotenv
- Regex

## Tools
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```
AI_Interview_Assistant
│
├── agents
│   ├── ats_agent.py
│   ├── evaluation_agent.py
│   ├── question_agent.py
│   ├── resume_agent.py
│   └── supervisor.py
│
├── llm
│   └── gemini.py
│
├── services
│   ├── resume_service.py
│   └── voice_service.py
│
├── main.py
├── style.css
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Interview-Assistant.git
```

Move into project

```bash
cd AI-Interview-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the project

```bash
streamlit run main.py
```

---

# 📸 Screenshots

- Resume Upload
- ATS Resume Analysis
- AI Interview Questions
- Voice Recording
- AI Interview Report

(Add screenshots here)

---

# 🔮 Future Enhancements

- LangGraph Integration
- Retrieval-Augmented Generation (RAG)
- Vector Database (FAISS / ChromaDB)
- AI Follow-up Questions
- Text-to-Speech
- PDF Interview Report
- Interview History
- User Authentication
- Cloud Deployment
- Docker Support

---

# 🎯 Learning Outcomes

- Multi-Agent AI Design
- Generative AI Applications
- Prompt Engineering
- Resume Parsing
- Speech-to-Text Integration
- ATS Resume Analysis
- AI Interview Evaluation
- Streamlit Application Development
- API Integration
- Git & GitHub Workflow

---

# 👩‍💻 Author

**Rakshitha**

Information Technology Graduate

GitHub: https://github.com/E-rakshitha

---
