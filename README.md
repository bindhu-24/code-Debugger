# 🤖 AI Code Review Agent

<<<<<<< HEAD
An AI-powered code review system that analyzes source code for bugs, security vulnerabilities, code smells, readability issues, and best practice violations using Large Language Models and LangGraph orchestration.

## Features

* Multi-language code review support

  * Python
  * JavaScript
  * Java
  * C++
  * Go
* Security vulnerability detection
* Bug risk identification
* Code smell detection
* Readability analysis
* Best practice recommendations
* RAG-powered coding standards retrieval
* LangGraph workflow orchestration
* Review history tracking
* Code health score visualization
* Streamlit frontend UI
* FastAPI backend API

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* LangGraph
* LangChain
* OpenAI GPT Models

### Frontend

* Streamlit

### Database

* PostgreSQL
* pgvector

---

## Project Structure

```text
code-Debugger/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── graph/
│   ├── llm/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── pages/
│       └── review_history.py
│
├── requirements.txt
├── README.md
└── .env
=======
An AI-powered Code Review Agent built with **FastAPI, LangGraph, OpenAI GPT, PostgreSQL, pgvector, Docker, and Streamlit**.

The application analyzes source code, detects security vulnerabilities, bug risks, performance issues, readability problems, and best-practice violations, then generates a structured review report with an overall quality score.

---

# Features

- AI-powered code review
- Multi-language support
  - Python
  - JavaScript
  - Java
  - C++
  - Go
- Quality score (0–100)
- Security vulnerability detection
- Bug risk analysis
- Performance suggestions
- Readability improvements
- Best practice recommendations
- Review history
- Dockerized deployment
- PostgreSQL storage
- REST API with FastAPI
- Interactive Streamlit UI

---

# Tech Stack

## Backend

- FastAPI
- LangGraph
- OpenAI GPT
- SQLAlchemy
- PostgreSQL
- pgvector
- Pydantic

## Frontend

- Streamlit

## DevOps

- Docker
- Docker Compose

---

# Project Structure

```
app/
│
├── database/
│   ├── connection.py
│   ├── dependencies.py
│   └── models.py
│
├── graph/
│   ├── graph_builder.py
│   └── nodes.py
│
├── routes/
│   ├── review.py
│   └── history.py
│
├── schemas/
│   └── review_schema.py
│
├── services/
│   ├── llm_service.py
│   ├── review_service.py
│   └── review_history_service.py
│
├── prompts/
│   └── review_prompt.py
│
├── main.py
│
frontend/
│
├── streamlit_app.py
└── pages/
    └── review_history.py
>>>>>>> a9d6b23 (Fixed the review page error)
```

---

<<<<<<< HEAD
## LangGraph Workflow

1. Accept source code from user.
2. Store submission in database.
3. Retrieve relevant coding standards using RAG.
4. Analyze code using LLM.
5. Generate structured review report.
6. Save review results.
7. Return response to UI.

---

## API Endpoints

### Review Code

```http
POST /review
```

Example Request:

```json
{
  "language": "python",
  "code": "print('Hello World')",
  "context": "Example API"
=======
# Architecture

```
          User

            │

            ▼

      Streamlit UI

            │

            ▼

        FastAPI API

            │

            ▼

      LangGraph Agent

            │

            ▼

      OpenAI GPT Model

            │

            ▼

Structured Review Report

            │

            ▼

      PostgreSQL Database
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/code-debugger.git

cd code-debugger
```

---

Install dependencies

```bash
pip install -r requirements.txt
```

---

Create a `.env`

```env
OPENAI_API_KEY=your_api_key

DATABASE_URL=postgresql://postgres:postgres@db:5432/code_review_db
```

---

# Run using Docker

```bash
docker compose up --build
```

---

Frontend

```
http://localhost:8501
```

Backend

```
http://localhost:8000/docs
```

---

# API Endpoints

## Review Code

```
POST /review
```

Example Request

```json
{
  "language":"python",
  "code":"print('Hello World')",
  "context":"Example"
>>>>>>> a9d6b23 (Fixed the review page error)
}
```

---

<<<<<<< HEAD
### Review History

```http
GET /reviews
```

Returns all previously generated code reviews.

---

## Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
=======
## Review History

```
GET /reviews
```

Returns previously generated code review reports.

---

# Example Output

```json
{
  "review_id": 1,
  "status":"completed",
  "review":{
      "score":85,
      "summary":"The code is functional but has readability issues.",
      "issues":[
          {
              "severity":"Medium",
              "category":"Readability",
              "description":"Variable names are unclear.",
              "recommendation":"Use descriptive variable names."
          }
      ]
  }
}
>>>>>>> a9d6b23 (Fixed the review page error)
```

---

<<<<<<< HEAD
## Running the Frontend

Activate virtual environment:

```bash
venv\Scripts\activate
```

Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

---

## Example Issues Detected

* SQL Injection
* Hardcoded Secrets
* Command Injection
* Infinite Loops
* Division by Zero
* Magic Numbers
* Missing Type Hints
* Duplicate Code
* Performance Bottlenecks

---

## Future Enhancements

* GitHub Pull Request Reviews
* SonarQube Integration
* PDF Report Export
* Authentication and User Management
* CI/CD Integration
* Docker Deployment

---
=======
# Future Enhancements

- Authentication
- User Accounts
- AI-generated code fixes
- GitHub Pull Request Integration
- PDF Report Export
- RAG-based coding standards retrieval
- Syntax highlighting improvements
- CI/CD deployment
- Rate limiting
- Logging & monitoring

---

# Screenshots

Add screenshots of:

- Review Page
- Review History
- Swagger API
- Docker Containers

---

>>>>>>> a9d6b23 (Fixed the review page error)
