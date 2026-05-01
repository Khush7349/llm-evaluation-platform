# 🔥 Elite LLM Evaluation Platform

An advanced platform for **evaluating, comparing, and optimizing prompts** using Large Language Models (LLMs).

This system enables **automated scoring, dataset-based benchmarking, and prompt performance analysis** using an LLM-as-judge approach.

---

## 🚀 Overview

LLMs are powerful—but evaluating prompt quality is hard.

This project solves that by:

- Running multiple prompts on the same inputs
- Scoring outputs using an LLM evaluator
- Aggregating performance across datasets
- Ranking prompts via a leaderboard
- Identifying weak cases (failure analysis)

---

## 🧠 Architecture

```
User Inputs + Prompts
↓
LLM Generation (Ollama)
↓
LLM-as-Judge Evaluation
↓
Scoring Engine (Relevance, Clarity, Accuracy)
↓
Caching Layer
↓
Aggregation + Leaderboard
↓
Streamlit Dashboard
```

---

## ✨ Features

### 🧪 Prompt Evaluation
- Compare multiple prompts side-by-side
- Generate outputs for each input

### 📊 Multi-Metric Scoring
- Relevance
- Clarity
- Accuracy

### 🏆 Leaderboard System
- Rank prompts based on aggregated scores
- Identify best-performing prompt

### 📚 Dataset-Based Benchmarking
- Evaluate prompts across multiple inputs
- Compute average performance

### ⚠️ Failure Analysis
- Detect weak cases where prompts underperform

### ⚡ Caching System
- Avoid redundant LLM calls
- Improve performance

### 🧠 LLM-as-Judge
- Uses LLM to evaluate LLM outputs

---

## 🧩 Tech Stack

- **Backend** → FastAPI  
- **Frontend** → Streamlit  
- **LLM** → Ollama (Mistral)  
- **Data Handling** → Python  
- **Evaluation Engine** → Custom scoring system  

---

## 📂 Project Structure

```
llm-evaluation-platform/
│
├── backend/
│ ├── main.py
│ ├── evaluator.py
│ ├── llm.py
│ ├── scoring.py
│ ├── cache.py
│ ├── logger.py
│ ├── test_basic.py
│ └── init.py
│
├── frontend/
│ └── app.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository


- git clone https://github.com/your-username/llm-evaluation-platform.git

- cd llm-evaluation-platform


---

### 2. Install Dependencies


- pip install -r requirements.txt


---

### 3. Start Ollama


- ollama run mistral


---

### 4. Run Backend


- uvicorn backend.main:app --reload


---

### 5. Run Frontend


- streamlit run frontend/app.py


---

## 🧪 Usage

1. Enter multiple inputs (one per line)
2. Provide prompts
3. Click **Evaluate**
4. View:
   - Leaderboard rankings
   - Score breakdown
   - Failure cases

---

## 🎯 Key Highlights

- LLM-as-judge evaluation system  
- Multi-metric scoring pipeline  
- Dataset-based benchmarking  
- Real-time UI dashboard  
- Modular backend architecture  


---

## 👤 Author

Khushi Sharma

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub
