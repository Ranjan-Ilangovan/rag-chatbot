# 🤖 AI Document Q&A Chatbot (RAG Pipeline)
### Ask questions about any PDF — powered by Llama3 + LangChain + Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-purple)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🔍 Overview

A fully local, privacy-first AI document assistant. Upload any PDF — a company report, research paper, legal document, or textbook — and ask natural language questions. The app reads the document, finds the most relevant sections using TF-IDF retrieval, and generates a cited answer using Llama3 running entirely on your machine.

**No API costs. No data sent to the cloud. Works completely offline.**

> Built to demonstrate RAG (Retrieval Augmented Generation) — the #1 most in-demand AI engineering skill in 2025.

---

## 🎯 What Problem Does It Solve?

Reading a 50-page report to find one answer wastes hours. This app lets you:

- Upload any PDF in seconds
- Ask plain English questions
- Get precise answers with page citations
- Chat history maintained throughout the session

---

## 🖥️ App Preview

<img width="248" height="546" alt="Screenshot 1" src="https://github.com/user-attachments/assets/b0116dad-c563-45f7-979e-512192e004b0" />
<img width="248" height="546" alt="Screenshot 2" src="https://github.com/user-attachments/assets/b0116dad-c563-45f7-979e-512192e004b0" />
<img width="248" height="546" alt="Screenshot 3" src="https://github.com/user-attachments/assets/b0116dad-c563-45f7-979e-512192e004b0" />
<img width="248" height="546" alt="Screenshot 4" src="https://github.com/user-attachments/assets/b0116dad-c563-45f7-979e-512192e004b0" />
<img width="248" height="546" alt="Screenshot 5" src="https://github.com/user-attachments/assets/b0116dad-c563-45f7-979e-512192e004b0" />




---

## ⚙️ How It Works — RAG Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    RAG PIPELINE                          │
│                                                          │
│  PDF Upload                                              │
│      ↓                                                   │
│  PyPDF reads all pages                                   │
│      ↓                                                   │
│  LangChain splits into 1000-word chunks                  │
│      ↓                                                   │
│  TF-IDF indexes all chunks instantly                     │
│                                                          │
│  User asks question                                      │
│      ↓                                                   │
│  TF-IDF finds top 3 most relevant chunks                 │
│      ↓                                                   │
│  Llama3 reads chunks + generates cited answer            │
│      ↓                                                   │
│  Answer + page citations shown to user                   │
└─────────────────────────────────────────────────────────┘
```

### Why RAG beats standard ChatGPT for documents:

| Standard ChatGPT | This RAG App |
|---|---|
| Relies on training memory | Reads your actual document |
| Can hallucinate facts | Answers grounded in source |
| No page references | Shows exact citations |
| Sends data to cloud | 100% local and private |
| Costs money per query | Completely free |

---

## 📁 Project Structure

```
rag-chatbot/
│
├── app.py                  # Streamlit web app (UI layer)
├── rag.py                  # RAG pipeline (AI logic layer)
├── requirements.txt        # Project dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose | Why I Chose It |
|---|---|---|
| Python 3.9+ | Core language | Best AI/ML ecosystem |
| LangChain | AI orchestration | Connects all components cleanly |
| TF-IDF Retriever | Document search | Fast, lightweight, no GPU needed |
| Ollama + Llama3 | Local LLM | Free, private, no API costs |
| Streamlit | Web interface | Python-only, production-ready UI |
| PyPDF | PDF extraction | Simple, reliable page-by-page reading |

---

## 🚀 Run It Yourself

### Prerequisites
- Python 3.9+
- Anaconda (recommended)
- Ollama installed ([ollama.com](https://ollama.com))
- Llama3 model downloaded

### Step 1 — Install Ollama and Llama3
```bash
# Download Ollama from ollama.com, then:
ollama pull llama3
```

### Step 2 — Clone the Repo
```bash
git clone https://github.com/YOUR-USERNAME/rag-chatbot.git
cd rag-chatbot
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the App
```bash
streamlit run app.py
```

### Step 5 — Use It
1. Open browser at `http://localhost:8501`
2. Upload any PDF using the sidebar
3. Wait for indexing (5-10 seconds)
4. Ask questions in the chat box
5. See answers with page citations

---

## 💡 Example Use Cases

| PDF Type | Example Question |
|---|---|
| Company Annual Report | "What was the revenue growth in 2023?" |
| Research Paper | "What methodology did the authors use?" |
| Legal Document | "What are the termination clauses?" |
| Your CV | "What are this candidate's key skills?" |
| Product Manual | "How do I reset the device?" |

---

## 🔑 Key Technical Concepts

**Chunking:** Documents are split into 1000-word overlapping segments so no context is lost at boundaries.

**TF-IDF Retrieval:** Finds the most relevant document chunks based on term frequency — fast, lightweight and works on any machine without a GPU.

**Retrieval Augmented Generation:** The top 3 most relevant chunks are passed to Llama3 alongside the question, grounding the answer in your actual document rather than AI memory.

**Local LLM:** Llama3 runs entirely on your laptop via Ollama — no internet required after setup, no data ever leaves your machine.

---

## 🔮 Future Improvements

- [ ] Switch to vector embeddings for semantic search
- [ ] Support multiple PDF uploads simultaneously
- [ ] Add document comparison feature
- [ ] Export Q&A session as PDF report
- [ ] Support Word documents and text files
- [ ] Deploy via Docker for self-hosted enterprise use

---

## 👤 Author

**Ranjan Ilangovan**
MSc Information Science (Data Analytics) — Northumbria University

🔗 [LinkedIn](https://www.linkedin.com/in/ranjan-ilangovan/) · 📧 ranjan28198@gmail.com · 🔗 [Churn Dashboard Project](https://github.com/YOUR-USERNAME/customer-churn-dashboard)

---

## 📌 Project Status

✅ RAG pipeline built and tested
✅ Streamlit UI complete  
✅ Chat history implemented
✅ Source citations working
✅ Fully local — no API costs
✅ Works on standard laptop hardware
✅ Fully private — runs locally via Streamlit, zero cloud dependency, no API costs
