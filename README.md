# Course Forge — AI-Powered Learning Path Generator

🧭 Full-stack web application that generates personalized, structured learning roadmaps for any topic. Built with **FastAPI** (backend), **React + Vite** (frontend), **Azure OpenAI** (pathway generation), and **Ollama** (quiz generation).

> **For end users:** Use the web interface at `http://localhost:5173` — no setup needed.  
> **For developers:** Instructions below cover running both backend and frontend locally.

---

## 🚀 What It Does

- **Generate personalized learning paths:** Takes a topic, experience level, and daily time commitment as input
- **Dynamic timeline calculation:** AI calculates optimal learning duration based on complexity and available time
- **Live resources:** Automatically fetches curated resources (videos, articles, tutorials) for each week
- **Weekly milestones:** Structured curriculum with focus areas, practice tasks, and mini-exercises
- **Quiz generation & grading:** Generate milestone quizzes and receive AI-powered feedback (coming soon)
- **Responsive UI:** Clean, modern interface for viewing paths and taking quizzes

---

## 🛠️ Tech Stack

### Backend
- **Python 3.11+** with FastAPI
- **Azure OpenAI** — generates personalized learning paths
- **Ollama (qwen3.5:9b)** — generates and grades milestone quizzes *(in progress)*
- **Uvicorn** — ASGI server
- **Pydantic** — data validation
- **CORS middleware** — enables frontend communication

### Frontend
- **React 18** with Vite
- **Lucide React** — icons
- **Vite** — fast build tooling
- **Firebase** — deployment-ready

---

## 📁 Project Structure

```
Course_Forge/
├── backend/
│   ├── main.py                 # FastAPI entry point, CORS config
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Local config (create this yourself)
│   ├── models/
│   │   └── schemas.py           # Pydantic request/response models
│   ├── routes/
│   │   └── learning_path.py     # /api/generate endpoint
│   └── services/
│       ├── ai_service.py        # Azure OpenAI integration
│       ├── resource_service.py  # Resource fetching
│       └── quiz_service.py      # Ollama quiz generation (coming)
│
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── App.jsx              # Main React component
        ├── App.css              # Styling
        └── assets/              # Images and icons
```

---

## ⚙️ Setup Instructions

### Prerequisites
- **Python 3.11+** on your machine
- **Node.js 18+** for frontend
- **Azure OpenAI API credentials** (for pathway generation)
- **Ollama** (for quiz generation) — *optional for now, required when quiz endpoints go live*

---

### Backend Setup

#### 1. Navigate to the backend directory
```bash
cd Course_Forge/backend
```

#### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Create a `.env` file
In the `backend/` directory, create a `.env` file with your Azure OpenAI credentials:

```env
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-05-01-preview

# Frontend origin (for CORS)
ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

**⚠️ Never commit `.env`. It's already in `.gitignore`.**

#### 5. Start the backend server
```bash
uvicorn main:app --reload
```

The backend will start at `http://127.0.0.1:8000`  
Swagger docs available at `http://127.0.0.1:8000/docs`

---

### Frontend Setup

#### 1. Navigate to the frontend directory
```bash
cd Course_Forge/frontend
```

#### 2. Install dependencies
```bash
npm install
```

#### 3. Start the dev server
```bash
npm run dev
```

The frontend will start at `http://localhost:5173`

---

## 📖 API Endpoints

### Base URL
```
http://127.0.0.1:8000/api
```

### `POST /generate` — Generate a Learning Path
**Currently Implemented** ✅

Generate a personalized learning roadmap for any topic.

**Request:**
```json
{
  "topic": "Learn Python for Data Science",
  "experience_level": "intermediate",
  "hours_per_day": 2
}
```

**Response:**
```json
{
  "title": "Python for Data Science Learning Path",
  "calculated_total_weeks": 8,
  "daily_hours_commitment": 2,
  "weeks": [
    {
      "week_number": 1,
      "focus": "Python fundamentals and NumPy basics",
      "topics": ["Variables", "Data types", "NumPy arrays"],
      "practice": ["Install Python", "Write basic scripts"],
      "mini_exercise": "Create a NumPy array and perform basic operations",
      "live_resources": [
        {
          "title": "NumPy Tutorial",
          "url": "https://...",
          "source": "YouTube"
        }
      ]
    }
  ],
  "learning_outcomes": ["Understand Python basics", "Use NumPy effectively"]
}
```

---

### `POST /quiz/generate` — Generate a Quiz
**Coming Soon** 🚧 *(Ollama integration in progress)*

Generate multiple choice and open-ended questions for a milestone.

**Request:**
```json
{
  "milestone": "Python fundamentals and NumPy basics",
  "week_number": 1
}
```

**Response:**
```json
{
  "week_number": 1,
  "milestone": "Python fundamentals and NumPy basics",
  "questions": [
    {
      "question_number": 1,
      "type": "mcq",
      "question": "What is a NumPy array?",
      "options": ["A", "B", "C", "D"]
    }
  ]
}
```

---

### `POST /quiz/submit` — Grade Quiz Answers
**Coming Soon** 🚧 *(Ollama integration in progress)*

Submit quiz answers and receive AI-powered feedback.

**Request:**
```json
{
  "week_number": 1,
  "milestone": "Python fundamentals and NumPy basics",
  "questions": [...],
  "answers": [
    { "question_number": 1, "answer": "A" },
    { "question_number": 2, "answer": "True, because..." }
  ]
}
```

**Response:**
```json
{
  "week_number": 1,
  "score": 4,
  "total": 5,
  "passed": true,
  "feedback": [
    { "question_number": 1, "correct": true, "explanation": "..." }
  ],
  "overall_feedback": "Great understanding of the fundamentals!"
}
```

---

## 🤖 AI Model Routing

### Current Implementation
- **Azure OpenAI** — Generates personalized learning paths (configurable deployment)
- **Ollama (qwen3.5:9b)** — Quiz generation and grading *(coming soon)*

### Why Two Models?
- **Azure OpenAI** excels at complex curriculum design and understanding nuanced learning requirements
- **Ollama's qwen3.5:9b** efficiently generates and grades quizzes locally, reducing API costs and latency

---

## 🧪 Testing the API

### Option 1: Swagger UI (Recommended)
1. Start the backend: `uvicorn main:app --reload`
2. Open `http://127.0.0.1:8000/docs`
3. Click an endpoint → "Try it out" → Fill in request → "Execute"

### Option 2: cURL
```bash
curl -X POST "http://127.0.0.1:8000/api/generate" \
  -H "Content-Type: application/json" \
  -d '{"topic":"Learn Python","experience_level":"beginner","hours_per_day":2}'
```

### Option 3: Frontend UI
1. Start the backend and frontend
2. Open `http://localhost:5173`
3. Fill in the form and generate a path

---

## 🛠️ Setting Up Ollama for Quiz Generation

*This setup is optional for now. It becomes required once quiz endpoints are implemented.*

#### 1. Install Ollama
Download from https://ollama.com and follow installation instructions.

#### 2. Pull the required model
```bash
ollama pull qwen3.5:9b
```

**Note:** qwen3.5:9b requires ~6GB RAM. A machine with ≥16GB RAM is recommended.

#### 3. Start Ollama
```bash
ollama serve
```

#### 4. Update backend `.env`
```env
OLLAMA_HOST=http://localhost:11434
QUIZ_MODEL=qwen3.5:9b
```

---

## 📝 Project Contributions

### What my Partner (pratyushPtr) Built
- ✅ Full FastAPI backend with Azure OpenAI integration
- ✅ Learning path generation with dynamic timeline calculation
- ✅ Live resource fetching and injection
- ✅ React frontend with Vite and responsive UI
- ✅ CORS middleware for frontend-backend communication
- ✅ Dockerfiles for deployment

### What I'm Adding
- 🚧 Ollama integration for quiz generation (`quiz_service.py`)
- 🚧 `/api/quiz/generate` endpoint
- 🚧 `/api/quiz/submit` endpoint with AI grading
- 🚧 Quiz model routing and prompt engineering

---

## 🚀 Deployment

### Backend (Docker)
```bash
cd backend
docker build -t course-forge-backend .
docker run -p 8000:8000 --env-file .env course-forge-backend
```

### Frontend (Firebase/Vercel)
```bash
cd frontend
npm run build
firebase deploy
```

---

## 🐛 Troubleshooting

### Backend won't start
- Ensure Python 3.11+ is installed: `python --version`
- Verify virtual environment is activated
- Check `.env` file has all required Azure credentials

### Frontend can't connect to backend
- Ensure backend is running on `http://127.0.0.1:8000`
- Check CORS `ALLOWED_ORIGINS` in backend `.env`
- Open browser console (F12) for error messages

### Ollama errors (when quiz endpoints go live)
- Verify Ollama is running: `ollama serve` in a separate terminal
- Check model is installed: `ollama list`
- Verify `OLLAMA_HOST` in `.env` matches your setup

---

## 📚 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Ollama Documentation](https://ollama.com/)
- [Azure OpenAI API](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

---

## 👥 Team

| Role | Responsibility |
|------|-----------------|
| **pratyushPtr** | Full-stack development (FastAPI backend, React frontend, Azure OpenAI integration) |
| **You** | Ollama integration for quiz generation, prompt engineering, deployment |

---

## 📌 Notes for Developers

- **No keys in code:** All credentials live in `.env` — never commit them
- **Use `--reload` during dev:** Backend auto-restarts on file changes
- **Check Swagger:** Open `/docs` to explore endpoints and schemas
- **Quiz endpoints are TODO:** Frontend already calls them, but backend stubs need implementation
- **Model configs are flexible:** Override model names via `.env` without touching code

---

**Last updated:** June 2026  
**Status:** MVP with pathway generation live, quiz generation in progress