# 🎌 AniMatch — AI Anime Recommender System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3.7-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red?style=for-the-badge&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?style=for-the-badge&logo=kubernetes)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector--Store-purple?style=for-the-badge)

**An AI-powered anime recommendation system built with RAG (Retrieval Augmented Generation)**

[Demo](#demo) · [Features](#features) · [Installation](#installation) · [Usage](#usage) · [Architecture](#architecture) · [Deployment](#deployment)

</div>

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Deployment](#deployment)
- [Monitoring](#monitoring)
- [Contributing](#contributing)

---

## 🎯 About the Project

AniMatch is an **AI-powered anime recommendation system** that uses **RAG (Retrieval Augmented Generation)** to recommend anime based on user preferences.

Instead of simple keyword search, it understands the **meaning** behind your query and finds semantically similar anime from a database of **1200+ titles**.

> **Example:**
> ```
> User: "I want a dark psychological anime like Death Note"
>
> AniMatch: 
> 1️⃣ Code Geass — Strategic mind games + power struggle
> 2️⃣ Monster    — Dark thriller with moral complexity  
> 3️⃣ Psycho-Pass — Dystopian psychological crime drama
> ```

---

## ✨ Features

- 🧠 **AI-Powered Search** — Understands meaning, not just keywords
- 🎯 **Top 3 Recommendations** — Curated picks with explanations
- ⚡ **Fast Response** — Powered by Groq's ultra-fast LLaMA 3
- 🗄️ **Vector Search** — ChromaDB for semantic similarity
- 🌐 **REST API** — FastAPI endpoint for integration
- 🐳 **Dockerized** — Easy deployment anywhere
- ☸️ **Kubernetes Ready** — Production-grade orchestration
- 📊 **Monitoring** — Grafana Cloud integration
- 🎨 **Beautiful UI** — Dark anime-themed Streamlit interface

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **LLM** | LLaMA 3 via Groq (Free) |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` |
| **Vector Store** | ChromaDB |
| **Framework** | LangChain 0.3.7 |
| **Frontend** | Streamlit |
| **API** | FastAPI + Uvicorn |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Cloud** | Google Cloud Platform (GCP) |
| **Monitoring** | Grafana Cloud |
| **Language** | Python 3.10 |

---

## 📁 Project Structure

```
ANIME_RECOMMENDATION/
│
├── 📂 app/
│   └── app.py                    # Streamlit UI
│
├── 📂 src/
│   ├── data_loader.py            # CSV loading & processing
│   ├── vector_store.py           # ChromaDB operations
│   ├── recommender.py            # LLM recommendation logic
│   └── prompt_template.py        # LLM prompt templates
│
├── 📂 pipeline/
│   ├── build_pipeline.py         # Training pipeline (run once)
│   └── pipeline.py               # Prediction pipeline
│
├── 📂 config/
│   └── config.py                 # API keys & model config
│
├── 📂 utils/
│   ├── logger.py                 # Logging setup
│   └── custom_exception.py       # Error handling
│
├── 📂 data/
│   ├── anime_with_synopsis.csv   # Raw dataset (1200+ anime)
│   └── anime_updated.csv         # Processed dataset
│
├── 📂 chroma_db/                 # Vector store (auto-generated)
│
├── 📂 logs/                      # Application logs
│
├── api.py                        # FastAPI REST API
├── setup.py                      # Package configuration
├── requirements.txt              # Dependencies
├── Dockerfile                    # Docker configuration
├── k8s.yaml                      # Kubernetes deployment
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    USER REQUEST                      │
│         "anime like Naruto with friendship"          │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              STREAMLIT UI / FastAPI                  │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│           PREDICTION PIPELINE (pipeline.py)          │
│                                                      │
│  Query ──► HuggingFace Embeddings ──► Vector        │
│                                        │             │
│                                        ▼             │
│                                   ChromaDB           │
│                                   Similarity         │
│                                   Search             │
│                                        │             │
│                                        ▼             │
│                              Top 5 Similar Anime     │
│                                        │             │
│                                        ▼             │
│                          Prompt Template + Context   │
│                                        │             │
│                                        ▼             │
│                          Groq LLaMA 3 (Free LLM)    │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              TOP 3 RECOMMENDATIONS                   │
│   1️⃣ Bleach  2️⃣ My Hero Academia  3️⃣ Demon Slayer   │
└─────────────────────────────────────────────────────┘
```

### RAG Pipeline (Training — Run Once)

```
anime_with_synopsis.csv
        │
        ▼ AnimeDataLoader
Cleaned + Processed CSV
        │
        ▼ CSVLoader
LangChain Documents
        │
        ▼ CharacterTextSplitter
Text Chunks (1000 chars)
        │
        ▼ HuggingFaceEmbeddings
Vectors [0.12, 0.87, ...]
        │
        ▼ ChromaDB
Saved to disk ✅
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10+
- Git
- Docker (for deployment)
- Minikube (for Kubernetes)

### Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/anime-recommender.git
cd anime-recommender
```

### Step 2 — Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -e .
```

### Step 4 — Setup Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API Key — Get free at https://console.groq.com
GROQ_API_KEY=your_groq_api_key_here

# HuggingFace Token — Get at https://huggingface.co/settings/tokens
HF_TOKEN=your_huggingface_token_here

# Model Configuration
MODEL_NAME=llama3-8b-8192
```

### Get API Keys

| Key | Where to Get | Cost |
|-----|-------------|------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | ✅ Free |
| `HF_TOKEN` | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | ✅ Free |

---

## 🚀 Usage

### Step 1 — Build Vector Store (Run Once!)

```bash
python -m pipeline.build_pipeline
```

This will:
- Load `data/anime_with_synopsis.csv`
- Convert to embeddings
- Save to `chroma_db/`

### Step 2 — Run Streamlit App

```bash
streamlit run app/app.py
```

Open: `http://localhost:8501`

### Step 3 — Run API (Optional)

```bash
python api.py
```

Open Swagger UI: `http://localhost:8000/docs`

---

## 🌐 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

#### `GET /` — Welcome
```bash
curl http://localhost:8000/
```

#### `GET /health` — Health Check
```bash
curl http://localhost:8000/health
```
**Response:**
```json
{
  "status": "healthy",
  "pipeline_loaded": true,
  "message": "Pipeline ready!",
  "version": "1.0.0"
}
```

#### `POST /recommend` — Get Recommendations
```bash
curl -X POST "http://localhost:8000/recommend" \
     -H "Content-Type: application/json" \
     -d '{"query": "dark psychological anime like Death Note"}'
```
**Response:**
```json
{
  "success": true,
  "query": "dark psychological anime like Death Note",
  "recommendation": "1️⃣ Code Geass...\n2️⃣ Monster...\n3️⃣ Psycho-Pass...",
  "response_time": 2.34
}
```

#### `GET /recommend/{query}` — Quick Recommendation
```bash
curl http://localhost:8000/recommend/anime%20like%20Naruto
```

---

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t llmops-app:latest .
```

### Run Container
```bash
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_key \
  -e HF_TOKEN=your_token \
  llmops-app:latest
```

### Access App
```
http://localhost:8501
```

---

## ☸️ Kubernetes Deployment

### Step 1 — Start Minikube
```bash
minikube start
```

### Step 2 — Inject Secrets
```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=your_groq_key \
  --from-literal=HF_TOKEN=your_hf_token
```

### Step 3 — Deploy Application
```bash
kubectl apply -f k8s.yaml
```

### Step 4 — Get App URL
```bash
minikube service llmops-service --url
```

### Step 5 — Monitor
```bash
# Check pods
kubectl get pods

# Check services
kubectl get services

# Check logs
kubectl logs <pod-name>
```

---

## 📊 Monitoring

This project uses **Grafana Cloud** for Kubernetes monitoring.

### What Gets Monitored
- Number of running pods
- CPU & Memory usage
- Pod health status
- Node metrics
- Service availability

### Setup Grafana Cloud
1. Create account at [grafana.com](https://grafana.com) (14-day free trial)
2. Connect your Kubernetes cluster
3. View dashboards in browser

---

## 🧪 Project Components

### `build_pipeline.py` — Training Pipeline
```bash
# Run once to create vector store
python -m pipeline.build_pipeline
```
- Reads CSV → Processes data → Creates embeddings → Saves to ChromaDB

### `pipeline.py` — Prediction Pipeline
- Loads saved ChromaDB
- Creates retriever
- Initializes AnimeRecommender
- Used by Streamlit app at runtime

---

## 🔧 Troubleshooting

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: src` | Run `python -m pipeline.build_pipeline` from root |
| `ModuleNotFoundError: langchain.text_splitter` | `pip install langchain-text-splitters` |
| `ModuleNotFoundError: langchain.chains` | Use `create_retrieval_chain` instead of `RetrievalQA` |
| `ModelProfile error` | Reinstall: `pip install langchain-huggingface==0.1.2` |
| `Pipeline not loaded` | Run `build_pipeline.py` first |
| `GROQ_API_KEY not found` | Check your `.env` file |

---

## 📦 Requirements

```txt
langchain==0.3.7
langchain-core==0.3.15
langchain-community==0.3.7
langchain-huggingface==0.1.2
langchain-groq==0.2.1
langchain-text-splitters==0.3.2
chromadb==0.5.0
streamlit==1.38.0
fastapi
uvicorn
sentence-transformers==3.1.1
python-dotenv==1.0.1
pandas==2.2.3
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Toqeer**

- GitHub: [@toqeer](https://github.com/toqeer)

---

## 🌟 Show Your Support

Give a ⭐ if this project helped you!

---

<div align="center">

**Built with ❤️ using LangChain · Groq LLaMA 3 · ChromaDB · Streamlit · Docker · Kubernetes**

🎌

</div>
